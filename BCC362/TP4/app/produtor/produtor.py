import pika
import time
import os

# Função para enviar mensagens para a fila
def enviar_mensagens(qtd_mensagens, tamanho_mensagem, intervalo_segundos):
    connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ['R_HOST']))
    channel = connection.channel()

    # Declara a fila no servidor RabbitMQ
    channel.queue_declare(queue='minha_fila')

    for i in range(qtd_mensagens):
        mensagem = 'Mensagem ' + str(i + 1) + ' ' + 'X' * tamanho_mensagem
        channel.basic_publish(exchange='', routing_key='minha_fila', body=mensagem)
        print("Mensagem enviada:", mensagem)
        time.sleep(intervalo_segundos)

    connection.close()

# Variáveis para definir as configurações do produtor
qtd_mensagens = 10
tamanho_mensagem = 100
intervalo_segundos = 2

# Envia as mensagens para a fila
while True:
    time.sleep(0.2)   
    enviar_mensagens(qtd_mensagens, tamanho_mensagem, intervalo_segundos)