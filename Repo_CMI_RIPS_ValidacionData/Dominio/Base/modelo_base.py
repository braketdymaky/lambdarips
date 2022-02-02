class ModeloBase:
    __instance = None
    __lista_registros = []

    @classmethod
    def obtener_instancia(cls):
        """
        obtener la instancia de la clase
        :return:
        """
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def asignar_valores(self, lista_registros):
        self.__lista_registros = lista_registros

    def obtener_lista(self):
        """
        Retorna la direccion
        :return:
        """
        return self.__lista_registros
