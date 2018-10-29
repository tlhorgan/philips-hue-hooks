from enum import Enum, unique

from philips_hue_hooks.sensors.sensor import Sensor


class MotionSensor(Sensor):
    def __init__(self, sensor_id):
        super().__init__(sensor_id)
        self.state = None

    def get_type(self):
        return 'motion_sensor'

    def update(self, json):
        state_from_json = json['state']['status']
        new_state = State(state_from_json)

        if self.state != new_state:
            self.state = new_state
            return new_state

        return None


@unique
class State(Enum):
    OFF = 0
    ON = 1
    TURNING_OFF = 2
