from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    output = None

    if request.method == "POST":
        # get url that the user has entered
        print(request.form)
        height = dict(request.form)["height"]
        weight = dict(request.form)["weight"]
        dob = dict(request.form)["dob"]
        age = 2010 - int(dob)
        position = dict(request.form)["position"]
        start = dict(request.form)["start"]
        years_played_before_2010 = 2010 - int(start)
        year_11 = dict(request.form)["2011"]
        year_12 = dict(request.form)["2012"]
        year_13 = dict(request.form)["2013"]
        year_14 = dict(request.form)["2014"]
        year_15 = dict(request.form)["2015"]
        year_16 = dict(request.form)["2016"]
        year_17 = dict(request.form)["2017"]
        year_18 = dict(request.form)["2018"]
        played = [0 for i in range(9)]
        diff = int(start) - 2011
        for i in range(len(played)):
            if i >= diff:
                played[i] = 1
        G_position = 0
        F_position = 0
        C_position = 0
        if position == 'forward':
            F_position = 1
        if position == 'center':
            C_position = 1
        if position == 'guard':
            G_position = 1
        
        # Load model
        model = pickle.load(open("model.pickle", "rb"))
        
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        
        x = [[int(height), int(weight), G_position, F_position, C_position, \
              years_played_before_2010, age, int(year_11), int(year_12), int(year_13), \
              int(year_14), int(year_15), int(year_16), int(year_17), int(year_18), \
              played[0], played[1], played[2], played[3], played[4], played[5], \
              played[6], played[7], played[8]]]

        x = scaler.fit_transform(x)
        
        #output = round(model.predict_proba(x)[0][1], 2)
        
        output = 0.49

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run()
