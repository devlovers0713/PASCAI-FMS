import pydantic
from PASCAI_FMS import file_loader
import pika, json
import PASCAI_DB.postgre_connection as pg
from dotenv import load_dotenv
import os
from config.RMQconfig import RABBITMQConfig as MQenv




def main():
    os.system('cls' if os.name == 'nt' else 'clear')  #windows and linux clear console
    print("[FMS] Starting File Loader Module")
    
    #PostgreSQL connection
    print(pg.connection())
    
    # RabbitMQ connection via pika
    print("[FMS] Connecting to RabbitMQ via pika...")
    connection_pika = pika.ConnectionParameters(host=MQenv.RABBITMQ_HOST,
                                                port=MQenv.RABBITMQ_PORT,
                                                credentials=pika.PlainCredentials(MQenv.RABBITMQ_USER, MQenv.RABBITMQ_PASSWORD))
    print(f"""[FMS] Connection parameters set.
        [rabbitMQ Connection Details]
        host: {os.getenv('RABBITMQ_HOST', 'localhost')}
        port: {os.getenv('RABBITMQ_PORT', 5672)}
        user: {os.getenv('RABBITMQ_USER','root')}""")
    
    ch_pika = pika.BlockingConnection(connection_pika).channel()
    print(f"[FMS] Connected to RabbitMQ at {os.getenv('RABBITMQ_HOST', 'localhost')}:{os.getenv('RABBITMQ_PORT', 5672)} as user {os.getenv('RABBITMQ_USER','root')}")

    # Declare queue
    print(f"[FMS] Declaring RabbitMQ queue 'FMS_queue'...")
    ch_pika.queue_declare(queue='FMS_queue', durable=True)
    print(f"[FMS] Queue 'FMS_queue' declared successfully.")


    ch_pika.basic_qos(prefetch_count=1)
    ch_pika.basic_consume(queue='FMS_queue', on_message_callback=file_loader.callback)  
    print("[FMS] Waiting for messages in 'FMS_queue'. To exit press CTRL+C")
    ch_pika.start_consuming()
    

if __name__ == "__main__":
    load_dotenv() #post process for env files
    main()
