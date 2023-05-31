

class Entities:
    def __init__(self, logger, skill_data):
        self._logger = logger
        self._skill_data = skill_data
        self._data = {}

    def load(self):
        try:
            for i in self._skill_data['entities']:
                entity = i['entity']
                self._data[entity] = {}
                for j in i['values']:
                    if j['type'] == "synonyms":
                        value = j['value']
                        self._data[entity][value] = []
                        for synonym in j["synonyms"]:
                            self._data[entity][value].append(synonym)            
            return self._data
        except Exception as e:
            self._logger.log(str(e))
            print(e)
            raise