import uvicorn
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from groq_code import qroq_response



app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"],
)

class Chatbot_request(BaseModel):
    question: str
    memory_key: int
    session_id: int

class UserSessionManager:
    def __init__(self):
        self.user_sessions = {}

    def get_session(self, session_id):
        return self.sessions.get(session_id, None)

session_manager = UserSessionManager()




@app.post("/conversation")
async def conversation_chatbot(request: Chatbot_request):
    pass



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8084)

