import Battery

class SpindlerBattery(Battery.Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date, current_date)

    def needs_service(self):
        return self.last_service_date.replace(year=self.last_service_date.year + 3) < self.current_date
