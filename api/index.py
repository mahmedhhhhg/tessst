from fastapi import FastAPI, Request
import requests

app = FastAPI()

API_URL = "https://devil.xo.je/v/ai/gemini.php"


@app.get("/chat")
def chat(chat: str = None):
    if not chat:
        return {
            "status": "error",
            "message": "missing parameter: chat"
        }

    try:
        # نفس curl لكن POST JSON
        r = requests.post(
            API_URL,
            json={"prompt": chat},
            headers={"Content-Type": "application/json"},
            timeout=30
        )

        data = r.json()

        return {
            "status": "success",
            "chat": chat,
            "answer": data.get("answer")
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }