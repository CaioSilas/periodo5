var queue = 'task_queue';

// This makes sure the queue is declared before attempting to consume from it
channel.assertQueue(queue, {
  durable: true
});

channel.consume(queue, function(msg) {
  var secs = msg.content.toString().split('.').length - 1;

  console.log(" [x] Received %s", msg.content.toString());
  setTimeout(function() {
    console.log(" [x] Done");
  }, secs * 1000);
}, {
  // automatic acknowledgment mode,
  // see ../confirms.html for details
  noAck: true
});