import os
from statsd import client as statsd

class BlueMatadorClient():
    def __init__(self, prefix=None, host=os.environ.get('BLUEMATADOR_AGENT_HOST', 'localhost'), port=os.environ.get('BLUEMATADOR_AGENT_PORT', 8767)):
        print((host, port, prefix))
        self.client = statsd.StatsClient(host, port, prefix)

    def count(self, name, value=1, sample_rate=1, labels={}):
        '''
        '''
        self.client.incr(name, value, sample_rate, tags=labels)

    def gauge(self, name, value, sample_rate=1, labels={}):
        '''
        '''
        self.client.gauge(name, value, sample_rate, tags=labels)

    def close(self):
        # the statsd package doesn't currently support a close method for the udp client
        pass
