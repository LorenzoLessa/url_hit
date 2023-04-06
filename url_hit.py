import asyncio
from aiohttp import ClientSession

# Defina a URL que você deseja acessar
url = 'http://hello-hello-prdejxtp1khy-767387691.us-east-1.elb.amazonaws.com/'

# Cria uma função que envia uma solicitação HTTP
async def send_request(session):
    async with session.get(url) as response:
        status_code = response.status
        print(f'Response status code: {status_code}')

# Cria uma função assíncrona que envia várias solicitações HTTP simultaneamente
async def send_multiple_requests(num_requests):
    async with ClientSession() as session:
        tasks = []
        for i in range(num_requests):
            tasks.append(asyncio.create_task(send_request(session)))
        await asyncio.gather(*tasks)

# Inicia o loop assíncrono e envia solicitações simultaneamente
asyncio.run(send_multiple_requests(18000))
