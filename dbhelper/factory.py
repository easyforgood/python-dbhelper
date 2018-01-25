
class __DBFactory:
    def __init__(self, config):
        self.config = config or dict()

    def get_mysql(self, _config):
        from .mysql_db import DBHelper
        if isinstance(_config, str):
            _config = self.config.get(_config, None)
        if not _config:
            raise ValueError("config is empty or wrong")
        return DBHelper(**_config)

    def get_mongodb(self, _config):

        from .mongodb import get_mongodb
        if isinstance(_config, str):
            _config = self.config.get(_config, None)
        if not _config:
            raise ValueError("config is empty or wrong")
        return get_mongodb(**_config)


import os
def load_config(filename="db.json"):
    if os.path.exists(os.path.join(os.getcwd(), "db.json")):
        try:
            with open(filename, "r") as f:
                from json import load
                return load(f)
        except:
            pass

config = load_config()

factory = __DBFactory(config)

