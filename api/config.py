import configparser
import os

def load_config():
    config = configparser.ConfigParser()
    config.read('api/configs.ini')

    #use for local dev - remember to update the return below to => "return db_uri_local"
    db_uri_local = f"postgresql://{config.get('database', 'user')}:{config.get('database', 'password')}@{config.get('database', 'host')}:{config.get('database', 'port')}/{config.get('database', 'dbname')}"
    
    host = os.environ.get('host')
    dbname = os.environ.get('dbname')
    port = os.environ.get('port')
    user = os.environ.get('user')
    password = os.environ.get('password')
    
    db_uri_external = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
    
    #before deploying to Vercel, ensure you have set the variables with the same names in your project
    #Vercel = https://vercel.com/docs/concepts/projects/environment-variables
    #Supabase = https://supabase.com/docs/guides/database/connecting-to-postgres#direct-connections
    #look inside your enviroment variables and add them based on your information from Supabase.
    return db_uri_external
