from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/verify_license', methods=['POST'])
def verify_license():
    keylist = open('Key_List.txt','r')
    VALID_LICENSE_KEYS = keylist.readlines()

    i=0

    while i<len(VALID_LICENSE_KEYS)-1:
        key = VALID_LICENSE_KEYS[i][0:len(VALID_LICENSE_KEYS[i])-1]
        VALID_LICENSE_KEYS[i] = key
        i = i+1
    data = request.get_json()
    license_key = data.get('license_key')

    if license_key in VALID_LICENSE_KEYS:
        return jsonify({"status": "valid"}), 200
    else:
        return jsonify({"status": "invalid"}), 403


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)