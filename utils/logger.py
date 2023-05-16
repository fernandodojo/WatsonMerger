import json
import os


class Logger:
    errors = []
    log = {"qtd": 0, 'errors': []}

    def __init__(self, log_directory):
        self._log_directory = log_directory

    def export(self):
        try:
            if len(self.errors) > 0:
                if not os.path.exists(self._log_directory):
                    os.makedirs(self._log_directory)

                self.log['qtd'] = len(self.log['errors'])
                out_file = open(self._log_directory + "fail.json", "w")
                json.dump(self.log, out_file, indent=4)
                out_file.close()

                print("Failed execution\n{}".format(self._log_directory + "fail.json"))
            else:
                print("Successful execution ")
        except Exception as e:
            self.log['errors'].append(str(e))
            print(self.log['errors'])
            print(e)

    def log(self, error):
        try:
            self.errors.append(error)
        except Exception as e:
            self.log['errors'].append(str(e))
            print(self.log['errors'])
            print(e)

    def log_merge(self, name, dictionary):
        try:
            if not os.path.exists(self._log_directory):
                os.makedirs(self._log_directory)

            out_file = open(self._log_directory + name + ".json", "w")
            json.dump(dictionary, out_file, indent=4, sort_keys=True, ensure_ascii=False)
            out_file.close()
        except Exception as e:
            self.log['errors'].append(str(e))
            print(self.log['errors'])
            print(e)
