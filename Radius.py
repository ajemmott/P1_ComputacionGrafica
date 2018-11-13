import Point as p


class Ellipse:

    def __init__(self, **kwargs):

        self.radius_x = kwargs['radius_x']
        self.radius_y = kwargs['radius_y']
        self.offset_x = kwargs['center'][0]
        self.offset_y = kwargs['center'][1]

    def get_quarter(self):
        k = 0
        y_k = self.radius_y
        x_k = 0
        p_k = self.radius_y**2 - (self.radius_x**2)*self.radius_y + (self.radius_x**2)/4
        middle_point_ellipse = [p.Point(0, self.radius_y, str(k))]
        k = 1

        while 2*(self.radius_y**2)*x_k <= 2*(self.radius_x**2)*y_k:
            new_values = self.get_decision_parameter(p_k, x_k, y_k, self.radius_x, self.radius_y)
            p_k = new_values[2]
            x_k = new_values[0]
            y_k = new_values[1]
            k += 1
            middle_point_ellipse.append(p.Point(new_values[0], new_values[1], str(k)))

        p_k = (self.radius_y**2)*(x_k + 0.5)**2 + (self.radius_x**2)*(y_k-1)**2 - (self.radius_x**2)*(self.radius_y**2)

        while (self.radius_x, 0) != (x_k, y_k):
            new_values = self.get_region2_parameter(p_k, x_k, y_k, self.radius_x, self.radius_y)
            p_k = new_values[2]
            x_k = new_values[0]
            y_k = new_values[1]
            k += 1
            middle_point_ellipse.append(p.Point(new_values[0], new_values[1], str(k)))

        middle_point_ellipse.append(p.Point(x_k, y_k, str(k)))

        return middle_point_ellipse


    @staticmethod
    def get_decision_parameter(old_p, x_k, y_k, rx, ry):
        if old_p < 0:
            new_x = x_k + 1
            new_y = y_k
            p_k = old_p + 2*(ry**2)*new_x + ry**2
        else:
            new_x = x_k + 1
            new_y = y_k - 1
            p_k = old_p + 2*(ry**2)*new_x - 2*(rx**2)*new_y + (ry**2)
        return [new_x, new_y, p_k]

    @staticmethod
    def get_region2_parameter(old_p, x_k, y_k, rx, ry):
        if old_p > 0:
            new_x = x_k
            new_y = y_k - 1
            p_k = old_p - 2 * (rx ** 2) * new_y + rx ** 2
        else:
            new_x = x_k + 1
            new_y = y_k - 1
            p_k = old_p + 2 * (ry ** 2) * new_x - 2 * (rx ** 2) * new_y + (rx ** 2)
        return [new_x, new_y, p_k]

    def get_dimensions(self):
        if self.radius_y+self.offset_y > self.radius_x+self.offset_x:
            return[-self.radius_y-self.offset_y -2,
                   self.radius_y+self.offset_y + 2,
                   -self.radius_y-self.offset_y -2,
                   self.radius_y+self.offset_y+2]
        else:
            return [-self.radius_x- self.offset_x-2,
                    self.radius_x+ self.offset_x+2,
                    -self.radius_x - self.offset_x-2,
                    self.radius_x + self.offset_x+2]


#e = Ellipse(radius_x=6, radius_y=8, center=(0, 0), is_circle=False)
#l = e.get_quarter()

#for point in l:
#    print(point.x, point.y)












