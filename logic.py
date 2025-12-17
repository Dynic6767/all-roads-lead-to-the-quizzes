# Задание 2 - Импортируй нужные классы
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

class Question:

    def __init__(self, text, answer_id, *options):
        self.__text = text
        self.__answer_id = answer_id
        self.options = options

    # Задание 1 - Создай геттер для получения текста вопроса
    @property
    def text(self):
        return self.__text

    def gen_markup(self):
        # Задание 3 - Создай метод для генерации Inline клавиатуры
        markup = InlineKeyboardMarkup()
        markup.row_width = len(self.options)

        for i, option in enumerate(self.options):
            if i == self.__answer_id:
                markup.add(InlineKeyboardButton(option, callback_data="correct"))
            else:
                markup.add(InlineKeyboardButton(option, callback_data="wrong"))
        return markup
    
# Задание 4 - заполни список своими вопросами
quiz_questions = [
    Question("Что программисты делают когда что то незнают?", 1, "думают сами долго", "гуглят с инета"),
    Question("Что лучше использовать для такого случая?", 0, "спросить нейронку", "искать в яндекса", "искать в документации"),
    Question("Какой шанс что нейронка ответит правильно?", 3, "21%", "67%", "52%", "79%")
]
