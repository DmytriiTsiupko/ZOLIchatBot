import os
from dotenv import load_dotenv
import aiohttp

load_dotenv()


async def get_dishes():
    async with aiohttp.ClientSession() as session:
        async with session.get(os.getenv('GET_DISHES_URL')) as response:
            return await response.json()


async def get_dishes_by_tag(tag: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(os.getenv('GET_DISHES_URL')) as response:
            data = await response.json()

            # Фільтруємо дані за обраним тегом
            filtered_dishes = [dish for dish in data if dish.get('tag') == tag]

            return filtered_dishes
