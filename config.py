from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types



Token = "BOT_TOKEN"

bot = Bot(token=Token)
dp = Dispatcher(bot, storage=MemoryStorage())