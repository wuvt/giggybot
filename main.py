from flask import Flask, request
from handlers import (list_incidents, accept_incident, reject_incident,
                      resolve_incident)
app = Flask(__name__)

# "Accept" should probably be "acknowledge"
functions = {"list"   :list_incidents,
             "accept" :accept_incident,
             "reject" :reject_incident,
             "resolve":resolve_incident}

@app.route('/', methods=['POST'])
def parse_command():
    # Slack sends the command arguments in the "text" field of the
    # form data, so we first check to see if it even contains
    # any text:
    if not request.form['text']:
        return "Help!"
    # Split the received command by spaces into arguments
    args    = request.form['text'].split(' ')
    command = args[0]
    if command not in functions:
        return "Help!"
    return functions[command]()



