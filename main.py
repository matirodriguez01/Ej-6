from FechaHora import FechaHora

if __name__ == '__main__':


    d = int(input("Ingrese Dia: "))

    mes = int(input("Ingrese Mes: "))

    a = int(input("Ingrese Año: "))

    h = int(input("Ingrese Hora: "))

    m = int(input("Ingrese Minutos: "))

    s = int(input("Ingrese Segundos: "))

    r = FechaHora()  # inicilizar día, mes, año con 1/1/2020, y hora, minutos y

    #  segundos con 0h, 0m, 0s.

    r1 = FechaHora(d, mes, a)   # inicializar con 0h 0m 0s

    r2 = FechaHora(d, mes, a, h, m, s)

    r.Mostrar()

    r1.Mostrar()

    r2.Mostrar()

    input()

    r.PonerEnHora(5)  # solamente la hora

    r.Mostrar()

    input()

    r2.PonerEnHora(13, 30)  # hora y minutos

    r2.Mostrar()

    input()

    r.PonerEnHora(14, 30, 25)  # hora, minutos y segundos

    r.Mostrar()

    input()

    r.AdelantarHora(3)  # sumar 3 horas a la hora actual

    r.Mostrar()

    input()

    r1.AdelantarHora(1, 15)  # sumar 1 hora y 15 minutos a la hora actual

    r1.Mostrar()


    h1 = FechaHora(18, 8, 2010)
    h1.AdelantarHora(5, 20, 30)
    h1.Mostrar()

    h2 = FechaHora(15, 6, 2020)
    h2.AdelantarHora(3, 30, 30)
    h2.Mostrar()

    h3 = FechaHora()
    h3 = h1 + h2
    h3.Mostrar()
    h3.AdelantarHora()
    h3.Mostrar()

    h4 = FechaHora()
    h4 = h1 - h2

    print(h1 > h2)
