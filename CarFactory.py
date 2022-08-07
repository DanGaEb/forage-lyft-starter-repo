from battery import NubbinBattery, SpindlerBattery
from engines import CapuletEngine, SternmanEngine, WilloughbyEngine
from tyres import OctoprimeTyres, CarriganTyres
from car import Car


def create_calliope(current_date, last_service_date, current_mileage,
                    last_service_mileage, tyres):  # Capulet, Spindler:
    return Car(CapuletEngine.CapuletEngine(last_service_mileage, current_mileage),
               SpindlerBattery.SpindlerBattery(last_service_date, current_date), OctoprimeTyres.OctoprimeTyres(tyres))


def create_glissade(current_date, last_service_date, current_mileage,
                    last_service_mileage, tyres):  # Willoughby, Spindler
    return Car(WilloughbyEngine.WilloughbyEngine(last_service_mileage, current_mileage),
               SpindlerBattery.SpindlerBattery(last_service_date, current_date), CarriganTyres.CarriganTyres(tyres))


def create_palindrome(current_date, last_service_date, warning_light_on, tyres):  # Sternman, Spindler
    return Car(SternmanEngine.SternmanEngine(warning_light_on),
               SpindlerBattery.SpindlerBattery(last_service_date, current_date), CarriganTyres.CarriganTyres(tyres))


def create_rorschach(current_date, last_service_date, current_mileage,
                     last_service_mileage, tyres):  # Willoughby, Nubbin
    return Car(WilloughbyEngine.WilloughbyEngine(last_service_mileage, current_mileage),
               NubbinBattery.NubbinBattery(last_service_date, current_date), CarriganTyres.CarriganTyres(tyres))


def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tyres):  # Capulet, Nubbin
    return Car(CapuletEngine.CapuletEngine(last_service_mileage, current_mileage),
               NubbinBattery.NubbinBattery(last_service_date, current_date), CarriganTyres.CarriganTyres(tyres))
