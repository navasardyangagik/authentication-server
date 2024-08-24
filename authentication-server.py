from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/verify_license', methods=['POST'])
def verify_license():
    # Load keys from JSON file
    try:
        with open('keys.json', 'r') as keyfile:
            keys_data = json.load(keyfile)
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "Key database not found"}), 500

    # Get license key from request data
    data = request.get_json()
    license_key = data.get('key')

    # Check if the key exists in the JSON data
    for entry in keys_data:
        if entry['key'] == license_key:
            return jsonify({
                "status": "valid",
                "username": entry['username'],
                "subscription_type": entry['subscription_type'],
                "access_token_chars": entry['access_token_chars'], 
                "version": "0.12"
            }), 200

    # If no matching key is found
    return jsonify({"status": "invalid"}), 403

@app.route('/verify_license_lite', methods=['POST'])
def verify_license_lt():
    # Load keys from JSON file
    try:
        with open('keys.json', 'r') as keyfile:
            keys_data = json.load(keyfile)
    except FileNotFoundError:
        return jsonify({"status": "error", "message": "Key database not found"}), 500

    # Get license key from request data
    data = request.get_json()
    license_key = data.get('key')

    # Check if the key exists in the JSON data
    for entry in keys_data:
        if entry['key'] == license_key:
            return jsonify({
                "status": "valid",
                "username": entry['username'],
                "subscription_type": entry['subscription_type'],
                "version": "0.01"
            }), 200

    # If no matching key is found
    return jsonify({"status": "invalid"}), 403
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)