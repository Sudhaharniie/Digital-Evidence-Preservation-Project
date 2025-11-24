📁 Digital Evidence Integrity Verification System

A Flask-based application for secure file hashing and integrity validation using Python and hashlib.

🔎 Project Overview

This project demonstrates a practical approach to preserving the integrity of digital evidence using cryptographic hashing.
It is a web-based system built with Flask, where users can upload files to:

Generate cryptographic hash values

Store or note down the hash values as proof of authenticity

Re-verify files at any time to detect tampering or unauthorized modifications

This workflow closely aligns with real-world digital forensics, cybercrime investigation, and chain-of-custody preservation.

⭐ Key Features

Secure File Uploading

Automatic Hash Generation using hashlib

Supports multiple algorithms: MD5, SHA-1, SHA-256, SHA-512

File Integrity Verification (re-upload and compare)

Simple and clean Flask web interface

Demonstrates core concepts in evidence preservation & validation

🛠️ Technology Stack
Component	Technology
Backend	Python 3.x
Framework	Flask
Hashing Engine	Python hashlib
Frontend	HTML, CSS (optional styling)
Storage	Local file system
📂 Project Structure
Digital-Evidence-Integrity-System/
│
├── app.py                 # Main Flask application
│
├── templates/             # HTML templates
│   ├── index.html         # Main upload & hash page
│   └── verify.html        # Verification result page
│
├── static/
│   └── styles.css         # Optional custom styles
│
└── uploads/               # Temporary file storage

🚀 How to Run the Application
1. Install Required Dependencies
pip install flask

2. Start the Flask Server
python app.py

3. Open the Web App

Visit:

➡️ http://127.0.0.1:5000

🔐 How It Works
1. File Upload

A file is uploaded through the web interface and temporarily stored.

2. Hash Calculation

The file’s bytes are passed to Python’s hashlib, which generates a unique hash:

hashlib.sha256(file_data).hexdigest()

3. Integrity Verification

When the same (or another) file is uploaded again:

The system recalculates its hash

Compares it with the original

Determines whether the file has been altered or remains authentic

Result

✔ Matching Hash → File is genuine

❌ Different Hash → File has been modified

🧪 Applications in Digital Forensics

This project demonstrates essential forensic principles:

Evidence authenticity verification

Detecting data tampering

Maintaining chain of custody

Using hashing algorithms for validation

Understanding how forensic tools validate integrity

It closely mirrors what tools like FTK Imager, EnCase, and Autopsy do internally.
