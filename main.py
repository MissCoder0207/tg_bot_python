import logging
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from token import BOT_TOKE

BOT_TOKEN = (BOT_TOKE)
logging.basicConfig(level = logging.INFO)
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot , storage=MemoryStorage())

@dp.message_handler(commands='start')
async def start(message: types.Message):
    text = f'''
    Welcome {message.from_user.last_name} {message.from_user.first_name} to
    our LEDY.PY
    
'''
    await message.bot.send_photo(chat_id=message.chat.id , photo=open('logo.png', mode='rb'), caption=text)



if __name__ == '__main__':
    executor.start_polling(dp , skip_updates=True)