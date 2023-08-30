from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/webhook', methods=['POST'])
def webhook_handler():
    data = request.json  # Get the JSON data from the request

    print("Received webhook data:", data)

    return jsonify({"message": "Webhook data received"})


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
