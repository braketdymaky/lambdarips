var div_resultado = $("#resultado");
var div_spinner = $("#spinner-cargando");
var btn_validar = $("#btn-validar");
var btn_cancelar = $("#btn-cancelar-rips");
var resultado_proceso = '';
var ajaxPool = [];

$(document).ready(function () {
    btn_cancelar.hide();
    $("#validar-zip").on('submit', enviarRips);
});

$(".custom-file-input").on("change", function () {
    var nombre = $(this).val().split("\\").pop();
    if (nombre === '') {
        $(".custom-file-label").text('Seleccionar archivo zip');
    } else {
        $(".custom-file-label").text(nombre);
    }
    $("#resultado").hide();
});


function cancelarPeticion() {
    btn_validar.prop("disabled", false);
    div_resultado.show();
    div_spinner.hide();
    $.each(ajaxPool, function (idx, peticion) {
        peticion.abort();
    });
    btn_cancelar.hide();
    $("#resultado-mensaje").text("La validación del RIPS ha sido cancelada.");
}

function enviarRips(event) {
    event.preventDefault();
    $('#spinner-mensaje').text("1. Validando estructura del RIPS...");
    btn_validar.prop("disabled", true);
    btn_cancelar.show();
    div_resultado.hide();
    div_spinner.show();

    var archivo_rips = new FormData($("#validar-zip").get(0));

    request = $.ajax({
        url: $(this).attr('action'),
        type: 'POST',
        data: archivo_rips,
        cache: false,
        processData: false,
        contentType: false,
        beforeSend: function (jqXHR, settings) {
            ajaxPool.push(jqXHR);
        },
        success: function (respuesta) {
            switch (respuesta.statusCode) {
                case 200:
                    if (respuesta.body && respuesta.body.length === 2) {
                        $('#spinner-mensaje').text("2. Validando datos del RIPS...");
                        validarDatosRips(respuesta.datos_extra);
                    } else {
                        errorEnRips(respuesta);
                    }
                    break;
                case 400:
                    errorEnZip(respuesta);
                    break;
                case 409:
                    errorEnZip(respuesta);
                    break;
                case 500:
                    errorEnZip(respuesta);
                    break;
                default:
                    errorInterno(respuesta);
                    break;
            }
            if (respuesta.statusCode === 200){
                delete respuesta['datos_extra'];
            }
            resultado_proceso = JSON.stringify(respuesta);
        },
        error: function (xhr, textStatus, errorThrown) {
            div_spinner.hide();
            if (xhr.abort)
                return;
            alert("Status: " + textStatus + ".\nError: " + errorThrown);
            activarBotones()
        }
    });
}

function validarDatosRips(datos) {
    request = $.ajax({
        url: '/validar-datos-rips/',
        type: 'POST',
        dataType: 'json',
        headers: {
            "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
        },
        data: datos,
        cache: false,
        processData: false,
        contentType: false,
        beforeSend: function (jqXHR, settings) {
            ajaxPool.push(jqXHR);
        },
        success: function (respuesta) {
            switch (respuesta.statusCode) {
                case 200:
                    if (respuesta.body && respuesta.body.length === 2) {
                        $("#spinner-mensaje").text("3. Guardando datos del RIPS...");
                        guardarRipsDB(respuesta.datos_extra)
                    } else {
                        errorEnRips(respuesta);
                    }
                    break;
                case 400:
                    errorEnZip(respuesta);
                    break;
                case 500:
                    errorEnZip(respuesta);
                    break;
                default:
                    errorInterno(respuesta);
                    break;
            }
            if (respuesta.statusCode === 200){
                delete respuesta['datos_extra'];
            }
            resultado_proceso = JSON.stringify(respuesta);
        },
        error: function (xhr, textStatus, errorThrown) {
            div_spinner.hide();
            if (xhr.abort)
                return;
            alert("Status: " + textStatus + ".\nError: " + errorThrown);
        },


    });
}

function guardarRipsDB(datos) {
    btn_cancelar.hide();
    request = $.ajax({
        url: '/guardar-datos-rips/',
        type: 'POST',
        headers: {
            "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
        },
        data: datos,
        cache: false,
        processData: false,
        contentType: false,
        beforeSend: function (jqXHR) {
            ajaxPool.push(jqXHR);
        },
        success: function (respuesta) {
            div_spinner.hide();
            div_resultado.show();
            switch (respuesta.statusCode) {
                case 200:
                    if (respuesta.body) {
                        $("#resultado-mensaje").text(respuesta.mensaje);
                        var arrayBuffer = convertirArchivoEnArrayBuffer(respuesta.pdf);
                        descargarArchivo(respuesta.nombrePdf, " application/pdf", arrayBuffer);
                    } else {
                        errorEnRips(respuesta);
                    }
                    break;
                case 400:
                    errorEnZip(respuesta);
                    break;
                case 500:
                    errorEnZip(respuesta);
                    break;
                default:
                    errorInterno(respuesta);
                    break;
            }
            activarBotones();
            resultado_proceso = JSON.stringify(respuesta);
        },
        error: function (xhr, textStatus, errorThrown) {
            div_spinner.hide();
            if (xhr.abort)
                return;
            alert("Status: " + textStatus + ".\nError: " + errorThrown);
            activarBotones();

        },
    });
}

function errorEnRips(respuesta) {
    $("#resultado-mensaje").text("RIPS inválido, por favor corregir los errores presentes en el archivo.");
    mostrarTextosError();
    var arrayBuffer = convertirArchivoEnArrayBuffer(respuesta.body);
    descargarArchivo(respuesta.error,
        " application/zip, application/octet-stream, application/x-zip-compressed, multipart/x-zip",
        arrayBuffer);
}

function errorEnZip(respuesta) {
    $("#resultado-mensaje").text(respuesta.mensaje);
    mostrarTextosError();
}

function errorInterno(respuesta) {
    div_spinner.hide();
    div_resultado.hide();
    activarBotones();
    alert("Status: " + respuesta.statusCode + ".\nError: " + respuesta.mensaje);
}

function mostrarTextosError() {
    activarBotones();
    div_spinner.hide();
    div_resultado.show();
}

function activarBotones() {
    btn_cancelar.hide();
    btn_validar.prop('disabled', false);
    btn_cancelar.prop('disabled', false);
}

function convertirArchivoEnArrayBuffer(respuesta) {
    var binaryString = window.atob(respuesta);
    var binaryLen = binaryString.length;
    var arrayBuffer = new Uint8Array(binaryLen);
    for (var i = 0; i < binaryLen; i++) {
        arrayBuffer[i] = binaryString.charCodeAt(i);
    }
    return arrayBuffer;
}

function descargarArchivo(nombre, mime_type, arrayBuffer) {
    var blob = new Blob([arrayBuffer], {type: mime_type});
    if (window.navigator.msSaveOrOpenBlob) {
        window.navigator.msSaveBlob(blob, nombre);
    } else {
        var elem = window.document.createElement('a');
        elem.href = window.URL.createObjectURL(blob);
        elem.download = nombre;
        document.body.appendChild(elem);
        elem.click();
        document.body.removeChild(elem);
    }
}


