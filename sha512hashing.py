from flask import Flask, request, render_template
import hashlib

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    response = None
    if request.method == 'POST':
        file = request.files['file']

        if file:
            file_data = file.read()  
            file_size = len(file_data)

            hash_value = calculate_sha512(file_data)

            response = {
                'file_name': file.filename,
                'file_size': file_size,
                'hash_value': hash_value
            }

    return render_template('index.html', response=response)

def calculate_sha512(file_data):
    sha512 = hashlib.sha512()
    sha512.update(file_data)
    return sha512.hexdigest()

if __name__ == '__main__':
    app.run(debug=True)
