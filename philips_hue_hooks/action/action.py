import abc


class Action:
    @abc.abstractmethod
    def invoke(self, sensor_id, new_state):
        pass
