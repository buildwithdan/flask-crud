import configparser

def load_config():
    config = configparser.ConfigParser()
    config.read('api/configs.ini')

    db_uri = f"postgresql://{config.get('database', 'user')}:{config.get('database', 'password')}@{config.get('database', 'host')}:{config.get('database', 'port')}/{config.get('database', 'dbname')}"
    return db_uri
