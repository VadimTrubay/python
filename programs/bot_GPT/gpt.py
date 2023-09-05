# Импортируем библиотеку
import chatterbot

# Создаем экземпляр бота
bot = chatterbot.ChatBot('Chatgpt')

# Объявляем функцию для обработки ввода пользователя
def handle_input(user_input):
    # Получаем ответ от бота
    bot_response = bot.get_response(user_input)
    # Возвращаем ответ бота
    return bot_response

# Запускаем бесконечный цикл
while True:
    # Запрашиваем ввод пользователя
    user_input = input('Введите сообщение: ')
    # Обрабатываем ввод пользователя
    bot_response = handle_input(user_input)
    # Выводим ответ бота
    print(bot_response)