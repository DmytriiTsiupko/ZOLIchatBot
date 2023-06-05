# ZOLIchatBot

Telegram Bot

## Project Description

A bot that helps restaurant customers learn more about the dishes served, showing photos of the dishes, their descriptions, and ingredients.

## Functionality

Sure! Here are the functionalities for your Telegram bot:

1. **/start command**: Upon starting the interaction with the bot, it will greet the user and provide instructions on how to use it.

2. **The button "Menu"**: When this command is triggered, the bot will display the restaurant's menu categorized by types of dishes (e.g., soups, main courses, desserts). The user can select a specific type of dish.

3. **Displaying dishes**: After choosing a type of dish, the bot will show a list of dishes belonging to that category. The user can select a particular dish to obtain more detailed information.

4. **Dish description**: Upon selecting a specific dish, the bot will provide a full description of the dish. The description may include information about the ingredients, preparation method, origin, etc.

5. **Dish visual representation**: After displaying the dish description, the bot can send a photograph to showcase how the dish looks. The photograph can be attached to the message or sent as a link to an image.

6. **The button "Rules"**: When this command is invoked, the bot will present the restaurant's rules. These rules could cover behavior guidelines, ordering procedures, operating hours, etc.

Please note that the functionalities mentioned above serve as a basic outline, and you can customize them further based on your specific requirements and preferences.

## Installation and Setup

1. Clone the repository from GitHub:

```
git clone https://github.com/DmytriiTsiupko/ZOLIchatBot
```

2. Install the project dependencies:

```
pip install -r requirements.txt
```

3.Create a `.env` file and provide the necessary configuration data, for example:

```
BOT_TOKEN=your_bot_token
SECRET_KEY=your_api_key
```


4. Run command "docker compose -d"

```
docker compose -d
```
5. :

```
python main.py
```

## Making Changes and Development

If you wish to make changes or develop additional features for this project, you can follow these steps:

1. Create a new branch for development:

```
git checkout -b feature/your-feature-name
```

2. Make the necessary changes and developments.

3. Commit the changes:

```
git commit -m "Add your commit message"
```

4. Push the branch to the remote repository:

```
git push origin feature/your-feature-name
```

5. Open a pull request to the project's main branch.

## Authors

Author: Dmytrii Tsiupko

## License

[MIT License](https://opensource.org/licenses/MIT)

This project is distributed under the MIT License. For more information, see the LICENSE file.