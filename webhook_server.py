from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/api/webhook', methods=['POST'])
def webhook_handler():
    try:
        data = request.json if request else None

        print("Received webhook data:", data)

        return jsonify({"message": "Webhook data received"})
    except Exception as e:
        return jsonify({"Error": str(e)})


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
