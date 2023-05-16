import json
from copy import deepcopy
from controllers import Merger, Intents, Exporter
from utils import Logger, File


def main():
    try:
        with open("./WatsonMerger/configs/config.json") as config_file:
            _config = json.load(config_file)

        with open("./WatsonMerger/configs/schema.json") as schema_file:
            _schema = json.load(schema_file)

        logger = Logger(_config['log_directory'])

        # File Load
        file = File(logger, _schema)
        primary_skill_file, secondary_skill_file = file.load(_config['primary_skill_dir'],
                                                             _config['secondary_skill_dir'])

        # Intentes Parse
        primary_skill_intents_data = Intents(logger, primary_skill_file)
        temp_primary_skill_intents_dict = primary_skill_intents_data.load()
        primary_skill_intents_dict = deepcopy(temp_primary_skill_intents_dict)

        secondary_skill_data = Intents(logger, secondary_skill_file)
        temp_secondary_skill_dict = secondary_skill_data.load()
        secondary_skill_dict = deepcopy(temp_secondary_skill_dict)

        # Intentes Merge
        merger_intents = Merger(logger, primary_skill_intents_dict, secondary_skill_dict)
        merge_intents_dict = merger_intents.merge_intents()

        # Intents Export
        exporter_intents = Exporter(_config['export_directory'], logger)
        exporter_intents.export_merge_intents(merge_intents_dict)

        # Logs Export
        logger.export()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
