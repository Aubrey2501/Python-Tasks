from bot import bot
from telebot.types import Message
from config_utils import MESSAGES
from database.db_utils import get_history


@bot.message_handler(commands=["history"])
def cmd_history(message: Message):
    history = get_history()
    print(history)
    text = "\n".join([
        f"Команда: {row['cmd']}\n"
        f"Время: {row['cmd_time']}\n"
        f"Отели:\n- " + "\n- ".join(row['hotels']) + "\n\n"
        for row in history
    ])

    bot.reply_to(message, text)