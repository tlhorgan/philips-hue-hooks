from philips_hue_hooks.action.action import Action


class PrintAction(Action):
    def invoke(self, sensor_id, new_state):
        print(f'Sensor {sensor_id} => {new_state}')
