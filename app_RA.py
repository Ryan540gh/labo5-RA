from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # Remplacer IP_DE_LA_MACHINE_ICI par l'adresse IPv4 de la machine (commande ipconfig)
    return '<h2>Hello, World! From RA: 192.168.76.171</h2>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)