from bot import bot
from handlers import start, help, highprices, lowprices, bestdeal


if __name__ == '__main__':
	bot.polling(non_stop=True)


