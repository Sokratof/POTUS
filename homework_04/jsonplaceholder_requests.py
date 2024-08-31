"""
Создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import aiohttp
import asyncio


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def get_data(url):
    async with aiohttp.ClientSession() as session:
        print(await fetch(session, url))


async def main():
    users_data_url = asyncio.ensure_future(get_data('https://jsonplaceholder.typicode.com/users'))
    posts_data_url = asyncio.ensure_future(get_data('https://jsonplaceholder.typicode.com/posts'))
    await asyncio.gather(users_data_url, posts_data_url)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
