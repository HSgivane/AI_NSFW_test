from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import httpx, uvicorn, os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.deepai.org/api/nsfw-detector"

app = FastAPI(
    title="Сервер модерации изображений",
)

@app.post("/moderate")
async def moderate_image(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=415, detail="Неподдерживаемый тип файла")
    contents = await file.read()
    headers = {"api-key": API_KEY}
    files = {"image": (file.filename, contents, file.content_type)}

    async with httpx.AsyncClient() as client:
        response = await client.post(API_URL, headers=headers, files=files)
        if response.status_code != 200:
            raise HTTPException(status_code=502, detail="Ошибка на стороне сервера")
        data = response.json()

    nsfw_score = data.get("output", {}).get("nsfw_score")
    if nsfw_score is None:
        raise HTTPException(status_code=502, detail="Неверный ответ от сервера")
    if nsfw_score > 0.7:
        return JSONResponse(status_code=200, content={"status": "REJECTED", "reason": "NSFW content"})
    return JSONResponse(status_code=200, content={"status": "OK"})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

