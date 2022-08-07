import Engine


class SternmanEngine(Engine.Engine):
    def __init__(self, warning_light_on):
        super().__init__(warning_light_on, -1)

    def needs_service(self):
        return self.warning_light_on
