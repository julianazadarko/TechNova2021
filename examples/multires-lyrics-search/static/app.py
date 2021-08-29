from flask import Flask
from flask import request
from flask import render_template
#import stringComparison
from google.cloud import datastore
from flask import jsonify
import requests

app = Flask(__name__)

@app.route('/')
def my_form():
    print("go home")
    return render_template("home.html") # this should be the name of your html file

@app.route('/home', methods=['POST'])
def go_home():
    print("go home2")
    return render_template("home.html") # this should be the name of your html file

@app.route('/result', methods=['POST'])
def go_result():
    print("go result")
    print(request.form["user_input"])
    
    r = requests.post(url="http://0.0.0.0:45678/search", headers={'Content-Type':'application/json'}, data={'parameters':{'top_k':10}, 'data':[request.form['user_input']]})
#curl --request POST -d '{"parameters": {"top_k": 10}}, "data": ["hello world"]}' -H 'Content-Type: application/json' 'http://0.0.0.0:45678/search'
    r.raise_for_status()
    print(r.json())


    return render_template("result.html",value=request.form["user_input"]) # this should be the name of your html file

@app.route('/index', methods=['POST'])
def go_index():
    return render_template("index.html") # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():
    print("hello")
    print(request.form)
    text1 = request.form['q1rf']
    text2 = request.form['q2rf']

    # Instantiates a client
    datastore_client = datastore.Client()

    # The kind for the new entity
    kind = "JournalEntries"
    # The name/ID for the new entity
    ID = "passed_in"
    # The Cloud Datastore key for the new entity
    task_key = datastore_client.key(kind)

    # Prepares the new entity
    journal_entry = datastore.Entity(key=task_key)
    journal_entry["song_id"] = "id"
    journal_entry["q_type"] = "explore"
    journal_entry["q"] = "Test q"
    journal_entry["resp"] = text1

    # Saves the entity
    datastore_client.put(journal_entry)
    
    # Prepares the new entity
    journal_entry = datastore.Entity(key=task_key)
    journal_entry["song_id"] = "id"
    journal_entry["q_type"] = "explore"
    journal_entry["q"] = "Test q2"
    journal_entry["resp"] = text2

    # Saves the entity
    datastore_client.put(journal_entry)

    print(f"Saved {journal_entry.key.name}: {journal_entry}")

    return jsonify(sucess=True)

if __name__ == '__main__':
    app.run()
