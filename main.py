import telebot
from config import token
from collections import defaultdict  # Задание 7 - импортируем defaultdict
from logic import quiz_questions

user_responses = defaultdict(int)
# Задание 8 - создаём словарь points для каждого пользователя
points = defaultdict(int)

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я Telegram бот. Я задаю квиз. Вот мои командды: /quiz.")

def send_question(chat_id):
    question = quiz_questions[user_responses[chat_id]]
    bot.send_message(chat_id, question.text, reply_markup=question.gen_markup())

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id

    if call.data == "correct":
        bot.answer_callback_query(call.id, "Answer is correct")
        points[chat_id] += 1  # Добавляем очко пользователю
    elif call.data == "wrong":
        bot.answer_callback_query(call.id,  "Answer is wrong")

    user_responses[chat_id] += 1  # Счётчик вопросов

    if user_responses[chat_id] >= len(quiz_questions):
        if points[chat_id] == 0:
            bot.send_message(
            chat_id,
            f"Твои очки: {points[chat_id]}, ты проиграл, 0 очков это позор."
            )
        elif points[chat_id] == 1:
            bot.send_message(
            chat_id,
            f"Твои очки: {points[chat_id]}, ты проиграл, 1 очко это плохо, как так."
            )
        elif points[chat_id] == 2:
            bot.send_message(
                chat_id,
                f"Твои очки: {points[chat_id]}, ты проиграл, 2 очка это средне."
            )
        elif points[chat_id] == 3:
            bot.send_message(
                chat_id,
                f"Твои очки: {points[chat_id]}, ты проиграл, 3 очка это имба."
            )
        else:
            print('cheese')
        bot.send_message(
            chat_id, 
            "Конец печален и обиден, он есть."
        )
        # Сбросим результат для нового круга
        user_responses[chat_id] = 0
        points[chat_id] = 0
    else:
        send_question(chat_id)

@bot.message_handler(commands=['quiz'])
def start(message):
    chat_id = message.chat.id
    user_responses[chat_id] = 0
    points[chat_id] = 0
    send_question(chat_id)

bot.infinity_polling()