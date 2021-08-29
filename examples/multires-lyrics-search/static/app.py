from flask import Flask
from flask import request
from flask import render_template
#import stringComparison
from google.cloud import datastore
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html") # this should be the name of your html file

@app.route('/home', methods=['POST'])
def go_home():
    print("entered home")
    return render_template("home.html") # this should be the name of your html file

@app.route('/', methods=['POST'])
def my_form_post():
    print("hello")
    print(request.form)
    text1 = request.form['q1rf']
    text2 = request.form['q2rf']
    #plagiarismPercent = stringComparison.extremelySimplePlagiarismChecker(text1,text2)
    plagiarismPercent = 0



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
    #if plagiarismPercent > 50 :
    #    return "<h1>Plagiarism Detected !</h1>"
    # else :
    #    return "<h1>No Plagiarism Detected !</h1>"

if __name__ == '__main__':
    app.run()
