from configparser import ConfigParser

def load_config(file_path):
    config = ConfigParser()
    config.read(file_path)
    return config

if __name__ == "__main__":
    print("You are not suppose to run this module individually")
    