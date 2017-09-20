import asyncio
import socket
import sys

class ServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport


    def data_received(self, data):
        message = data.decode()

        if message == 'quit':
            loop.stop()
            return

        if len(message.split()) < 2:
            self.transport.close()
            return

        message = message.split()

        if message[0] == 'get':
            prefix = message[1]
            answer = find_words(prefix)
            if answer:
                self.transport.write(answer.encode('utf-8'))
        else:
            self.transport.write('Unknown'.encode('utf-8'))

        self.transport.close()


def qsort_words(w, n, first, last):
    '''
        Realization of quick sort algoritm for dictionary.
        w -- array of words
        n -- array of frequencies
        first, last -- the first and the last bounds of an arrays' parts that
        are being sorted on the current iteration

    '''
    l = first
    r = last
    m = n[int(((l+r)/2))]

    while l <= r:
        while n[l] > m:
            l += 1
        while n[r] < m:
            r -= 1

        if l <= r:
            if l < r:
                n[l], n[r] = n[r], n[l]
                w[l], w[r] = w[r], w[l]
            l += 1
            r -= 1

    if l < last:
        qsort_words(w,n,l,last)
    if r > first:
        qsort_words(w,n,first,r)


def find_words(prefix):
    ''' Finding words in sorted dictionary

    '''
    words = list(filter(lambda s: s.startswith(prefix),wi))
    if words == []:
        return None
    if len(words) > 10:
        words = words[0:10]
    result = '\n'.join(words)
    result += '\n'
    return result

try:
    dict_path = sys.argv[1]
except:
    print('Path not specified or incorrect')
    sys.exit()
try:
    port = int(sys.argv[2])
except:
    print('Port number not specified or incorrect')
    sys.exit()

if port > 65535 or port < 0:
    print('Port number must be int from 0 to 65535')
    sys.exit()

my_ip = socket.gethostbyname(socket.gethostname())

wi = []
ni = []

try:
    f = open(dict_path, 'r')

except Exception as e:
    print(e)
    sys.exit()

else:
    for line in f:
        splitted = line.split()
        if len(splitted) != 2:
            continue
        wi.append(splitted[0])
        try:
            ni.append(int(splitted[1]))
        except:
            wi.pop() # ignore a word if second argument is not int
    f.close()

    if len(wi) == 0:
        print('Error: dictionary is empty')
        sys.exit()

    qsort_words(wi,ni,0,len(wi)-1)

    for i in range(0,len(ni)-1): # Sorting words with same frequency.
        if ni[i] == ni[i-1]:
            t = i
            while True:
                if t < len(ni):
                    if ni[t] == ni[t-1]:
                        t += 1
                    else:
                        break
                else:
                    break
            wi[i-1:t+1] = sorted(wi[i-1:t+1])



loop = asyncio.get_event_loop()
coro = loop.create_server(ServerProtocol, my_ip, port)
server = loop.run_until_complete(coro)

try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

server.close()
loop.run_until_complete(server.wait_closed())
loop.close()