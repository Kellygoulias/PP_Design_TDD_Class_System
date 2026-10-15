# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a car owner
So that I can keep a record of details about my tyres
I want to keep track of the tyres individually, by their position on my car

As a car owner
So that I have the two important pieces of data for a tyre
I want to be able to record both tyre pressure and tyre tread depth

As a car owner
So that I have a history of tyre readings
I want to be able to keep a record of historical readings, when those were, as well as current readings

As a car owner
So that I can see the details of my car at a glance
I want to list the tyres' positions, latest readings and when those were


## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌────────────────────────────┐
│ MusicPlayer                │
│                            │
│ - tracks                   │
│ - add(track)               │
│ - search_by_title(keyword) │
│   => [tracks...]           │
└───────────┬────────────────┘
            │
            │ owns a list of
            ▼
┌─────────────────────────┐
│ Track(title, artist)    │
│                         │
│ - title                 │
│ - artist                │
│ - format()              │
│   => "TITLE by ARTIST"  │
└─────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Car:

    def __init__(self):
        #_tyre_positions : dict {front left: { latest reading: ,
                                                date_of_latest_reading: date,
                                                }}
        # list_of_readings : List of reading instances

    def add_tyre(self, tyre, position):
        # Parameters:
        #   tyre : Tyre instance
        #   position: string eg: "front-left"
        # Side-effects:
        #   Adds the track to the tracks property of the self object
        pass # No code here yet

    def record_reading(self, reading):
        # Parameters:
        #   reading instance
        # Returns:
        #   none
        pass # No code here yet

    def record_summary(self):
        # Parameters:
        #   none
        # Returns:
        #   A list of all the details of the tyres readings
        pass

    def at_a_glance(self):
        #params / n/a
        #Return : return tyre_positions



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
        pass # No code here yet
    
    # def add_reading(self, reading):
    #     pass

    # def format(self):
    #     # Returns:
    #     #   A string of the form "TITLE by ARTIST"
    #     pass # No code here yet

class Reading:

    def __init__(self, date, position, pressure, tread_depth):
        record_details = [
                    date: datetime,
                    tyre: Tyre instance,
                    position: string,
                    pressure: int,
                    tread_depth: float
        ]

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a car, add 1 tyre
"""
car = Car
tyre1 = Tyre(12.5, 50)
car.add(tyre1, "front-left")
# tyre1 = Tyre(12.3, 51)
# tyre1 = Tyre(12.2, 52)
# tyre1 = Tyre(12.1, 50)
assert car._tyre_positions == {"front-left": {pressure: 50, tread_depth: 12.5}}

"""
Given a car, add 4 tyre, make a reading.
"""
car = Car
tyre1 = Tyre(12.5, 50)
tyre2 = Tyre(12.5, 50)
tyre3 = Tyre(12.5, 50)
tyre4 = Tyre(12.5, 50)
car.add(tyre1, "front-left")
car.add(tyre2, "front-right")
car.add(tyre3, "back-left")
car.add(tyre4, "back-right")
reading1 = Reading("15/10/2026", tyre1)
reading2 = Reading("15/10/2026", tyre2)
reading3 = Reading("15/10/2026", tyre3)
reading4 = Reading("15/10/2026", tyre4)
car.record_reading(reading1)
car.record_reading(reading2)
car.record_reading(reading3)
car.record_reading(reading4)
assert car.list_of_readings == [reading1, reading2, reading3, reading4]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a single car instance and nothing else
At at_a_glance method returns None
"""
car = Car()
assert not car.at_a_glance()

"""
Given a single car instance and nothing else
At record_summary() method returns empty list
"""
car = Car()
assert not car.at_a_glance()
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
