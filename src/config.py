import json
import sys, os, pathlib

global path_script
path_script = sys.path[0]
if not os.path.isdir(path_script):
    sys.exit()
if not pathlib.Path(path_script).exists:
    sys.exit()
if not pathlib.Path(path_script).is_dir:
    sys.exit()
path_db_config = os.path.join(path_script,'db_config.json')

#config = json.load(open('db_config.json'))  #load db in json format
config = json.load(open(path_db_config))  #load db in json format
