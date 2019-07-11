from flask import Flask
from subprocess import call

app = Flask(__name__)

@app.route("/", methods=["POST"])
def kick_off_script():
    call(["./script.sh"])
    return "job started"

if __name__ == '__main__':
    app.run()
