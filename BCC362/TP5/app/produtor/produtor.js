const { Kafka } = require('kafkajs');

const kafka = new Kafka({
  clientId: 'produtor',
  brokers: ['kafka:9092'], // Substitua pelo endereço do broker Kafka
  retry: {
    initialRetryTime: 100,
    retries: 10, 
    maxRetryTime: 3600000,
  }  
});

const producer = kafka.producer();

const runProducer = async () => {
  await producer.connect();

  const topic = 'my-topic';
  const message = { key: 'chave', value: 'Cruzeirao Cabuloso!!!' };

  await producer.send({
    topic: topic,
    messages: [message]
  });

  console.log('Mensagem enviada com sucesso');
  await producer.disconnect();
};

const tempo_em_milisegundos = 3000;
const func = () => {runProducer().catch(console.error)}
setInterval(func, tempo_em_milisegundos)
