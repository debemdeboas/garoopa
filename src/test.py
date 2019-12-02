import unittest
from src.classes import *


class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.g = Geometry.get_instance()
        self.humaita = Neighborhood("One And Done", 15, 13, 10, 80, 3)
        self.neighborhoods_list = [Neighborhood("Moinhos de Vento", 15, 0, 0, 4, 4),
                                   Neighborhood("Menino Deus", 10, 5, 5, 6, 6),
                                   Neighborhood("Lami", 5, -5, 2, 0, 11),
                                   Neighborhood("Tres Figueiras", 17, -15, 3, -5, 10)
                                   ]
        self.c = City("Porto Alegre", self.neighborhoods_list)

        self.c1 = VehicleFactory.create_vehicle('SIMPLE', '1234ABC', 'Ford Focus', 'Blue')
        self.c2 = VehicleFactory.create_vehicle('NORMAL', '1234DCC', 'Rav4', 'Gray', True, True)
        self.c3 = VehicleFactory.create_vehicle('lux', 'IRH6Z86', 'Lexus', 'Red', False, True)
        self.car_list = [self.c1, self.c2, self.c3]

        self.driver1 = Driver(123456789, "John Doe", self.c1, ['DEBIT', 'CREDIT'])
        self.driver2 = Driver(465984488, "Joo Dee", self.c2, ['MONEY', 'CREDIT'])
        self.driver3 = Driver(684591377, "Azulon", self.c3, ['MONEY'])

    def test_route_cost(self):
        r = Route(self.c, self.neighborhoods_list[3], self.neighborhoods_list[0])
        self.assertEqual(r.route_cost(), (37, 3))

    def test_trip_cost(self):
        r = Route(self.c, self.neighborhoods_list[3], self.neighborhoods_list[0])
        t = Trip(None, self.driver1, 0, 0, r)
        self.assertEqual(t.trip_cost(), 37)

        t = Trip(None, self.driver2, 0, 0, r)
        self.assertEqual(t.trip_cost(), 40.7)

        t = Trip(None, self.driver3, 0, 0, r)
        self.assertEqual(t.trip_cost(), 43.14)

    def test_cohen_sutherland_rectangles(self):
        self.g.set_pos(((0, 0,), (10, 10)))
        self.assertTrue(g.in_rectangle(3, 3, 6, 7))  # Completely inside
        self.assertTrue(g.in_rectangle(-1, 6, 7, 12))  # Partially inside
        self.assertFalse(g.in_rectangle(-1, -1, -2, -7))  # Outside

    def test_geometry_singleton(self):
        # Try to create a new instance of the Geometry class, which is a singleton
        with self.assertRaises(Exception):
            Geometry(0, 0, 0, 0)

    def test_neighborhood_pos(self):
        self.assertEqual(self.humaita.pos(), ((13, 10), (80, 3)))

    def test_neighborhood_center_point(self):
        self.assertEqual(self.humaita.center_point, (46.5, 6.5))

    def test_vehicle_factory(self):
        self.assertTrue(isinstance(self.c1, SimpleCar))
        self.assertFalse(isinstance(self.c2, SimpleCar))
        self.assertTrue(isinstance(self.c2, NormalCar))
        self.assertTrue(isinstance(self.c3, LuxCar))

    def test_vehicle_inheritance(self):
        for c in self.car_list:
            self.assertTrue(isinstance(c, Vehicle))

    def test_member_evals(self):
        m = Member(123456, "John Appleseed")
        m.add_eval(9)
        m.add_eval(8)
        m.add_eval(6.5)
        self.assertEqual(m.stars, 8)

    def test_simple_trip_price(self):
        self.assertEqual(simple_trip_price((39, 4)), 39)

    def test_normal_trip_prince(self):
        self.assertEqual(normal_trip_price((39, 4)), 42.9)

    def test_lux_trip_price(self):
        self.assertEqual(lux_trip_price((39, 4)), 46.33)


if __name__ == '__main__':
    unittest.main()
