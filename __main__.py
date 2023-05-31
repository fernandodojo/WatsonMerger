import json
from copy import deepcopy
from controllers import Exporter, Merger, Threading
from modules import Entities, File, Intents
from utils import Logger


def intents_threading(logger, config, primary_skill_file, secondary_skill_file):
    try:
        # Intentes Parse
        primary_skill_intents_data = Intents(logger, primary_skill_file)
        temp_primary_skill_intents_dict = primary_skill_intents_data.load()
        primary_skill_intents_dict = deepcopy(temp_primary_skill_intents_dict)

        secondary_skill_data = Intents(logger, secondary_skill_file)
        temp_secondary_skill_dict = secondary_skill_data.load()
        secondary_skill_intents_dict = deepcopy(temp_secondary_skill_dict)

        # Intentes Merge
        merger_intents = Merger(logger, primary_skill_intents_dict, secondary_skill_intents_dict)
        merge_intents_dict = merger_intents.merge_intents()
        diff_intents_dict = merger_intents.diff_intents()

        # Intents Export
        exporter_intents = Exporter(config['export_directory'], logger)
        exporter_intents.export_merge_intents(merge_intents_dict)
        exporter_intents.export_diff_intents(diff_intents_dict)
    except Exception as e:
        print(e)
        return False
    else:
        return True

def entities_threading(logger, config , primary_skill_file, secondary_skill_file):
    try:
        # Entities Parse
        primary_skill_entities_data = Entities(logger, primary_skill_file)
        temp_primary_skill_entities_dict = primary_skill_entities_data.load()
        primary_skill_entities_dict = deepcopy(temp_primary_skill_entities_dict)

        secondary_skill_entities_data = Entities(logger, secondary_skill_file)
        temp_secondary_skill_entities_dict = secondary_skill_entities_data.load()
        secondary_skill_entities_dict = deepcopy(temp_secondary_skill_entities_dict)

        # Entities Merge
        merger_entities = Merger(logger, primary_skill_entities_dict, secondary_skill_entities_dict)
        merge_entities_dict = merger_entities.merge_entities()
        diff_entities_dict = merger_entities.diff_entities()

        # Entities Export
        export_entities = Exporter(config['export_directory'], logger)
        export_entities.export_merge_entities(merge_entities_dict)
        export_entities.export_diff_entities(diff_entities_dict)
    except Exception as e:
        print(e)
        return False
    else:
        return True

     
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
        
        intents_thread = Threading(target=intents_threading, args=(logger, _config, primary_skill_file,
                                                                    secondary_skill_file, ))
        entities_thread = Threading(target=entities_threading, args=(logger, _config , primary_skill_file,
                                                                      secondary_skill_file, ))

        intents_thread.start()
        entities_thread.start()

        print("Intents execution successful: {}".format(intents_thread.join()))
        print("Entities execution successful: {}".format(entities_thread.join()))

        # Logs Export
        logger.export()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
