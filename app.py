from flask import Flask, render_template, request, redirect
import os
import hashlib
import csv
from datetime import datetime

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Create uploads folder if it doesn't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# CSV file to store evidence
CSV_FILE = 'evidence.csv'

# Create CSV file with headers if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['File Name', 'Officer', 'Timestamp', 'SHA-256', 'MD5', 'SHA-1', 'SHA-512', 'BLAKE2b'])


# Home page
@app.route('/')
def index():
    return render_template('index.html')


# Upload route
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files.get('file')
    officer = request.form.get('officer', '').strip()

    if not file or not officer:
        return "Missing file or officer name!"

    # Save file to uploads folder
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Read file in binary and calculate hashes
    with open(filepath, 'rb') as f:
        data = f.read()
        hash_sha256 = hashlib.sha256(data).hexdigest()
        hash_md5 = hashlib.md5(data).hexdigest()
        hash_sha1 = hashlib.sha1(data).hexdigest()
        hash_sha512 = hashlib.sha512(data).hexdigest()
        hash_blake2b = hashlib.blake2b(data).hexdigest()

    # Append record to CSV (correct order)
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([
            file.filename,
            officer,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            hash_sha256,
            hash_md5,
            hash_sha1,
            hash_sha512,
            hash_blake2b
        ])

    return redirect('/view')


# View route
@app.route('/view')
def view():
    records = []
    with open(CSV_FILE, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # skip header
        for row in reader:
            if len(row) == 8:  # only valid rows
                records.append(row)
    return render_template('view.html', records=records)


if __name__ == '__main__':
    app.run(debug=True)
