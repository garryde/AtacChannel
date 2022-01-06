import configparser
import os
import sys


class Config:
    def __init__(self, file_name='config.ini', config_strs=[]):
        self.config_strs = config_strs
        self.file_name = file_name
        self.con = configparser.RawConfigParser()

        if not os.path.exists(file_name):
            self.con.add_section('config')
            for config_str in config_strs:
                if "list" in config_str:
                    self.con.set('config', config_str, '[]')
                else:
                    self.con.set('config', config_str, '')
            with open(file_name, 'w') as fw:
                self.con.write(fw)
            print("Running first time!")
            print('The configuration file has been generated!')
            print('Please fill configuration and run again!')
            sys.exit()
        self.con.read(file_name, encoding='utf-8')

    def read_str(self, config_key: str):
        val = dict(self.con.items('config'))[config_key]
        return 'empty' if val == "" else val

    def read_bool(self, config_key: str):
        return True if dict(self.con.items('config'))[config_key].lower() == 'true' else False

    def read_list(self, config_key: str):
        try:
            return eval(self.read_str(config_key))
        except NameError:
            return []

    def write_config(self, config_key: str, config_val: str):
        self.con.set('config', config_key, config_val)
        with open(self.file_name, 'w') as fw:
            self.con.write(fw)
