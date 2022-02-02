$(document).ready(function () {
    $("#tabla-validaciones").DataTable({
        "search": {
            "regex": false,
            "smart": false,
        },
        "language": {
            "sProcessing": "Procesando...",
            "sLengthMenu": "Mostrar _MENU_ registros",
            "sZeroRecords": "No se encontraron resultados",
            "sEmptyTable": "Ningún dato disponible en esta tabla",
            "sInfo": "Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros",
            "sInfoEmpty": "Mostrando registros del 0 al 0 de un total de 0 registros",
            "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
            "sInfoPostFix": "",
            "sSearch": "Buscar:",
            "sUrl": "",
            "sInfoThousands": ",",
            "sLoadingRecords": "Cargando...",
            "oPaginate": {
                "sFirst": "Primero",
                "sLast": "Último",
                "sNext": "Siguiente",
                "sPrevious": "Anterior"
            },
            "oAria": {
                "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
                "sSortDescending": ": Activar para ordenar la columna de manera descendente"
            }
        },
    });
    agregarTooltipBuscador();

    $("#guardar-validaciones").on('click', function (event) {
        event.preventDefault();

        $("#guardarModal").modal('hide');
        mostrarSpinnerGuardar(true);
        guardarValidaciones(event)
    });

    mostrarAlertaExito();
});

$('.custom-checkbox').click(function () {
    var checked = $('input', this).is(':checked');
    $('label', this).text(checked ? 'Activa' : 'Inactiva');
});

function guardarValidaciones() {

    var tabla = $('#tabla-validaciones').DataTable();
    var lista_validaciones = tabla.$('input[type="checkbox"]').serializeArray();

    datos = {
        nit: $("#nit").val(),
        token: $("#token").val(),
        cliente: $("#cliente").val(),
        prestador: $("#prestador").val(),
        validaciones: lista_validaciones
    };

    $.ajax({
        url: $("#guardar-validaciones-form").attr('action'),
        type: 'POST',
        headers: {
            "X-CSRFToken": $("[name=csrfmiddlewaretoken]").val()
        },
        data: JSON.stringify(datos),
        dataType: 'json',
        cache: false,
        success: function (respuesta) {
            mostrarSpinnerGuardar(false);
            if (respuesta.statusCode === 200) {
                localStorage.setItem("guardadoExitoso", "true");
                window.location = window.location
            }
            if (respuesta.statusCode === 502) {
                $('#alerta-error').fadeIn();
                window.setTimeout(function () {
                    $('#alerta-error').alert('close')
                }, 5000);
            }
        },
        error: function (xhr, textStatus, errorThrown) {
            alert("Status: " + textStatus + ".\nError: " + errorThrown);
        }
    })
}

function mostrarSpinnerGuardar(guardando) {
    var botonGuardar = $("#btn-guardar");

    botonGuardar.prop("disabled", guardando);
    if (guardando === true) {
        botonGuardar.html(
            '<span class="spinner-border spinner-border-sm"></span> Guardando...'
        );
    } else {
        botonGuardar.find("span").remove();
        botonGuardar.text("Guardar");
    }

}

function agregarTooltipBuscador() {
    $('.dataTables_filter input').attr('data-toggle', 'tooltip')
        .attr('data-placement', 'top')
        .attr('title', 'Ingrese al menos 3 letras para buscar en la tabla.')
        .tooltip();
}

function mostrarAlertaExito() {
    if (localStorage.getItem("guardadoExitoso") === "true") {
        $('#alerta-exito').fadeIn();
        localStorage.clear();
        window.setTimeout(function () {
            $('#alerta-exito').alert('close')
        }, 5000);
    }
}