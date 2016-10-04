import sys
import time
import telepot
from telepot.namedtuple import InlineQueryResultArticle, InputTextMessageContent
TOEKN=sys.argv[1]
bot= telepot.Bot(TOKEN)
bot.getMe()

