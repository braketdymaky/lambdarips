from Aplicacion.Almacenamiento.almacenamiento import Almacenamiento
from Aplicacion.Consulta.consultas import Consulta
from Aplicacion.General.general import General
from Aplicacion.Implementacion.implementacion import Implementacion
from Aplicacion.Consulta.tablas import Tablas


class Ejecucion:

    def ejecutar_lambda(self, zipf, nombre_zip, codigo_prestador, codigo_cliente):
        almacenar = Almacenamiento()
        implementar = Implementacion()
        consulta = Consulta()
        general = General()
        continuar = True

        """ Obtener listas de tablas maestro en base de datos"""
        if not continuar:
            return continuar
        continuar = Tablas().obtener_ficheros()

        """ Guardar tabla principal rips - Registros Validados"""
        if not continuar:
            return continuar
        lista_archivos_af = general.generar_lista_af(zipf)

        lista_archivos_ct = general.generar_lista_ct(zipf)

        almacenar.insertar_rips(lista_archivos_ct[0][0], lista_archivos_af[0][8], nombre_zip)

        """ Obtener ID de rips previamente almacenado en base de datos"""
        if not almacenar.continuar:
            return almacenar.continuar
        rips_id = consulta.rips_id(lista_archivos_ct[0][0])

        if not consulta.continuar:
            return consulta.continuar
        """ Crear lista de registro US"""
        lista_archivos = general.generar_lista_us(zipf)

        """Reemplazar valores en US"""
        implementar.us_reemplazar(lista_archivos)

        """ Guardar tablas de US"""
        almacenar.insertar_us(lista_archivos, rips_id)

        if not almacenar.continuar:
            return almacenar.guardar_cambios()
        """Crear lista de registro AF"""
        lista_archivos = general.generar_lista_af(zipf)

        """Reemplazar valores en AF"""
        implementar.af_reemplazar(lista_archivos, rips_id)

        """ Guardar tablas de AF"""
        almacenar.insertar_af(lista_archivos)
        if not almacenar.continuar:
            return almacenar.guardar_cambios()

        """Crear lista de registro CT"""
        lista_archivos = general.generar_lista_ct(zipf)

        """Reemplazar valores en CT"""
        implementar.ct_reemplazar(lista_archivos, rips_id)

        """ Guardar tablas de CT"""
        almacenar.insertar_ct(lista_archivos, rips_id)
        if not almacenar.continuar:
            return almacenar.guardar_cambios()

        """Crear lista de registro AC"""
        lista_archivos = general.generar_lista_ac(zipf)
        if lista_archivos:
            """Reemplazar valores en AC"""
            implementar.ac_reemplazar(lista_archivos)

            """ Guardar tablas de AC"""
            almacenar.insertar_ac(lista_archivos, rips_id)
            if not almacenar.continuar:
                return almacenar.guardar_cambios()

        """Crear lista de registro AP"""
        lista_archivos = general.generar_lista_ap(zipf)
        if lista_archivos:
            """Reemplazar valores en AP"""
            implementar.ap_reemplazar(lista_archivos)

            """ Guardar tablas de AP"""
            almacenar.insertar_ap(lista_archivos, rips_id)
            if not almacenar.continuar:
                return almacenar.guardar_cambios()

        """Crear lista de registro AU"""
        lista_archivos = general.generar_lista_au(zipf)
        if lista_archivos:
            """Reemplazar valores en AU"""
            implementar.au_reemplazar(lista_archivos)

            """ Guardar tablas de AU"""
            almacenar.insertar_au(lista_archivos, rips_id)
            if not almacenar.continuar:
                return almacenar.guardar_cambios()
        """Crear lista de registro AH"""
        lista_archivos = general.generar_lista_ah(zipf)
        if lista_archivos:
            """Reemplazar valores en AH"""
            implementar.ah_reemplazar(lista_archivos)

            """ Guardar tablas de AH"""
            almacenar.insertar_ah(lista_archivos, rips_id)
            if not almacenar.continuar:
                return almacenar.guardar_cambios()

        """Crear lista de registro AN"""
        lista_archivos = general.generar_lista_an(zipf)
        if lista_archivos:
            """Reemplazar valores en AN"""
            implementar.an_reemplazar(lista_archivos)

            """ Guardar tablas de AN"""
            almacenar.insertar_an(lista_archivos, rips_id)
            if not almacenar.continuar:
                return almacenar.guardar_cambios()

        """Crear lista de registro AM"""
        lista_archivos = general.generar_lista_am(zipf)
        if lista_archivos:
            """Reemplazar valores en AM"""
            implementar.am_reemplazar(lista_archivos)

            """ Guardar tablas de AM"""
            almacenar.insertar_am(lista_archivos, rips_id)
            if not almacenar.continuar:
                return almacenar.guardar_cambios()

        """Crear lista de registro AT"""
        lista_archivos = general.generar_lista_at(zipf)
        if lista_archivos:
            """Reemplazar valores en AT"""
            implementar.at_reemplazar(lista_archivos)

            """ Guardar tablas de AT"""
            almacenar.insertar_at(lista_archivos, rips_id)
            if not almacenar.continuar:
                return almacenar.guardar_cambios()

        """Crear lista de registro AD"""
        lista_archivos = general.generar_lista_ad(zipf)
        if lista_archivos:
            """Reemplazar valores en AD"""
            implementar.ad_reemplazar(lista_archivos)

            """ Guardar tablas de AD"""
            almacenar.insertar_ad(lista_archivos, rips_id)
            if not almacenar.continuar:
                return almacenar.guardar_cambios()

        """ Guardar tablas """
        return almacenar.guardar_cambios()
