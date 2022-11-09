import logging
from oxforddictionaries import getDefinitions
from aiogram import Bot, Dispatcher, executor, types
from TransleteTest import getTranslate
from TransleteTest import getTranslateLang
from googletrans import Translator
translator = Translator()

API_TOKEN = '5304403653:AAHI9-Y8u8Q5Ws8lM3_n2kghH7nodyVjnQs'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Tarjimon  Botga Xush Kelibsiz! ")


@dp.message_handler()
async def translator(message: types.Message):

    if len(message.text.split()) > 2:
        await message.reply(getTranslate(message.text))
    else:
        text = message.text
        if getTranslateLang(message.text) == 'en':
            text = getTranslate(message.text)
        response = getDefinitions(text)
        if not response:
            await message.reply(getTranslate(message.text))

        else:

            try:
                definition = response['definitions']
                await message.reply(f"Word: {text}\nDefinitions: \n{definition}")
                if response.get('audio'):
                    await  message.reply_audio(response['audio'])
            except:
                await message.reply(getTranslate(message.text))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
