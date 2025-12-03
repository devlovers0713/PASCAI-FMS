import os

class RABBITMQConfig:
    RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')
    RABBITMQ_PORT = int(os.getenv('RABBITMQ_PORT', 5672))
    RABBITMQ_USER = os.getenv('RABBITMQ_USER','root')
    RABBITMQ_PASSWORD = os.getenv('RABBITMQ_PASSWORD','1234')