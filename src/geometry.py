# Python program to implement Cohen Sutherland algorithm for line clipping.
# Adapted from: https://www.geeksforgeeks.org/line-clipping-set-1-cohen-sutherland-algorithm/

# Defining x_max,y_max and x_min,y_min for rectangle
# Since diagonal points are enough to define a rectangle
# x_max = 10.0
# y_max = 8.0
# x_min = 4.0
# y_min = 4.0

# Defining region codes
INSIDE = 0  # 0000
LEFT = 1  # 0001
RIGHT = 2  # 0010
BOTTOM = 4  # 0100
TOP = 8  # 1000


class Geometry:
    __instance = None

    @staticmethod
    def get_instance():
        if Geometry.__instance is None:
            Geometry(0, 0, 0, 0)
        return Geometry.__instance

    def set_pos(self, pos):
        self.x_min = pos[0][0]
        self.y_min = pos[0][1]
        self.x_max = pos[1][0]
        self.y_max = pos[1][1]

    def __init__(self, x_max, y_max, x_min, y_min):
        if Geometry.__instance is not None:
            raise Exception("This class is a singleton.")
        else:
            self.x_max = x_max
            self.y_max = y_max
            self.x_min = x_min
            self.y_min = y_min
            Geometry.__instance = self

    # Function to compute region code for a point(x,y)
    def computeCode(self, x, y):
        code = INSIDE
        if x < self.x_min:  # to the left of rectangle
            code |= LEFT
        elif x > self.x_max:  # to the right of rectangle
            code |= RIGHT
        if y < self.y_min:  # below the rectangle
            code |= BOTTOM
        elif y > self.y_max:  # above the rectangle
            code |= TOP
        return code

    # Implementing Cohen-Sutherland algorithm
    # Clipping a line from P1 = (x1, y1) to P2 = (x2, y2)
    def cohenSutherlandClip(self, x1, y1, x2, y2):
        # Compute region codes for P1, P2
        code1 = self.computeCode(x1, y1)
        code2 = self.computeCode(x2, y2)
        accept = False
        while True:
            # If both endpoints lie within rectangle
            if code1 == 0 and code2 == 0:
                accept = True
                break
            # If both endpoints are outside rectangle
            elif (code1 & code2) != 0:
                break
            # Some segment lies within the rectangle
            else:
                # Line Needs clipping
                # At least one of the points is outside,
                # select it
                x = 1.0
                y = 1.0
                if code1 != 0:
                    code_out = code1
                else:
                    code_out = code2
                    # Find intersection point
                # using formulas y = y1 + slope * (x - x1),
                # x = x1 + (1 / slope) * (y - y1)
                if code_out & TOP:
                    # point is above the clip rectangle
                    x = x1 + (x2 - x1) * \
                        (self.y_max - y1) / (y2 - y1)
                    y = self.y_max
                elif code_out & BOTTOM:
                    # point is below the clip rectangle
                    x = x1 + (x2 - x1) * \
                        (self.y_min - y1) / (y2 - y1)
                    y = self.y_min
                elif code_out & RIGHT:
                    # point is to the right of the clip rectangle
                    y = y1 + (y2 - y1) * \
                        (self.x_max - x1) / (x2 - x1)
                    x = self.x_max
                elif code_out & LEFT:
                    # point is to the left of the clip rectangle
                    y = y1 + (y2 - y1) * \
                        (self.x_min - x1) / (x2 - x1)
                    x = self.x_min
                    # Now intersection point x,y is found
                # We replace point outside clipping rectangle
                # by intersection point
                if code_out == code1:
                    x1 = x
                    y1 = y
                    code1 = self.computeCode(x1, y1)
                else:
                    x2 = x
                    y2 = y
                    code2 = self.computeCode(x2, y2)
        if accept:
            return True
        else:
            return False


# # First Line segment
# # P11 = (5, 5), P12 = (7, 7)
# cohenSutherlandClip(5, 5, 7, 7)
#
# # Second Line segment
# # P21 = (7, 9), P22 = (11, 4)
# cohenSutherlandClip(7, 9, 11, 4)
#
# # Third Line segment
# # P31 = (1, 5), P32 = (4, 1)
# cohenSutherlandClip(1, 5, 4, 1)
