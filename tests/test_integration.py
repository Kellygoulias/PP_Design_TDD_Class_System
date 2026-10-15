from lib.car import *
from lib.tyre import *
from datetime import date
"""
Given a car, add 1 tyre
"""
def test_add_tyre():
    car = Car()
    tyre1 = Tyre(12.5, 50)
    car.add_tyre(tyre1, "front-left")
    # tyre1 = Tyre(12.3, 51)
    # tyre1 = Tyre(12.2, 52)
    # tyre1 = Tyre(12.1, 50)
    assert car._tyre_positions == {"front-left": {"pressure": 50, "tread_depth": 12.5, "date": date.today()}}

# """
# Given a car, add 4 tyre, make a reading.
# """
# car = Car
# tyre1 = Tyre(12.5, 50)
# tyre2 = Tyre(12.5, 50)
# tyre3 = Tyre(12.5, 50)
# tyre4 = Tyre(12.5, 50)
# car.add(tyre1, "front-left")
# car.add(tyre2, "front-right")
# car.add(tyre3, "back-left")
# car.add(tyre4, "back-right")
# reading1 = Reading("15/10/2026", tyre1)
# reading2 = Reading("15/10/2026", tyre2)
# reading3 = Reading("15/10/2026", tyre3)
# reading4 = Reading("15/10/2026", tyre4)
# car.record_reading(reading1)
# car.record_reading(reading2)
# car.record_reading(reading3)
# car.record_reading(reading4)
# assert car.list_of_readings == [reading1, reading2, reading3, reading4]