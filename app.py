from flask import Flask, jsonify, request

app = Flask(__name__)

# Flag to disable the app
app_disabled = False

@app.route('/check_app_status', methods=['GET'])
def check_app_status():
    return jsonify({"disabled": app_disabled})

@app.route('/disable_app', methods=['POST'])
def disable_app():
    global app_disabled
    app_disabled = True
    return jsonify({"status": "App disabled"})

@app.route('/enable_app', methods=['POST'])
def enable_app():
    global app_disabled
    app_disabled = False
    return jsonify({"status": "App enabled"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
