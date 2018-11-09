import Point
import Line as l
import matplotlib.pyplot as plt
import numpy as np


class Plot:
    def __init__(self, list_data, **kwargs):
        self.x_list = []
        self.y_list = []
        for point in list_data:
            self.x_list.append(int(point.x))
            self.y_list.append(int(point.y))

        if kwargs['ellipse_tag'] == 'True' and not None:
            for point in list_data:
                self.x_list.append(-int(point.x))
                self.y_list.append(int(point.y))

            for point in list_data:
                self.x_list.append(int(point.x))
                self.y_list.append(-int(point.y))

            for point in list_data:
                self.x_list.append(-int(point.x))
                self.y_list.append(-int(point.y))











