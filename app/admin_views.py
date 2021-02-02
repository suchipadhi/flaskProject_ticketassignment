import flask

from app import app

# not necessary for the current implementation
@app.route("/admin/dashboard")
def admin_dashboard():
    ticket = [{'id': '1', 'language_restrictions': ['English'], 'platform': 'facebook_chat'}]

    return flask.jsonify(ticket)
