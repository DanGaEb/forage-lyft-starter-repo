import Tyre


class OctoprimeTyres(Tyre.Tyre):
    def __init__(self, worn):
        super().__init__(worn)

    def needs_service(self):
        return sum(self.worn) >= 3
