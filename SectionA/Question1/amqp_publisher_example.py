import os
import pika
import os
import pika
import json

AMQP_URL = 'amqps://ncvxnkvq:Vpf8yc_tTiFuqfXj_7hDqaiDGH4LYmCy@hummingbird.rmq.cloudamqp.com/ncvxnkvq'

class BasePublisher(object):
    def __init__(self, routing_key, body) -> None:
        self.exchange = "test_exchange"
        self.queue = "test_queue"
        self.routing_key = routing_key
        self.url = AMQP_URL
        self.body = body

    def run(self):
        self._start_connection()
        self._publish_message()
        

    def _start_connection(self):
        params = pika.URLParameters(self.url)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()

        channel.exchange_declare(self.exchange)
        channel.queue_declare(queue=self.queue, durable=True)
        channel.queue_bind(self.queue, self.exchange, self.routing_key)

        return channel, connection

    def _publish_message(self):
        channel, connection = self._start_connection()
        channel.basic_publish(
            body=json.dumps(self.body),
            exchange=self.exchange,
            routing_key=self.routing_key
        )
        channel.close()
        connection.close()


publisher = BasePublisher(
    routing_key="testing_queue",
    body={
        "name": "Paul Ndambo",
        "school": "Masinde Muliro University of Sci. & Tech.",
        "programme": "Bsc. Information Technology",
        "specialty": "Backend Software Engineering"
    }
)
publisher.run()