from flask import Flask, jsonify, request

app = Flask(__name__)

# Flag to disable the app
app_disabled = False

# This variable simulates the latest version information
latest_version_info = {
    "version": "1.0",
    "release_notes": "Bug fixes and performance improvements.",
    "download_url": "https://example.com/download"
}

# Endpoint to check the status of the app
@app.route('/check_app_status', methods=['GET'])
def check_app_status():
    return jsonify({"disabled": app_disabled})

# Endpoint to disable the app
@app.route('/disable_app', methods=['POST'])
def disable_app():
    global app_disabled
    app_disabled = True
    return jsonify({"status": "App disabled"})

# Endpoint to enable the app
@app.route('/enable_app', methods=['POST'])
def enable_app():
    global app_disabled
    app_disabled = False
    return jsonify({"status": "App enabled"})

# Endpoint to check for updates
@app.route('/check_for_updates', methods=['GET'])
def check_for_updates():
    client_version = request.args.get('version')  # Get version from client request
    if client_version and client_version < latest_version_info['version']:
        update_available = True
    else:
        update_available = False

    return jsonify({
        "update_available": update_available,
        "latest_version": latest_version_info['version'],
        "release_notes": latest_version_info['release_notes'],
        "download_url": latest_version_info['download_url']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
