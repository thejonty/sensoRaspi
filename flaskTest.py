from flask import Flask, render_template, request, url_for
from datetime import datetime
from readWeather import readWeather
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])


def print_form():
    now = datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
        'title' : 'Humidity and Temperature Log',
        'time'  : timeString
        }
     

    if request.method == 'POST':
        readW = readWeather('humidity_temp_log.h5')
        result=request.form['fooput']
        readW.generatePlot(result)
        filename1 = 'temp_humid_' + result + '.png'
        return render_template('form.html',result=result, filename1=filename1, **templateData)
    if request.method == 'GET':
        #filename1 = 'temp.png'
        return render_template("form.html", **templateData)

if __name__ == "__main__":
    #app.run(host='0.0.0.0', debug=True)
    app.run(host='192.168.0.24', port=5000, debug=False)
