#!flask/bin/python

import redis
from flask import Flask, jsonify, abort, request

redis_server = redis.Redis('localhost')

app = Flask(__name__)



@app.route('/todo/api/read/<key>', methods=['GET'])
def get_key(key):
    if len(key) == 0:
        abort(404)
    kv = {
        'key': key,
        'value': redis_server.get(key)
    }
    return jsonify({'kv': kv})


if __name__ == '__main__':
    app.run(debug=True)