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


async def get_dish_info(dish: str):
    dish_url = os.getenv('GET_DETAIL_DISH_URL') + dish

    async with aiohttp.ClientSession() as session:
        async with session.get(str(dish_url)) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None


async def get_photo_from_url(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.read()
            else:
                return None
