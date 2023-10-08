const { Kafka } = require('kafkajs');

const kafka = new Kafka({
  clientId: 'consumidor',
  brokers: ['kafka:9092'], // Substitua pelo endereço do broker Kafka
  retry: {
    initialRetryTime: 100,
    retries: 10,
    maxRetryTime: 3600000,
  }
});

const consumer = kafka.consumer({ groupId: 'meu-grupo' });
const runConsumer = async () => {
  await consumer.connect();
  await consumer.subscribe({ topic: 'my-topic', fromBeginning: true });

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      console.log(`Mensagem recebida - Partição: ${partition}, Valor: ${message.value}`);
    }
  });
};

runConsumer().catch(console.error);
