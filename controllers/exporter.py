import pandas as pd
import os


class Exporter:
    def __init__(self, export_directory, logger):
        self._export_directory = export_directory
        self._logger = logger

    def export_merge_intents(self, merge_dict):
        try:
            export_list = []
            for intent in list(merge_dict.keys()):
                for example in merge_dict[intent]:
                    export_list.append([intent, example])

            if not os.path.exists(self._export_directory):
                    os.makedirs(self._export_directory)

            df = pd.DataFrame(export_list)
            df.to_csv(self._export_directory + 'intents_merge.csv', index=False, header=False)
            return export_list  
        except Exception as e:
            self._logger.log(str(e))
            print(e)
            raise

    def export_diff_intents(self, diff_dict):
        try:
            export_list = []
            for intent in list(diff_dict.keys()):
                for example in diff_dict[intent]:
                    export_list.append([intent, example])

            if not os.path.exists(self._export_directory):
                os.makedirs(self._export_directory)

            df = pd.DataFrame(export_list)
            df.to_csv(self._export_directory + 'intents_diff.csv', index=False, header=False)
            return export_list  
        except Exception as e:
            self._logger.log(str(e))
            print(e)
            raise

    def export_merge_entities(self, merge_dict):
        try:
            export_list = []
            max_list = []
            for entity in list(merge_dict.keys()):
                for value in merge_dict[entity]:
                    temp_list = [entity, value]
                    for synonyms in merge_dict[entity][value]:
                        temp_list.append(synonyms)
                    max_list.append(len(temp_list))
                    export_list.append(temp_list)
            max_len = max(max_list)

            ([index.extend([""] * (max_len - len(index))) for index in export_list])

            if not os.path.exists(self._export_directory):
                os.makedirs(self._export_directory)

            df = pd.DataFrame(export_list)
            df.to_csv(self._export_directory + 'entities_merge.csv', index=False, header=False)
            return export_list  
        except Exception as e:
            self._logger.log(str(e))
            print(e)
            raise