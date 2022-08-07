import Tyre


class CarriganTyres(Tyre.Tyre):
    def __init__(self, worn):
        super().__init__(worn)

    def needs_service(self):
        return max(self.worn) >= 0.9
