from os import walk, path, stat
from datetime import datetime
import json
from jsonschema import validate, ValidationError, SchemaError


class File:
    def __init__(self, logger, schema):
        self._logger = logger
        self._schema = schema

    def find_latest_skill(self, files_path):
        try:
            files_path_list = []
            file_time_list = []

            for root, dirs, files in walk(files_path, topdown=False):
                for file in files:
                    file_path = path.join(root, file)
                    files_path_list.append(file_path)
                    file_time = datetime.fromtimestamp(stat(file_path).st_mtime)
                    file_time_list.append(file_time)
            latest_timestamp_index = file_time_list.index(max(file_time_list))
            
            path_latest_file = files_path_list[latest_timestamp_index]
            file = open(path_latest_file, "r")
            data = json.loads(file.read())

            return data
        except Exception as e:
            self._logger.log(str(e))
            print(e)
            raise

    def validate_skill(self, skill_json):
        try:
            validate(instance=skill_json, schema=self._schema)
        except SchemaError as e:
            print(e)
        except ValidationError as e:
            print(e)
            return False
        except Exception as e:
            self._logger.log(str(e))
            print(e)
            raise
        return True

    def load(self, primary_file_path, secondary_file_path):      
        try:
            primary_skill = self.find_latest_skill(primary_file_path)
            secondary_skill = self.find_latest_skill(secondary_file_path)

            if not primary_skill or not self.validate_skill(primary_skill):
                raise
            if not secondary_skill or not self.validate_skill(secondary_skill):
                raise
            return primary_skill, secondary_skill
        except Exception as e:
            self._logger.log(str(e))
            print(e)
            raise
