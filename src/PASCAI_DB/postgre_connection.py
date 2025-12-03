import psycopg2 as postgre
import os
from dotenv import load_dotenv
from config.pgconfig import POSTGRESConfig as PGenv


load_dotenv() #post process for env files



def connection():
    
    try:
        conn = postgre.connect(
            host=PGenv.POSTGRES_HOST,
            database=PGenv.POSTGRES_DB,
            user=PGenv.POSTGRES_USER,
            password=PGenv.POSTGRES_PASSWORD,
            port=PGenv.POSTGRES_PORT
        )
        return f"[FMS | DB] Connected to PostgreSQL database: {os.getenv('POSTGRES_DB')} at {os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')} as user {os.getenv('POSTGRES_USER')}"

    except Exception as e:
        return f"""[FMS | DB] Error connecting to PostgreSQL database: {e} 
        \n env vars: {PGenv.POSTGRES_HOST},
                     {PGenv.POSTGRES_DB},
                     {PGenv.POSTGRES_USER},
                     {PGenv.POSTGRES_PORT}
                     """