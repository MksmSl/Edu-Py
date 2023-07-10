import json
from urllib import parse, request

def search_gif(word):
    url = "http://api.giphy.com/v1/gifs/search"
    params = parse.urlencode({
    "q": word,
    "api_key": "QnfznSvRsFJ3fowqeGmaMTjPuX9ojPZN",
    "limit": "5"
    })

    with request.urlopen("".join((url, "?", params))) as response:
        data = json.loads(response.read())
    try:
        result = data.get('data')[0].get('images').get('original').get('url') 
        return result
    except IndexError:
        return 'We didn\'t find a gif releted to your word'



from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6367104590:AAGqm0EDs7OpowCKgVHLGDp29aohQGv0Fz8'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nEnter word for searching GIF")

@dp.message_handler()
async def echo(message: types.Message):
    link = search_gif(message.text)
    await message.answer(link)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

#hthp://t.me/MksmSl_bot