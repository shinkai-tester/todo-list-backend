from flask import Flask, request
from resources import Entry, EntryManager

app = Flask(__name__)

FOLDER = 'C:\\Users\\alexa\\Downloads'


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route('/api/entries/')
def get_entries():
    entry_manager = EntryManager(FOLDER)
    entry_manager.load()
    result = []
    for entry in entry_manager.entries:
        result.append(entry.json())
    return result


@app.route('/api/save_entries/', methods=['POST'])
def save_entries():
    entry_manager = EntryManager(FOLDER)
    data = request.get_json()
    for entry_data in data:
        entry = Entry.from_json(entry_data)
        entry_manager.entries.append(entry)
    entry_manager.save()
    return {'status': 'success'}


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
