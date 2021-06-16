import os

import requests
from flask import Flask, jsonify, request


app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'dev')
app.config['NEWS_API_URL'] = os.environ.get('NEWS_API_URL')
app.config['NEWS_API_KEY'] = os.environ.get('NEWS_API_KEY')

@app.route('/search')
def search():
    response = {}
    response_code = -1

    try:
        params = {
            'q': request.args.get('q'),
            'sortBy': request.args.get('sortBy'), 
            'pageSize': request.args.get('pageSize'),
            'page': request.args.get('page'),
            'apiKey': app.config['NEWS_API_KEY']
        }

        r = requests.get(app.config['NEWS_API_URL'], params=params)

        response = r.json()
        response_code = r.status_code
    
    except Exception as e:
        response_code = 500
        response['message'] = 'Error: {}'.format(e)

    return jsonify(response), response_code

if __name__ == "__main__":
    app.run(host='0.0.0.0')