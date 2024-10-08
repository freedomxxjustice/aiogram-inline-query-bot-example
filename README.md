This code should serve an example of creating Telegram bots which can store data and then send it through inline-mode straight to the private chat / group chat.

In this project Tortoise ORM is used, but, of course, SQLAlchemy will fit alright.

Also, aiogram of the third version is used here as a leading library to work with Telegram bots.

IMPORTANT! This bot was mainly used to accept/delete/send vocie messages, thus all the media types are 'voice'. If you need to change it - https://docs.aiogram.dev/en/latest/api/types/inline_query_result.html. There you can obtain knowledge of chosen type parametres and change them if needed.
Bot doesn't have any specific features, such as anti-spam middleware and so forth.

Wish it could help you!
