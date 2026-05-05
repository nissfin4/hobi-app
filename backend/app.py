import os
from flask import Flask, jsonify, request
from flask_cors import CORS

# =====================================================
# INIT APP
# =====================================================
app = Flask(__name__)
CORS(app)

# =====================================================
# ENVIRONMENT VARIABLES (JANGAN DIUBAH / HARDCODE)
# =====================================================
nama_owner = os.environ.get('NAMA_PRAKTIKAN', 'Misterius')
nim_owner = os.environ.get('NIM_PRAKTIKAN', '00000000')

# =====================================================
# TEMA: KATALOG HOBI & MERCHANDISE
# =====================================================
katalog_data = {
    "judul_katalog": f"Katalog Hobi & Merchandise - {nama_owner}",
    "pemilik": nama_owner,
    "nim": nim_owner,
    "items": [
    "NCT 127 - Sticker (The 3rd Album)",
    "NCT DREAM - Hot Sauce (The 1st Album)",
    "NCT 2020 - Resonance Pt. 1",
    "NCT 2020 - Resonance Pt. 2",
    "WayV - Awaken The World (1st Album)",
    "NCT DREAM - Glitch Mode (2nd Album)",
    "NCT 127 - 2 Baddies (4th Album)"
]
}

# =====================================================
# ROUTE: GET INFO KATALOG
# =====================================================
@app.route('/api/info', methods=['GET'])
def get_info():
    return jsonify(katalog_data)

# =====================================================
# ROUTE: ADD ITEM KE KATALOG
# =====================================================
@app.route('/api/add-item', methods=['POST'])
def add_item():
    data = request.json
    new_item = data.get('item') if data else None

    if new_item:
        katalog_data["items"].append(new_item)
        return jsonify({
            "message": "Item berhasil ditambahkan!",
            "items": katalog_data["items"]
        }), 201

    return jsonify({
        "error": "Data tidak valid"
    }), 400

# =====================================================
# MAIN APP RUN
# =====================================================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)