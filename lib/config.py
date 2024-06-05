from configparser import ConfigParser

def load_config(file_path):
    config = ConfigParser()
    config.read(file_path)
    return config
