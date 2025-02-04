from flask import Flask
from Database.database import SessionLocal
from Database.database import engine, Base
from Models import User, Product

app = Flask(__name__)

Base.metadata.create_all(bind=engine)

@app.route('/')
def hello_world():
    db = SessionLocal()
    db.close()
    return "hello world"

if __name__ == "__main__":
    app.run(debug=True)