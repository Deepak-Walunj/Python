from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    url = "https://lernx.io/Courses/Python-3-Bootcamp/view.php?code=2.7-8"
    req = requests.get(url)
    
    if req.status_code == 200:
        content_type = req.headers.get('Content-Type')
        if 'application/json' in content_type:
            data = req.json()
            return jsonify(data)
        else:
            return req.text, 200
    else:
        return jsonify({'error': f'Request failed with status code: {req.status_code}'}), req.status_code

if __name__ == '__main__':
    app.run(debug=True)
