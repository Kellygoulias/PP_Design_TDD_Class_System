from datetime import date
class Car:

    def __init__(self):
        #_tyre_positions : dict {front left: { latest reading: , date_of_latest_reading: date}}
        # list_of_readings : List of reading instances
        self._tyre_positions = {}
        self._list_of_readings = []
        

    def add_tyre(self, tyre, position):
        # Parameters:
        #   tyre : Tyre instance
        #   position: string eg: "front-left"
        # Side-effects:
        #   Adds the track to the tracks property of the self object
        self._tyre_positions[position] = {"pressure": tyre.pressure, "tread_depth": tyre.tread_depth, "date": date.today()}

    def record_reading(self, reading):
        # Parameters:
        #   reading instance
        # Returns:
        #   none
        pass # No code here yet

    def record_summary(self):
        return self._list_of_readings

    def at_a_glance(self):
        return self._tyre_positions