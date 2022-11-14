import uvicorn
import logging as lg
from fastapi import FastAPI, Response, status
from pydantic import BaseModel

lg.basicConfig(level=lg.INFO)

app = FastAPI()


class Message(BaseModel):
    value: str
    number: int


@app.get("/message/")
def get_messages(response: Response):
    """
    This Function stands for returning of all messages in GET request
    :return: returns the list with all messages, already sorted
    """
    response.status_code = status.HTTP_200_OK
    return "I'm here :)"


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
