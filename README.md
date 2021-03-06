# Contact form Telegram

API for contact forms using Telegram bots with FastAPI.

## Quickstart

First of all, clone this repo.

```
git clone https://github.com/DD21S/contact-backend.git
```

Then, in the project directory, install the requirements.

```
pip install -r requirements.txt
```

Set environmet variables.

```
export API_TOKEN=your_api_token
export CHAT_ID=your_chat_id
```

And finally, run the project.

```
uvicorn main:app
```

Ready, now your API is running :&#41;

---

Consult the [documentation](https://fastapi.tiangolo.com/tutorial/cors/) for CORS configuration.

---

It's recommended to use a virtual enviroment to run Python web applications.

Create and activate one with these commands:

```
python3 -m venv venv
source ven/bin/activate
```
