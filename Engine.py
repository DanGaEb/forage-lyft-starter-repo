from abc import abstractmethod


class Engine:
    def __init__(self, arg1, arg2):
        if arg2 == -1:
            self.warning_light_on = arg1
        else:
            self.last_service_mileage = arg1
            self.current_mileage = arg2

    @abstractmethod
    def needs_service(self):
        pass
