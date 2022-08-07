from abc import abstractmethod

class Engine:
    def __init__(self, last_service_mileage, current_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def __init__(self, warning_light_on):
        self.warning_light_on = warning_light_on

    @abstractmethod
    def needs_service(self):
        pass
