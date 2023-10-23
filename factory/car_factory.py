# factory/car_factory.py

from car_model import CarModel
from engine.parts.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery


class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(
            last_service_date, current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date)
        return CarModel(engine, battery)

    # Implement create methods for other car models
