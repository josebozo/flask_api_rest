#!flask/bin/python

import redis
from flask import Flask, jsonify, abort, request

redis_server = redis.Redis('localhost')

app = Flask(__name__)


@app.route('/todo/api/add', methods=['POST'])
def create_key():
    if not request.json or not 'key' in request.json or not 'value' in request.json:
        abort(400)
    kv = {
        'key': request.json['key'],
        'value': request.json.get('value')
    }
    redis_server.set(request.json['key'], request.json['value'])
    return jsonify({'kv': kv}), 201



if __name__ == '__main__':
    app.run(debug=True)