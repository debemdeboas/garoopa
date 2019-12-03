import math
import random

from src.geometry import Geometry

ranks = ['SIMPLE', 'NORMAL', 'LUX']

payment_methods = ['MONEY', 'DEBIT', 'CREDIT']


class Vehicle:
    def __init__(self, lic_plate, make, color, car_type='SIMPLE'):
        self.lic_plate = lic_plate
        self.make = make
        self.color = color
        self.car_type = car_type


class SimpleCar(Vehicle):
    def __init__(self, lic_plate, make, color):
        super().__init__(lic_plate, make, color)


class NormalCar(Vehicle):
    def __init__(self, lic_plate, make, color):
        super().__init__(lic_plate, make, color, 'NORMAL')


class LuxCar(Vehicle):
    def __init__(self, lic_plate, make, color, big_trunk):
        super().__init__(lic_plate, make, color, 'LUX')
        self.big_trunk = big_trunk


class VehicleFactory:
    @staticmethod
    def create_vehicle(car_type, lic_plate, make, color, big_trunk=False):
        car_type = car_type.upper()
        if car_type == 'SIMPLE':
            return VehicleFactory.create_simple_car(lic_plate, make, color)
        elif car_type == 'NORMAL':
            return VehicleFactory.create_normal_car(lic_plate, make, color)
        elif car_type == 'LUX':
            return VehicleFactory.create_lux_car(lic_plate, make, color, big_trunk)

    @staticmethod
    def create_simple_car(lic_plate, make, color):
        return SimpleCar(lic_plate, make, color)

    @staticmethod
    def create_normal_car(lic_plate, make, color):
        return NormalCar(lic_plate, make, color)

    @staticmethod
    def create_lux_car(lic_plate, make, color, big_trunk):
        return LuxCar(lic_plate, make, color, big_trunk)


class Member:
    def __init__(self, cpf, name):
        self.cpf = cpf
        self.name = name
        self.evals = []
        self.stars = 10

    def add_eval(self, grade):
        self.evals.append(grade)
        self.stars = math.ceil(sum(self.evals) / len(self.evals))


class Driver(Member):
    def __init__(self, cpf, name, car, payment_method, answers=False):
        super().__init__(cpf, name)
        self.car = car
        self.payment_method = payment_method
        self.rank = car.car_type
        self.trips = {}  # Trips dictionary of type <PassengerCPF, Trip>
        if self.rank in ['NORMAL', 'LUX']:
            self.answers = answers


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
        self.center_point = (top_right_x + bottom_left_x) / 2, (top_right_y + bottom_left_y) / 2

    def pos(self):
        return (self.bottom_left_x, self.bottom_left_y), (self.top_right_x, self.top_right_y)


class City:
    def __init__(self, name, neighborhoods):
        self.name = name
        self.neighborhoods = neighborhoods  # Neighborhood list


class Route:
    def __init__(self, city, origin, destiny):
        self.city = city  # City
        self.origin = origin  # Neighborhood
        self.destiny = destiny  # Neighborhood

    def route_cost(self):
        g = Geometry.get_instance()
        trip_cost = 0
        i = 0
        origin_x = self.origin.center_point[0]
        origin_y = self.origin.center_point[1]
        destiny_x = self.destiny.center_point[0]
        destiny_y = self.destiny.center_point[1]

        for n in self.city.neighborhoods:
            g.set_pos(n.pos())
            if g.in_rectangle(origin_x, origin_y, destiny_x, destiny_y):
                trip_cost = trip_cost + n.base_cost
                i = i + 1
        return trip_cost, i


def simple_trip_price(base_cost):
    return base_cost[0]


def normal_trip_price(base_cost):
    return round(base_cost[0] * 1.1, 2)  # Price + 110%


def lux_trip_price(base_cost):
    return round(normal_trip_price(base_cost) * (((2 * base_cost[1]) / 100) + 1), 2)


class Trip:
    def __init__(self, passenger, driver, trip_id, time, route):
        self.trip_id = trip_id
        self.datetime = time
        self.route = route
        self.passenger = passenger
        self.driver = driver

        if driver.rank == 'LUX':
            self._cost = lux_trip_price
        elif driver.rank == 'NORMAL':
            self._cost = normal_trip_price
        else:
            self._cost = simple_trip_price

    def trip_cost(self):
        route_cost = self.route.route_cost()
        return self._cost(route_cost)


def get_driver(rank, p_method, passenger, drivers, big_trunk=False):
    selected_drivers = []

    for d in drivers.values():
        if p_method in d.payment_method:
            selected_drivers.append(d)

    categorized_drivers = []

    for d in selected_drivers:
        if (d.rank == rank) or d.answers:
            if not (d.rank == 'NORMAL' and rank == 'LUX'):
                categorized_drivers.append(d)

    starred_drivers = []

    for d in categorized_drivers:
        if -2 <= d.stars - passenger.stars <= 2:
            starred_drivers.append(d)

    if big_trunk and rank == 'LUX':
        for d in starred_drivers:
            if not d.car.big_trunk:
                starred_drivers.remove(d)

    if starred_drivers:
        return random.choice(starred_drivers)
    return None


def get_neighborhood(name, neighborhoods):
    for n in neighborhoods:
        if n.name == name:
            return n
    return None
