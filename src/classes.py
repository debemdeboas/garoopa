import math

from src.geometry import Geometry

ranks = {'SIMPLE', 'NORMAL', 'LUX'}

payment_methods = {'MONEY', 'DEBIT', 'CREDIT'}


class Vehicle:
    def __init__(self, lic_plate, make, color, car_type):
        self.lic_plate = lic_plate
        self.make = make
        self.color = color
        self.car_type = car_type


class SimpleCar(Vehicle):
    def __init__(self, lic_plate, make, color):
        super().__init__(lic_plate, make, color, 'SIMPLE')


class NormalCar(Vehicle):
    def __init__(self, lic_plate, make, color, answers):
        super().__init__(lic_plate, make, color, 'NORMAL')
        self.answers = answers


class LuxCar(Vehicle):
    def __init__(self, lic_plate, make, color, answers, big_trunk):
        super().__init__(lic_plate, make, color, 'LUX')
        self.answers = answers
        self.big_trunk = big_trunk


class VehicleFactory:
    @staticmethod
    def create_vehicle(self, car_type, car, answers=False, big_trunk=False):
        if car_type == 'SIMPLE':
            return SimpleCar(car.lic_plate, car.make, car.color)
        elif car_type == 'NORMAL':
            return NormalCar(car.lic_plate, car.make, car.color, answers)
        elif car_type == 'LUX':
            return LuxCar(car.lic_plate, car.make, car.color, answers, big_trunk)


class Member:
    def __init__(self, cpf, name):
        self.cpf = cpf
        self.name = name
        self.evals = []
        self.stars = 0

    def add_eval(self, grade):
        self.evals.append(grade)
        self.stars = math.ceil(sum(self.evals) / len(self.evals))


class Driver(Member):
    def __init__(self, cpf, name, car, payment_method):
        super().__init__(cpf, name)
        self.car = car
        self.payment_method = payment_method
        self.rank = car.car_type


class Passenger(Member):
    def __init__(self, cpf, name):
        super().__init__(cpf, name)


class Neighborhood:
    def __init__(self, name, base_cost, bottom_left_x, bottom_left_y, top_right_x, top_right_y):
        self.name = name
        self.base_cost = base_cost
        self.bottom_left_x = bottom_left_x
        self.bottom_left_y = bottom_left_y
        self.top_right_x = top_right_x
        self.top_right_y = top_right_y
        self.center_point = math.ceil(abs(top_right_x - bottom_left_x) / 2), math.ceil(
            abs(bottom_left_y - top_right_y) / 2)

    def pos(self):
        return (self.bottom_left_x, self.bottom_left_y), (self.top_right_x, self.top_right_y)


class City:
    def __init__(self, name, neighborhoods):
        self.name = name
        self.neighborhoods = neighborhoods  # List


class Route:
    def __init__(self, city, origin, destiny):
        self.city = city  # City
        self.origin = origin  # Neighborhood
        self.destiny = destiny  # Neighborhood


class Trip:
    def __init__(self, trip_id, time, route):
        self.trip_id = trip_id
        self.datetime = time
        self.route = route

    def trip_cost(self):
        g = Geometry.get_instance()
        trip_cost = 0
        i = 0
        for n in self.route.city.neighborhoods:
            g.set_pos(n.pos())
            if g.cohenSutherlandClip(self.route.origin.center_point[0], self.route.origin.center_point[1],
                                     self.route.destiny.center_point[0], self.route.destiny.center_point[1]):
                trip_cost += n.base_cost
                i += 1
                print(self.route.origin.name, self.route.origin.center_point[0], self.route.origin.center_point[1],
                      self.route.destiny.name, self.route.destiny.center_point[0], self.route.destiny.center_point[1])
                print(n.name)
        return trip_cost, i
