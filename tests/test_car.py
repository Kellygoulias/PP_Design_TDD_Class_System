from lib.car import *
"""
Given a single car instance and nothing else
At at_a_glance method returns None
"""
def test_no_tyres_at_a_glance():
    car = Car()
    assert car.at_a_glance() == {}

"""
Given a single car instance and nothing else
At record_summary() method returns empty list
"""
def test_no_tyres_record_summary():
    car = Car()
    assert car.record_summary() == []