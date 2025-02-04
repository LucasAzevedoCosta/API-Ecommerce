from flask import Flask
from Database.database import SessionLocal
app = Flask(__name__)

@app.route('/')
def hello_world():
    db = SessionLocal()
    db.close()
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)