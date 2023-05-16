

class Merger:
    def __init__(self, logger, primary_skill_dict, secondary_skill_dict):
        self._logger = logger
        self._primary_skill_dict = primary_skill_dict
        self._secondary_skill_dict = secondary_skill_dict
        self._merge_dict = {}
        self._diff_dict = {}

    def merge_intents(self):
        try:           
            for intent in list(self._primary_skill_dict.keys()):
                self._merge_dict[intent] = list(set(self._primary_skill_dict[intent] + 
                                                    self._secondary_skill_dict[intent]))
            self._logger.log_merge("intents_merge", self._merge_dict)
            return self._merge_dict
        except Exception as e:
            self._logger.log(str(e))
            print(e)
            raise    

    def diff_intents(self):
        try:
            for intent in list(self._primary_skill_dict.keys()):
                self._diff_dict[intent] = list(set(self._primary_skill_dict[intent]).
                                               difference(self._secondary_skill_dict[intent]))
            self._logger.log_merge("intents_diff", self._diff_dict)
            return self._diff_dict
        except Exception as e:
            self._logger.log(str(e))
            print(e)
            raise