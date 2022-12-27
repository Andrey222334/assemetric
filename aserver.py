import asyncio, socket, os

async def handle_client(reader, writer):
    request = None
    while request != 'quit':
        request = (await reader.read(255)).decode('utf8')
        response = str(eval(request)) + '\n'
        writer.write(response.encode('utf8'))
        await writer.drain()
    writer.close()
    os._exit(0)

async def run_server():
    server = await asyncio.start_server(handle_client, 'localhost', 15555)
    async with server:
        await server.serve_forever()

asyncio.run(run_server())

