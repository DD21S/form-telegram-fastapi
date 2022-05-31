import os
import requests

from fastapi import FastAPI
from pydantic import BaseModel

API_TOKEN = os.environ.get('API_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

app = FastAPI()

class ContactForm(BaseModel):
    name: str
    email: str
    message: str

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "johndoe@example.com",
                "message": "I need your help."
            }
        }


@app.post("/")
async def contact_telegram(contact_form: ContactForm):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(API_TOKEN)

    name = contact_form.name
    email = contact_form.email
    message = contact_form.message

    text = "{}\n{}\n\n{}".format(name, email, message)

    params = {
        'chat_id': CHAT_ID,
        'text': text,
        'disable_web_page_preview': True,
        'protect_content': True
    }

    r = requests.get(url, params=params)

    return {"message": "Message sent successfully."}