import os
from statsd import client as statsd

class BlueMatadorClient():
    def __init__(self, prefix=None, host=os.environ.get('BLUEMATADOR_AGENT_HOST', 'localhost'), port=os.environ.get('BLUEMATADOR_AGENT_PORT', 8767)):
        self.client = statsd.StatsClient(host, port, prefix)

    def count(self, name, value=1, sample_rate=1, labels={}):
        '''
        '''
        self.client.incr(self.sanitize(name, ':'), value, sample_rate, tags=self.sanitize_labels(labels))

    def gauge(self, name, value, sample_rate=1, labels={}):
        '''
        '''
        self.client.gauge(self.sanitize(name, ':'), value, sample_rate, tags=self.sanitize_labels(labels))

    def sanitize(self, source_string, replace_string):
        sanitized_string = source_string
        if replace_string in sanitized_string:
            sanitized_string = sanitized_string.replace(replace_string, '_')
        if '|' in sanitized_string:
            sanitized_string = sanitized_string.replace('|', '_')
        return sanitized_string

    def sanitize_labels(self, labels):
        return {self.sanitize(k, '#'): self.sanitize(v, '#') if v else None for k, v in labels.items()}

    def close(self):
        # the statsd package doesn't currently support a close method for the udp client
        pass
