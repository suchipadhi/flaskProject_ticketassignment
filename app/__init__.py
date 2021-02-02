from flask import Flask
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

# authentication for the endpoint
USER_DATA = {

    "admin": "admin"
}


@auth.verify_password
def verify(username, password):
    if username in USER_DATA:
        return USER_DATA.get(username)
    return None


from app import views
from app import admin_views
from app import model
