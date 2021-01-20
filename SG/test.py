from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/wifi', methods=['POST'])
def wifi():
    nomBorne = request.form['borne']
    r = requests.get('http://api.site.org/weather?borne='+nomBorne+'')
    json_object = r.json()
    return render_template('wifi.html')

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)