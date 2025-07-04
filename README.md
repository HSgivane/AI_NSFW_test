# Сервер модерации изображений

### Простой сервер на FastAPI, который принимает изображение и проверяет его на наличие NSFW-контента.

### 1. Клонируй проект

```bash
git clone https://github.com/HSgivane/AI_NSFW_test
cd AI_NSFW_test
```

### 2. Установи зависимости
```bash
pip install -r requirements.txt
```

### 3. Укажи API-ключ DeepAI
Создай файл .env в корне проекта и добавь туда:
```
API_KEY='твой_API_ключ_от_DeepAI'
```
Создать ключ можно перейдя на https://deepai.org

### 4. Запусти сервер
Через консоль
```bash
uvicorn main:app --reload
```
Либо же запустив main.py

## Пример запроса
### Отправка изображения через curl в bush (изображение должно лежать в корне проекта и иметь расширение .png или .jpg):
```bash
curl -X POST -F "file=@example.jpg" http://localhost:8000/moderate
```

### Либо же через powershell:
```powershell
curl.exe -X POST -F "file=@example.jpg" http://localhost:8000/moderate
```
## Примеры ответа:
### Обычное изображение:
```json
{
  "status": "OK"
}
```
### NSFW изображение:
```json
{
  "status": "REJECTED",
  "reason": "NSFW content"
}
```
