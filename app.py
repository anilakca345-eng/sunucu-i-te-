from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Sunucu aktif ve Emergent\'ı bekliyor!'

@app.route('/api/baslat', methods=['POST'])
def gorevi_baslat():
    veri = request.json
    return jsonify({
        "durum": "Basarili",
        "mesaj": "Emir alindi, otonom surec baslatiliyor!",
        "alinan_veri": veri
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
