

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

    def merge_entities(self):
        try:
            for entity in list(self._primary_skill_dict.keys()):
                self._merge_dict[entity] = {}
                for value in self._primary_skill_dict[entity]:
                    if self._primary_skill_dict[entity][value] and self._secondary_skill_dict[entity][value]:
                        self._merge_dict[entity][value] = list(set(self._primary_skill_dict[entity][value] + 
                                                                   self._secondary_skill_dict[entity][value]))
                    else:
                        self._merge_dict[entity][value] = self._primary_skill_dict[entity][value]
            self._logger.log_merge("entities_merge", self._merge_dict)
            return self._merge_dict
        except Exception as e:
            self._logger.log(str(e))
            print(e)
            raise

    def diff_entities(self):
        try:
            for entity in list(self._primary_skill_dict.keys()):
                self._diff_dict[entity] = {}
                for value in self._primary_skill_dict[entity]:
                    if self._primary_skill_dict[entity] and self._secondary_skill_dict[entity]:
                        if self._primary_skill_dict[entity][value] and self._secondary_skill_dict[entity][value]:
                            self._diff_dict[entity][value] = list(set(self._primary_skill_dict[entity][value]).
                                                                  difference(self._secondary_skill_dict[entity][value]))
                        else:
                            self._diff_dict[entity][value] = self._primary_skill_dict[entity][value]
                    elif self._primary_skill_dict[entity] and not(self._secondary_skill_dict[entity]):
                        if self._primary_skill_dict[entity][value]:
                            self._diff_dict[entity][value] = self._primary_skill_dict[entity][value]
                        else:
                            self._diff_dict[entity] = self._primary_skill_dict[entity]
                    else:
                        raise                    
            self._logger.log_merge("entities_diff", self._diff_dict)
            return self._diff_dict
        except Exception as e:
            self._logger.log(str(e))
            print(e)
            raise
