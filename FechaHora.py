class FechaHora:
    __dia = 0
    __mes = 0
    __ano = 0
    __hora = 0
    __minutos = 0
    __segundos = 0

    def __init__(self, dia=1, mes=1, ano=2020, hora=0, minutos=0, segundos=0):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        self.__hora = hora
        self.__minutos = minutos
        self.__segundos = segundos

    def Mostrar(self):
        print(
            f"FECHA:\n{self.__dia}/{self.__mes}/{self.__ano}\nHORA:\n{self.__hora}:{self.__minutos}:{self.__segundos}")

    def PonerEnHora(self, h=0, m=0, s=0):
        self.__hora = h
        self.__minutos = m
        self.__segundos = s

    def AdelantarHora(self, h=0, m=0, s=0):

        self.__hora += h
        self.__minutos += m
        self.__segundos += s

        if self.__segundos >= 60:
            self.__minutos += 1
            self.__segundos -= 60

        if self.__minutos >= 60:
            self.__hora += 1
            self.__minutos -= 60

        if self.__hora >= 24:
            self.__dia += 1
            self.__hora -= 0

        if self.__mes > 12:
            x = self.__mes // 12 #Divide la cantidad de meses en los años que debe sumar
            self.__ano += x
            self.__mes -= 12

        # Meses con 30 días

        if self.__mes == 4 or self.__mes == 6 or self.__mes == 9 or self.__mes == 11:
            if self.__dia >= 30:
                self.__mes += 1
                self.__dia -= 30

        # Meses con 31 días

        if self.__mes == 1 or self.__mes == 2 or self.__mes == 3 or \
                self.__mes == 5 or self.__mes == 7 or self.__mes == 8 or \
                self.__mes == 10 or self.__mes == 12:
            if self.__dia >= 31:
                self.__mes += 1
                self.__dia -= 31



        if self.__mes == 12:
            if self.__dia >= 31:
                self.__mes -= 12
                self.__dia -= 31
                self.__ano += 1

        # Año Bisiesto

        anobis = False
        if self.__ano % 4 == 0 and self.__ano % 100 == 0 and self.__ano % 400 == 0:
            anobis = True

        if self.__mes == 2:
            if anobis == True:
                if self.__dia >= 29:
                    self.__mes += 1
                    self.__dia -= 29

            else:
                if self.__dia >= 28:
                    self.__mes += 1
                    self.__dia -= 28

    def __add__(self, x):
        return FechaHora(self.__dia + x.__dia, self.__mes + x.__mes, self.__ano + x.__ano,
                         self.__hora + x.__hora, self.__minutos + x.__minutos, self.__segundos + x.__segundos)

    def __sub__(self, x):
        if self.__ano - x.__ano >= 0:
            return FechaHora(self.__dia - x.__dia, self.__mes - x.__mes, self.__ano - x.__ano,
                         self.__hora - x.__hora, self.__minutos - x.__minutos, self.__segundos - x.__segundos)
        else:
            print("La resta no se puede realizar")

    def __gt__(self, x):
        if type(x) == FechaHora:
            ret = False
            if self.__ano > x.__ano:
                ret = True
            elif self.__mes > x.__mes:
                ret = True
            elif self.__dia > x.__dia:
                ret = True
            elif self.__hora > x.__hora:
                ret = True
            elif self.__minutos > x.__minutos:
                ret = True
            elif self.__segundos > x.__segundos:
                ret = True
            return ret
        else:
            print("No es de tipo FechaHora")
