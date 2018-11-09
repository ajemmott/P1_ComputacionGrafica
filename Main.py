
import Point as p
import Plotter
import Line as ln
import Radius as r
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
    Plotter.plt.plot(output.x_list, output.y_list, 'bs', markersize=11)
    Plotter.plt.axis(line.get_dimensions())
    Plotter.plt.xticks(output.x_list)
    Plotter.plt.yticks(output.y_list)
    Plotter.plt.grid(True)
    Plotter.plt.show()


def get_ellipse_plot():
    x_radius = int(input('Introduzca el valor del radio en x'))
    y_radius = int(input('Introduzca el valor del radio en y'))
    center_x = int(input('Introduzca el valor en x del centro'))
    center_y = int(input('Introduzca el valor en y del centro'))

    shape = r.Ellipse(radius_x=x_radius, radius_y=y_radius, center=(center_x, center_y), is_circle=False)
    output = Plotter.Plot(shape.get_quarter(), ellipse_tag='True')
    ratio = shape.radius_x if shape.radius_x > shape.radius_y else shape.radius_y
    Plotter.plt.plot(output.x_list, output.y_list, 'bs',
                     markersize=ratio)
    Plotter.plt.axis(shape.get_dimensions())
    Plotter.plt.xticks(output.x_list)
    Plotter.plt.yticks(output.y_list)
    Plotter.plt.grid(True)
    Plotter.plt.show()


options = {
    '1': get_line_plot,
    '2': get_ellipse_plot,
    '3': intro
}


in_use = True
intro()

while in_use:
    print('Seleccione alguna de las siguientes opciones')
    print('(1). Generar Línea a partir de dos puntos')
    print('(2). Generar elipse')
    print('(3). Ver presentación')
    print('(4). Salir')

    opt = str(input())

    if opt == '4':
        in_use = False
    else:
        call_func(opt)
