# car_model.py

from engine import Engine
from interfaces.serviceable import Serviceable

class CarModel:
    def __init__(self, engine):
        self.engine = engine

    def needs_service(self):
        return self.engine.needs_service()
