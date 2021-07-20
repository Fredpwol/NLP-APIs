from dotenv import load_dotenv
load_dotenv()
from api import app

 #this is used as a minimal database for storing users and their conversations.

application = app

if __name__ == "__main__":
    app.run(debug=True)