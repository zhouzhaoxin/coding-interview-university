import time

from canal.client import Client

client = Client()
client.connect(host='127.0.0.1', port=11111)
client.check_valid(username=b'', password=b'')
client.subscribe(client_id=b'1001', destination=b'test', filter=b'.*\\..*')
while True:
    time.sleep(1)
    message = client.get(100)
    print(message)