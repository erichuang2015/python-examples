"""尝试构建框架."""

import asyncio

from aiohttp import ClientSession


class SpiderMan:

    _session = None
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
    }

    def __init__(self):
        self._session = ClientSession()

    async def get(self, url, **kwargs):
        return await self._session.get(url, **kwargs)

    async def post(self, url, **kwargs):
        return await self._session.post(url, **kwargs)

    async def close(self):
        await self._session.close()

    def __enter__(self):
        raise TypeError("Use async with instead")

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


async def fetch(url):
    async with SpiderMan() as spiderman:
        response = await spiderman.get(url)
        return await response.text()


def main():
    url = 'http://127.0.0.1:5000/'

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(fetch(url)) for i in range(16)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    for task in tasks:
        print(task.result())


if __name__ == '__main__':
    main()
