from flask import Flask
app = Flask(__name__)

@app.route("/account/login/<user_id>")
def account_login(user_id):
    return "Account Login"+user_id

if __name__ == "__main__":
    app.run()
