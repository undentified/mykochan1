from app import app
import views
from flask import session

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)