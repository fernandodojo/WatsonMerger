

class Intents:
    def __init__(self, logger, skill_data):
        self._logger = logger
        self._skill_data = skill_data
        self._data = {}

    def load(self):
        try:
            for i in self._skill_data['intents']:
                intent = i['intent']
                self._data[intent] = []
                for j in i['examples']:
                    example = j['text']
                    self._data[intent].append(example)
            return self._data
        except Exception as e:
            self._logger.log(str(e))
            print(e)
            raise
