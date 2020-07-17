import bluematador

# use tcpdump -i lo -n udp port 8767 -X to check that values look right over the wire

client = bluematador.BlueMatadorClient(prefix='app')
client.count('a:sdf.1', 2, labels={'tag1': None})
client.gauge('asdf.2', 45, labels={'tag2': 'tag2|value', 'tag3': 'tag3#value'})
client.close()
