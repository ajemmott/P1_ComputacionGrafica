import Point
import Line as l
import matplotlib.pyplot as plt
import numpy as np


class Plot:
    def __init__(self, list_data, **kwargs):
        self.x_list = []
        self.y_list = []
        for point in list_data:

            if kwargs['shape_tag'] == 'ellipse' and not None:
                self.y_list.append(int(point.y) + kwargs['offset_y'])
                self.x_list.append(int(point.x) + kwargs['offset_x'])
            else:
                self.x_list.append(int(point.x))
                self.y_list.append(int(point.y))

        if kwargs['shape_tag'] == 'ellipse' and not None:
            for point in list_data:
                self.x_list.append(-int(point.x) + kwargs['offset_x'])
                self.y_list.append(int(point.y) + kwargs['offset_y'])

            for point in list_data:
                self.x_list.append(int(point.x) + kwargs['offset_x'])
                self.y_list.append(-int(point.y) + kwargs['offset_y'])

            for point in list_data:
                self.x_list.append(-int(point.x)+ kwargs['offset_x'])
                self.y_list.append(-int(point.y)+ kwargs['offset_y'])











