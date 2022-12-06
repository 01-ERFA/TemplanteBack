from config import app
from utils.db import db

if __name__ == '__main__':
    app.run(debug=True, port=4000)