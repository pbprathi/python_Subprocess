import json
import os
class jsonConfig:
    def getconfig(arg1, arg2):
        script_path = os.path.abspath(__file__) # i.e. /path/to/dir/foobar.py
        script_dir = os.path.split(script_path)[0] #i.e. /path/to/dir/
        rel_path = script_dir+"/config.json"
        with open(rel_path) as data_file:
            data = json.load(data_file)
            return data[arg1][arg2]
