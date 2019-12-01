import unittest
from src.classes import *


class MyTestCase(unittest.TestCase):
    def test_trip_cost(self):
        neighborhoods_list = [Neighborhood("Moinhos de Vento", 15, 0, 0, 4, 4), Neighborhood("Menino Deus", 10, 5, 5, 6, 6)]
        c = City("Porto Alegre", neighborhoods_list)
        r = Route(c, neighborhoods_list[1], neighborhoods_list[0])
        t = Trip(0, 0, r)
        print(t.trip_cost())
        # self.assertEqual(t.trip_cost(), )


if __name__ == '__main__':
    unittest.main()
