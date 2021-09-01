from sensors import *

class BinaryMatch:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class BinaryUnit:
    def __init__(self, u_radius, sensor_field_radius, etalon, event_diameter, dx,dy):
        self.u_radius = u_radius
        self.sensor_field_radius = sensor_field_radius
        self.A_min = etalon - int(event_diameter/2)
        self.A_max = self.A_min + event_diameter
        self.dx = dx
        self.dy = dy

    def apply(self, pic, x,y):
        matches = []
        expected_x = x + self.dx
        expected_y = y + self.dy
        for r in range(0, self.u_radius + 1):
            X, Y = get_coords_for_radius(expected_x, expected_y, r)
            for i in range(len(X)):
                mean = make_measurement(pic, X[i], Y[i], self.sensor_field_radius)
                if mean >= self.A_min and mean <= self.A_max:
                    matches.append(BinaryMatch(X[i], Y[i]))
        return matches

    def apply2(self, pic, x,y):
        if len(self.apply(pic,x,y)) > 0:
            return 1
        return 0