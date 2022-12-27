import asyncio

HOST = 'localhost'
PORT = 15555
request = None


async def tcp_echo_client(host, port):
    global request
    reader, writer = await asyncio.open_connection(host, port)

    while request != 'quit':
        request = input('>> ')
        if request:
            writer.write(request.encode())
            await writer.drain()
            data = await reader.read(255)
            print(data.decode())

    writer.close()
    await writer.wait_closed()


asyncio.run(tcp_echo_client(HOST, PORT))


