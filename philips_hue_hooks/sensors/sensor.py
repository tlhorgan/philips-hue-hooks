import abc


class Sensor:
    def __init__(self, sensor_id):
        self.sensor_id = sensor_id

    def get_sensor_id(self):
        return self.sensor_id

    @abc.abstractmethod
    def get_type(self):
        pass

    @abc.abstractmethod
    def update(self, json):
        pass
