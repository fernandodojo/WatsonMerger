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