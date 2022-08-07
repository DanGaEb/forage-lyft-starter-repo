from abc import abstractmethod


class Tyre:
    def __init__(self, worn):
        self.worn = worn

    @abstractmethod
    def needs_service(self):
        pass
