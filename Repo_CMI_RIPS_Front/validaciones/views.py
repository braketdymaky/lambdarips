# -*- coding: utf-8 -*-
import json
from django.shortcuts import render
from django.http import JsonResponse, Http404, HttpResponseForbidden
from validaciones.forms import ClienteForm
from validaciones.models import TripsValidaciones
from validaciones.models import TripsClientesEapb
from validaciones.models import TripsDinamismo
from django.template.context_processors import csrf
from django.db.models import Q
import cargar_archivo_rips.validacion_token as validar_token
from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def index(request):
    context = {}
    context.update(csrf(request))
    try:
        estado_token = validar_token.check(request.GET['token'], request.GET['cliente'], request.GET['prestador'])
        if estado_token['status']:
            if request.method == 'POST':

                form = ClienteForm(request.POST)

                if form.is_valid():
                    nit = form.cleaned_data['nit']
                    render_contenido = {'form': form, 'token': request.GET['token'], 'nit': None}
                    contenido = consultar_validaciones_por_cliente(nit, render_contenido)

                    return render(request, 'paginas/validaciones.html', contenido)
            form = ClienteForm()

            return render(request, 'paginas/validaciones.html', {'form': form, 'token': request.GET['token'],'cliente':request.GET['cliente'], 'prestador':request.GET['prestador']})
            return HttpResponseForbidden()
        else:
            return HttpResponseForbidden()
    except Exception as ex:
        print(ex)
        raise Http404("Página no existe")


def guardar(request):
    try:
        if request.method == 'POST':
            request_body = json.loads(request.body.decode('utf-8'))
            estado_token = validar_token.check(request_body['token'], request_body['cliente'], request_body['prestador'])

            if estado_token:
                validaciones_activas = []
                validaciones_a_ignorar = []
                codigos_validaciones = TripsValidaciones.objects.values_list('cdcodigo', flat=True)

                if request_body['validaciones']:
                    for codigo in request_body['validaciones']:
                        validaciones_activas.append(int(codigo['name']))

                validaciones_inactivas = list(set(codigos_validaciones) - set(validaciones_activas))

                for codigo in validaciones_inactivas:
                    if TripsValidaciones.objects.filter(Q(cdcodigo=codigo) & Q(sndinamico=1)):
                        validaciones_a_ignorar.append(codigo)

                if guardar_validaciones_cliente(request_body['nit'], str(validaciones_a_ignorar)[1:-1]):
                    return JsonResponse({'statusCode': 200, 'message': 'Guardado Correctamente'})
                return JsonResponse({'statusCode': 502, 'message': 'Error al intentar guardar.'})
            else:
                return HttpResponseForbidden()
    except Exception as ex:
        raise Http404("Página no existe")


def consultar_validaciones_por_cliente(nit, render_contenido):
    cliente = TripsClientesEapb.objects.filter(dsnit=nit).first()
    if cliente:
        validaciones = TripsValidaciones.objects.all()
        validaciones_nit = TripsDinamismo.objects.filter(Q(cdidcliente=cliente.cdid) & Q(snactive=1)).first()
        render_contenido['lista_validaciones'] = validaciones
        render_contenido['nit'] = nit
        if not validaciones_nit or not validaciones_nit.nmcod_metodo:
            render_contenido['nmcodigos'] = None
        else:
            nmcodigos = str(validaciones_nit.nmcod_metodo).split(',')
            nmcodigos = [int(cod) for cod in nmcodigos]
            render_contenido['nmcodigos'] = nmcodigos
    return render_contenido


def guardar_validaciones_cliente(nit, validaciones_a_ignorar):
    try:
        id_eapb = TripsClientesEapb.objects.filter(dsnit=nit).first()
        cliente = TripsDinamismo.objects.filter(Q(cdidcliente=id_eapb.cdid) & Q(snactive=1)).first()
        if cliente:
            if cliente.nmcod_metodo == validaciones_a_ignorar:
                return True
            else:
                cliente.snactive = 0
                cliente.save()
        nuevo_cliente = TripsDinamismo(cdidcliente_id=id_eapb.cdid, nmcod_metodo=validaciones_a_ignorar,
                                       snactive=1)
        nuevo_cliente.save()
        return True
    except Exception as ex:
        return False
