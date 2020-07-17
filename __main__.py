import bluematador

client = bluematador.BlueMatadorClient(prefix='app')
client.count('asdf.1', 2, labels={'tag1': None})
client.gauge('asdf.2', 45, labels={'tag2': 'tag2value', 'tag3': 'tag3value'})
client.close()
