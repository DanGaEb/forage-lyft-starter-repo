import unittest, CarFactory
from datetime import datetime


class TestOctoprime(unittest.TestCase): # Calliope has Octoprime tyres
    def test_exactly_3(self):
        today = datetime.today().date()
        car = CarFactory.create_calliope(today, today, 0, 0, [1, 1, 1, 0])
        self.assertTrue(car.needs_service())

    def test_below_3(self):
        today = datetime.today().date()
        car = CarFactory.create_calliope(today, today, 0, 0, [1, 1, 0, 0])
        self.assertFalse(car.needs_service())


class TestCarrigan(unittest.TestCase): # Glissade has Carrigan tyres
    def test_exactly_9(self):
        today = datetime.today().date()
        car = CarFactory.create_glissade(today, today, 0, 0, [.1, .7, .9, .8])
        self.assertTrue(car.needs_service())

    def test_below_9(self):
        today = datetime.today().date()
        car = CarFactory.create_glissade(today, today, 0, 0, [.3, .5, .6, .8999])
        self.assertFalse(car.needs_service())