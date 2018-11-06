
import Point as p
import Plotter
import Line as ln
import os


def intro():
    print('\nUniversidad Tecnológica de Panamá')
    print('Facultad de Ingeniería en Sistemas Computacionales')
    print('Departamento de Computación y Simulación de Sistemas')
    print('Licenciatura en Ingeniería en Sistemas y Computación')

    print('\nHerramientas de Computación Gráfica - Actividad 17')
    print('Algoritmos de Discretización')
    print('\nPresenta: Arturo Jemmott - 8-908-2064')
    print('Grupo 1IL131')

    print('\nFacilitado por: Prof. Nicolás Samaniego')

    input('\nPresione \'Enter\' para continuar...')
    os.system('cls')


def call_func(n):
    options[n]()


def get_line_plot():
    x_val = int(input('Introduzca el valor en x del primer punto'))
    y_val = int(input('Introduzca el valor en y del primer punto'))
    tag = input(f'Introduzca una etiqueta para el punto en ({x_val},{y_val}):')
    first_point = p.Point(x_val,y_val,tag)
    x_val = int(input('Introduzca el valor en x del segundo punto'))
    y_val = int(input('Introduzca el valor en y del segundo punto'))
    tag = input(f'Introduzca una etiqueta para el punto en ({x_val},{y_val}):')
    second_point = p.Point(x_val, y_val, tag)

    line = ln.Line(first_point, second_point)
    output = Plotter.Plot(ln.Line.get_digital_discretion(line))
    Plotter.plt.plot(output.x_list, output.y_list, 'bs')
    Plotter.plt.axis(line.get_dimensions())
    Plotter.plt.show()


options = {
    '1': get_line_plot,
    '2': intro
}


in_use = True
intro()

while in_use:
    print('Seleccione alguna de las siguientes opciones')
    print('(1). Generar Línea a partir de dos puntos')
    print('(2). Ver presentación')
    print('(3). Salir')

    opt = str(input())

    if opt == '3':
        in_use = False
    else:
        call_func(opt)
