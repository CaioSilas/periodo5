var queue = 'task_queue';
var msg = process.argv.slice(2).join(' ') || "Hello World!";

channel.assertQueue(queue, {
  durable: true
});
channel.sendToQueue(queue, Buffer.from(msg), {
  persistent: true
});
console.log(" [x] Sent '%s'", msg);