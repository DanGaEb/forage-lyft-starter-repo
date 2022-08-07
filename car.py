from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, engine, battery):
        self.parts = [engine, battery]

    def needs_service(self):
        for part in self.parts:
            if part.needs_service():
                return True
