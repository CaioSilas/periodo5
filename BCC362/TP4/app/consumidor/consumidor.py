import pika
import time
import os

# Variáveis para estatísticas do consumidor
mensagens_recebidas = 0
mensagem_esperadas = 10
inicio_segundos = time.time()

# Função para processar as mensagens recebidas
def processar_mensagem(ch, method, properties, body):
    global mensagens_recebidas
    mensagens_recebidas += 1
    print("Mensagem recebida:", body)
    # # Calcula o tempo decorrido e exibe o número de mensagens por segundo
    # tempo_decorrido = time.time() - inicio_segundos
    # mensagens_por_segundo = mensagens_recebidas / tempo_decorrido
    # print("Mensagens por segundo:", mensagens_por_segundo)

    # if mensagens_recebidas >= mensagem_esperadas:
    #         ch.stop_consuming()

# Estabelece a conexão com o servidor RabbitMQ
print(os.environ['R_HOST'])
connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ['R_HOST']))
channel = connection.channel()

# Declara a fila no servidor RabbitMQ
channel.queue_declare(queue='minha_fila')

# Registra a função de callback para receber mensagens
channel.basic_consume(queue='minha_fila', on_message_callback=processar_mensagem, auto_ack=True)

print('Aguardando mensagens. Pressione CTRL+C para sair.')

# Inicia o consumo de mensagens
channel.start_consuming()

# Calcula o tempo decorrido e exibe o número de mensagens por segundo
tempo_decorrido = time.time() - inicio_segundos
mensagens_por_segundo = mensagens_recebidas / tempo_decorrido
print("Mensagens por segundo:", mensagens_por_segundo)
