from flask import Flask, request

app = Flask(__name__)

@app.errorhandler(404)
def catch_all(*more):
    d =  {
        'path': request.path,
        'type': request.content_type,
        'data': request.data,
        'headers': request.headers,
        'args': request.args,
        'variable': more,
    }
    print(f'{d}')
    return "[]", 200

