from enum import Enum

class Theme:
    def __init__(self, name, gravity, text_color):
        self.name = name
        self.gravity = gravity
        self.text_color = text_color
    
    def get_current(self):
        if self.name == "Earth":
            return Planet.EARTH.value
        elif self.name == "Moon":
            return Planet.MOON.value
        else: return Planet.MARS.value

class Planet(Enum):
    EARTH = 0
    MOON = 1
    MARS = 2
