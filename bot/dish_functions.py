from dish.models import Dish
from asgiref.sync import sync_to_async


async def get_menu_items():
    return list(Dish.objects.all())


async def get_dish_by_id(dish_id):
    return Dish.objects.get(id=dish_id)


def format_dishes(dishes):
    formatted_text = ""
    for dish in dishes:
        formatted_text += f"- {dish}\n"
    return formatted_text

@sync_to_async
def get_dish_tags():
    tags = Dish.objects.values_list('tag', flat=True).distinct()
    return list(tags)


async def get_dishes_by_tag(tag):
    dishes = await Dish.objects.filter(tag=tag).values_list('name', flat=True)
    return list(dishes)


