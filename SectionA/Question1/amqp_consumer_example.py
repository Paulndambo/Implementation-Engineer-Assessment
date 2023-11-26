import pika

class BaseConsumer:
    def __init__(self, url, exchange_name, queue_name, routing_key):
        self.url = url
        self.exchange_name = exchange_name
        self.queue_name = queue_name
        self.routing_key = routing_key
        self.connection = None
        self.channel = None

    def _start_connection(self):
        params = pika.URLParameters(self.url)
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()

        # Declare a topic exchange
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type='topic')

        # Declare a queue with a specific routing key binding
        self.channel.queue_declare(queue=self.queue_name, durable=True)
        self.channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name, routing_key=self.routing_key)

    def callback(self, ch, method, properties, body):
        print(f' [x] Received {body} with routing key: {method.routing_key}')

    def _consume_messages(self):
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback, auto_ack=True)
        print(f' [*] Waiting for messages with routing key {self.routing_key}:')
        self.channel.start_consuming()

    def _close_connection(self):
        if self.connection and self.connection.is_open:
            self.connection.close()

if __name__ == "__main__":
    url = 'amqps://ncvxnkvq:Vpf8yc_tTiFuqfXj_7hDqaiDGH4LYmCy@hummingbird.rmq.cloudamqp.com/ncvxnkvq'
    exchange_name = 'topic_exchange'
    queue_name = 'test_queue'
    routing_key = 'test.*'

    consumer = BaseConsumer(url, exchange_name, queue_name, routing_key)
    consumer._start_connection()

    try:
        consumer._consume_messages()
    except KeyboardInterrupt:
        print('Interrupted. Closing connection...')
    finally:
        consumer._close_connection()
