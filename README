# Blue Matador Metrics Client

**Send StatsD-style custom metrics to your Blue Matador dashboard**

## Installation
  * `pip install bluematador`

## Setup

To start using the Blue Matador metrics client, simply import the package an instantiate an instance
of BlueMatadorClient.

```
import bluematador

client = bluematador.BlueMatadorClient()
```

### __init__
`def __init__(self, prefix, host, port):`

* `prefix: (optional)` a string that will be prepended to the name of every metric you send. Cannot contain ':' or '|'
* `host: (optional)` specifies the host to send the custom metrics to. If no host is specified, `localhost` is the default host.
* `port: (optional)` specifies the port to send the custom metrics to. If no port is specified, `8767` is the default port.

```
import bluematador

client = bluematador.BlueMatadorClient('app', '127.0.0.1', 8767)
```

**Note:** The constructor will detect if you have set `BLUEMATADOR_AGENT_HOST` and
`BLUEMATADOR_AGENT_PORT` in the config file for your agent. Manually setting the `host` or `port`
as parameters will override environmental variables.

Once you have an instance of the Blue Matador metrics client in your code you can start sending
custom metrics. A Blue Matador agent must be configured to receive metrics at the destination host
and port.

### Gauge
`def gauge(self, name, value, sample_rate, labels):`
  * `name: (required)` The metric name e.g. 'myapp.request.size'. Cannot contain ':' or '|'
  * `value: (required)` The latest value to set for the metric
  * `sample_rate: (optional)` sends only a sample of data e.g. 0.5 indicates 50% of data being sent. Default value is 1
  * `labels: (optional)`  adds metadata to a metric. Specified as a dict of key value pairs. Cannot contain '#' or '|'

```
import bluematador

client = bluematador.BlueMatadorClient()
client.gauge('request.size', 32.25, 0.75, {'environment': 'Prod', 'account_id': '1232151'})
```

### Count
`def count(self, name, value, sample_rate, labels):`
  * `name: (required)` The metric name e.g. 'myapp.request.size'. Cannot contain ':' or '|'
  * `value: (optional)` the amount to increment the metric by, the default is 1.
  * `sampleRate: (optional)` sends only a sample of data e.g. 0.5 indicates 50% of data being sent. Default value is 1
  * `labels: (optional)`  adds metadata to a metric. Specified as a dict of key value pairs. Cannot contain '#' or '|'

```
import bluematador

client = bluematador.BlueMatadorClient()
client.count('homepage.clicks', 1, 1, {'environment': 'Prod', 'account_id': '1232151'})
```

### Close

The close method should be called when shutting down your app.

```
client.close()
```


# License

More details in [LICENSE.](https://github.com/bluematador/bluematador-metrics-client-python/blob/master/LICENSE)

Copyright (c) 2020 [Blue Matador, Inc.](https://www.bluematador.com/)
