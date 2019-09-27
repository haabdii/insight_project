from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    output = None

    if request.method == "POST":
        # get url that the user has entered
        print(request.form)
        age = dict(request.form)["age"]
        height = dict(request.form)["height"]
        weight = dict(request.form)["weight"]
        
        # Load model
        #model = pickle.load(open("model.pickle", "rb"))
        #output = model.predict(X)
        output = int(age) + int(height)

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run()
