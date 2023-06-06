# ZOLIchatBot 1.0

Telegram Bot for Restaurant

## Project Description

A bot that helps restaurant customers learn more about the dishes served, showing photos of the dishes, their descriptions, and ingredients.

## Functionality

Sure! Here are the functionalities for your Telegram bot:

1. Command /start: initiates interaction with the bot and opens two buttons for interacting with the restaurant menu: "Menu" and "Rules".
2. Button "Menu": creates a list of dish categories and positions as a keyboard for the user, based on the dish tags present in the database. Users can select a dish category and view the full list of dishes with a short description for each dish based on the chosen category (this information is stored in the "description" field of the model object in the Django admin panel).
3. Button "Rules": displays the restaurant rules in text format;
4. When a specific dish name is selected from the dish list after selecting a category, detailed information about the dish is shown, including a photo of the dish (this information is stored in the "detail_description" and "photo" fields of the model object in the Django admin panel).

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

5. Run the server:

```
python manage.py run server
```

6. Run the bot:

```
pytnon main.py
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