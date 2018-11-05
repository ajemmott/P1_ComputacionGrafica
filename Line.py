import Point


class Line:

    def __init__(self, start_point, end_point):
        if start_point.x < end_point.x:
            self.start_point = start_point
            self.end_point = end_point
            self.y_len = int(self.end_point.y - self.start_point.y)
            self.x_len = int(self.end_point.x - self.start_point.x)
            self.slope = float(self.y_len) / float(self.x_len)
        elif start_point.x > end_point.x:
            self.start_point = end_point
            self.end_point = start_point
            self.y_len = int(self.end_point.y - self.start_point.y)
            self.x_len = int(self.end_point.x - self.start_point.x)
            self.slope = float(self.y_len) / float(self.x_len)
        else:
            self.start_point = start_point
            self.end_point = end_point
            self.y_len = int(end_point.y - start_point.y)
            self.x_len = 0
            self.slope = None
        self.name = self.start_point.name + self.end_point.name

    def get_digital_discretion(self):
        x_k = None
        y_k = None
        digital_difference_analysis = []

        if self.slope is None:
            for k in range(abs(self.y_len)+1):
                if k == 0:
                    digital_difference_analysis.append(Point.Point(self.start_point.x, self.start_point.y, str(k)))
                    x_k = digital_difference_analysis[k].x
                    y_k = float(digital_difference_analysis[k].y)
                    continue
                digital_difference_analysis.append(Point.Point(x_k, y_k + 1, str(k)))
                x_k = digital_difference_analysis[k].x
                y_k = float(digital_difference_analysis[k].y)

        elif -1 <= self.slope <= 1:
            for k in range(self.x_len+1):
                if k == 0:
                    digital_difference_analysis.append(Point.Point(self.start_point.x, self.start_point.y, str(k)))
                    x_k = digital_difference_analysis[k].x
                    y_k = float(digital_difference_analysis[k].y)
                    continue
                digital_difference_analysis.append(Point.Point(x_k + 1, y_k + self.slope, str(k)))
                x_k = digital_difference_analysis[k].x
                y_k = float(digital_difference_analysis[k].y)

        elif self.slope > 1:
            for k in range(self.y_len+1):
                if k == 0:
                    digital_difference_analysis.append(Point.Point(self.start_point.x, self.start_point.y, str(k)))
                    x_k = digital_difference_analysis[k].x
                    y_k = float(digital_difference_analysis[k].y)
                    continue
                digital_difference_analysis.append(Point.Point(x_k + 1/self.slope, y_k + 1, str(k)))
                x_k = digital_difference_analysis[k].x
                y_k = float(digital_difference_analysis[k].y)

        elif self.slope < -1:
            for k in range(abs(self.y_len)+1):
                if k == 0:
                    digital_difference_analysis.append(Point.Point(self.start_point.x, self.start_point.y, str(k)))
                    x_k = digital_difference_analysis[k].x
                    y_k = float(digital_difference_analysis[k].y)
                    continue
                digital_difference_analysis.append(Point.Point(x_k + 1/abs(self.slope), y_k - 1, str(k)))
                x_k = digital_difference_analysis[k].x
                y_k = float(digital_difference_analysis[k].y)
        return digital_difference_analysis


AB = Line(Point.a, Point.b)
print(AB.start_point.x, AB.end_point.y, AB.slope)
point_array = AB.get_digital_discretion()
for point in point_array:
    print(point)
