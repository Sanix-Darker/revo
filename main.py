from flask import Flask, request, Response
import requests


app = Flask(__name__)

@app.route("/")
def index():

    if request.method == "GET":
        resp = requests.get("https://ipinfo.io")

        excluded_headers = ['content-encoding', 'content-length', 'transfer-enconding', 'connection']

        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]

        response = Response(resp.content, resp.status_code, headers)

    return response


if __name__ == "__main__":
    app.run(debug=True)

