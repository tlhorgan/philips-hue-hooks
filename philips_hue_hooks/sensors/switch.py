from enum import unique, Enum

from philips_hue_hooks.sensors.sensor import Sensor


class Switch(Sensor):
    def __init__(self, sensor_id):
        super().__init__(sensor_id)
        self.state = None

    def get_type(self):
        return 'switch'

    def update(self, json):
        state_from_json = json['state']['buttonevent']
        new_state = SwitchState(int(str(state_from_json)[0]))

        if self.state != new_state:
            self.state = new_state
            return new_state

        return None


@unique
class SwitchState(Enum):
    ON = 1
    BRIGHTNESS_UP = 2
    BRIGHTNESS_DOWN = 3
    OFF = 4
