import requests
import json

# Помещаем в переменную API_URL адрес API
API_URL = "https://tts.api.cloud.yandex.net/speech/v1/tts:synthesize"

# Помещаем в словарь data данные для отправки в API Yandex.SpeechKit
data = {
    "text": "Привет! Это пример кода для статьи про API в Skillbox Media",
    "lang": "ru-RU",
    "speed": 1,
    "voice": "filipp",
    "emotion": "good"
}

# Преобразуем данные в строку в формате JSON
json_str = json.dumps(data)

# Отправляем данные на сервер и получаем ответ
answer = requests.post(API_URL, json_str)

print(answer)