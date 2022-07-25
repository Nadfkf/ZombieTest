import logging
from config import dp, executor
from aiogram import types
from states import States
from aiogram.dispatcher.filters import Text

from aiogram.dispatcher import FSMContext

logging.basicConfig(level=logging.INFO)


@dp.message_handler(Text(equals=['+', '-']), state=States.reciveAnswer1)
async def test(msg: types.Message, state: FSMContext):
    user_answer = msg.text
    await state.update_data({'ans1': user_answer})
    await States.next()
    await msg.answer("Do you like eat Brains?")

@dp.message_handler(Text(equals=['+', '-']), state=States.reciveAnswer2)
async def test(msg: types.Message, state: FSMContext): 
    user_answer = msg.text
    await state.update_data({'ans2': user_answer})
    await States.next()
    await msg.answer("Are you green and rotten?")

@dp.message_handler(Text(equals=['+', '-']), state=States.reciveAnswer3)
async def test(msg: types.Message, state: FSMContext):
    user_answer = msg.text
    await state.update_data({'ans3': user_answer})
    await States.next()
    await msg.answer("Do you like to run")

@dp.message_handler(Text(equals=['+', '-']), state=States.reciveAnswer4)
async def test(msg: types.Message, state: FSMContext):
    user_answer = msg.text
    await state.update_data({'ans4': user_answer})
    await States.next()
    await msg.answer("Do you like to walk")

@dp.message_handler(Text(equals=['+', '-']), state=States.reciveAnswer5)
async def test(msg: types.Message, state: FSMContext): 
    user_answer = msg.text
    await state.update_data({'ans5': user_answer})  
    data = await state.get_data()
    await rating(data, msg)
    await state.finish()

@dp.message_handler(commands='start', state = '*')
async def offerToTest(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.reply("Test is started and I tell you instuction:Here will be showed questions and you must write + or -.")
    await States.reciveAnswer1.set()
    await msg.answer("Do you know the zombies?")

async def rating(data: dict, msg: types.Message):
    values = list(data.values())
    match values:
        case '+' | '-', '-','-','+' | '-','+' | '-':
            await msg.answer(text = "You are 100% normal human")
        case '-', '+','-','+' | '-','+' | '-':
            await msg.answer(text = "You are a Canibal")
        case '+'| '-', '+','+','+','+' | '-':
            await msg.answer(text = "You are Runing  Zombie")
        case '+'| '-', '+','+','-','+':
            await msg.answer(text = "You are Walking Zombie")
        case '+'| '-', '+','+','-', '-':
            await msg.answer(text = "You are Sitting Zombie")
     


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


     