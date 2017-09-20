import asyncio
import sys

class ClientProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop

    def connection_made(self, transport):
        transport.write(self.message.encode())


    def data_received(self, data):
        print(data.decode())


    def connection_lost(self, exc):
        self.loop.stop()

try:
    addr = sys.argv[1]
except:
    print('Server address not specified or incorrect')
    sys.exit()

try:
    port = int(sys.argv[2])
except:
    print('Port number not specified or incorrect')
    sys.exit()
if port > 65535 or port < 0:
    print('Port number must be int from 0 to 65535')
    sys.exit()

loop = asyncio.get_event_loop()

while True:
    try:
        message = input()
        if len(message) == 0:
            continue
    except KeyboardInterrupt:
        break
    coro = loop.create_connection(lambda: ClientProtocol(message, loop),
                                addr, port)
    try:
        loop.run_until_complete(coro)
    except Exception as e:
        print(e)
        break
    loop.run_forever()
loop.close()