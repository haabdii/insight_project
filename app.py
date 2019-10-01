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
        dob = dict(request.form)["dob"]
        position = dict(request.form)["position"]
        start = dict(request.form)["start"]
        
        #print(dict(request.form)["2016"])
        #print(dict(request.form)["2017"])
        #year_2018 = dict(request.form)["2018"]
        
        # Load model
        #model = pickle.load(open("model.pickle", "rb"))
        #output = model.predict(X)
        #output = int(age) + int(height)
        output = 0.41

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run()
