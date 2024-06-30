import asyncio

import httpx


async def call_url(client):
    url = 'http://test.example/predict'
    files = {
        'image': ('dishwasher.JPEG', open('dishwasher.JPEG', 'rb'), 'image/jpeg'),
        'filename': (None, 'dishwasher.JPEG')
    }
    response = await client.request(method='POST', url=url, files=files, timeout=None)

    return response


async def main():
    with open('wl.txt', 'r') as f:
        line = f.read()
    workload = [int(i) for i in line.split(" ")]
    for load in workload:
        print(f"Running workload {load}")
        async with httpx.AsyncClient() as client:
            r1 = await asyncio.gather(*[call_url(client) for _ in range(load)])

        print(len([r.text for r in r1]))
        await asyncio.sleep(1)


asyncio.run(main())
