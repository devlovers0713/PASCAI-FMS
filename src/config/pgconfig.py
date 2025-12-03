import os
from dotenv import load_dotenv

load_dotenv() #post process for env files

class POSTGRESConfig:
    POSTGRES_HOST = os.getenv("POSTGRES_HOST", 'test')
    POSTGRES_DB = os.getenv("POSTGRES_DB",'a')
    POSTGRES_USER = os.getenv("POSTGRES_USER", 'b')
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", 'c')
    POSTGRES_PORT = os.getenv("POSTGRES_PORT",'d')
