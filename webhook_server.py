from flask import Flask, request, jsonify
import os

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook_handler():
    data = request.json  # Get the JSON data from the request

    # Process the data as needed
    print("Received webhook data:", data)

    return jsonify({"message": "Webhook data received"})


if __name__ == '__main__':
    app.run(host='localhost', port=5000)