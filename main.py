from flask import Flask, request, render_template

app = Flask(__name__)
IP_FILE = 'ips.txt'

def load_ips():
    try:
        with open(IP_FILE, 'r') as file:
            return set(line.strip() for line in file)
    except FileNotFoundError:
        return set()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip = request.form['ip']
        ips = load_ips()
        if ip in ips:
            result = "Found"
        else:
            with open(IP_FILE, 'a') as file:
                file.write(f"{ip}\n")
            result = "Not Found"
        return render_template('index.html', result=result)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
