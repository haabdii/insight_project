from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    output = None

    if request.method == "POST":
        
        output = 0.49

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run()
