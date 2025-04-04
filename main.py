import telebot
from config import *
from logic import *


bot = telebot.TeleBot(API_TOKEN)



# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def generate_message(message):
    prompt = message.text

    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', api_key, secret_key)
    # Получаем ID модели
    model_id = api.get_model()
        # Генерируем изображение и получаем UUID запроса
    uuid = api.generate(prompt, model_id)
        # Проверяем статус генерации и возвращаем изображения
    images = api.check_generation(uuid)[0]
    
    file_path = 'dec.png'
    api.save_image(images, file_path)
    

    with open(file_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


bot.infinity_polling()