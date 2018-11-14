import Line as l
import Point as p
import os


class Polygon:
    def __init__(self):
        vertex_amount = int(input('\n¿Cuantos vertices tiene el polígono a rellenar?\n\tcantidad de vertices = '))
        self.vertex_data = []
        self.TA = None
        self.TAA = None

        print('\n\tLlene los datos de cada vertice en el sentido de las manecillas del reloj...\n')
        x_val = int(input(f'\tIntroduzca el valor en x del punto 1:\n\tx = '))
        y_val = int(input(f'\tIntroduzca el valor en y del punto 1:\n\ty = '))
        self.min_y = y_val
        self.max_y = y_val

        current_vertex = p.Point(x_val, y_val, 'p0')
        first_vertex = current_vertex

        for vertex in range(1, vertex_amount):

            os.system('cls')

            print(f'\n\t¿Ingrese los dato del punto adyacente a {current_vertex}...\n')
            x_val = int(input(f'\tIntroduzca el valor en x del punto {vertex}:\n\tx = '))
            y_val = int(input(f'\tIntroduzca el valor en y del punto {vertex}:\n\ty = '))
            self.min_y = y_val if y_val < self.min_y else self.min_y
            self.max_y = y_val if y_val > self.max_y else self.max_y
            next_vertex = p.Point(x_val, y_val, 'p'+str(vertex))
            current_vertex.add_next_link(next_vertex)
            self.vertex_data.append(current_vertex)
            current_vertex = next_vertex

        self.vertex_data.append(current_vertex)
        current_vertex.next_link = first_vertex
        first_vertex.previous_link = current_vertex

    def build_TA(self):
        self.TA = []
        edge_list = [(0,0,0)]

        # for edge in edge_list:
        #     for new_vertex in self.vertex_data:
        #         new_edge = Edge(new_vertex, new_vertex.next_link)
        #         if Edge.edge_is_new(edge, new_edge):
        #             edge_list.append(new_edge.set)
        #             continue

        for new_vertex in self.vertex_data:
            new_edge = Edge(new_vertex.previous_link, new_vertex)
            if Edge.edge_is_new(edge_list, new_edge):
                edge_list.append(new_edge.set)

        print(edge_list)



class Edge:
    def __init__(self, vertex_a, vertex_b):
        self.edge = l.Line(vertex_a, vertex_b)
        if self.edge.slope is not None:
            if self.edge.slope != 0:
                self.edge_slope = 1/self.edge.slope
            else:
                self.edge_slope = 0
        else:
            self.edge_slope = 0

        if vertex_a.y > vertex_b.y:
            self.y_max = vertex_a.y
            self.x_min = vertex_b.x
        elif vertex_b.y == vertex_a.x:
            self.y_max = vertex_a.y
            self.x_min = vertex_b.x if vertex_b.x < vertex_a.x else vertex_a.x
        else:
            self.y_max = vertex_b.y
            self.x_min = vertex_a.x

        self.set = self.y_max, self.x_min, self.edge_slope

    @staticmethod
    def edge_is_new(item_list, edge):
        for item in item_list:
            return True if item != edge.set else False


poly = Polygon()
for vertex in poly.vertex_data:
    print(vertex.previous_link, vertex, vertex.next_link)

poly.build_TA()
print(poly.TA)

