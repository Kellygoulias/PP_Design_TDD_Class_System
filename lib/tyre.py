class Tyre:
    # User-facing properties:
    #   
    def __init__(self, tread_depth, pressure):
        # Parameters:
        #   Tread-depth: Float
        #   Pressure: Int
        #   Tyre_position: None
        # Side-effects:
        #   creates a tire with properties passed in
        self.tread_depth = tread_depth
        self.pressure = pressure
        
    
    # def add_reading(self, reading):
    #     pass

    # def format(self):
    #     # Returns:
    #     #   A string of the form "TITLE by ARTIST"
    #     pass # No code here yet