# main.py

from flask import Blueprint, render_template, request, send_from_directory, make_response, send_file, jsonify
from flask_login import login_required, current_user
from cryptosteganography import CryptoSteganography
import secrets, string
import os
# import requests

# uploads_dir = os.path.join(os.getcwd(), './app/images')
# os.makedirs(uploads_dir, exists_ok=True)

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)

@main.route('/encrypt')
@login_required
def encrypt():
    return render_template('encrypt.html')

@main.route('/decrypt')
@login_required
def decrypt():
    return render_template('decrypt.html')

@main.route('/success', methods = ['POST'])
@login_required
def success():
    if request.method == 'POST':  
        f = request.files['file'] 
        filename = "encrypt.png"
        f.save(f.filename)
        secret = request.form['secret']
        message = request.form['message']
        crypto_steganography = CryptoSteganography(secret)  
        crypto_steganography.hide(f.filename, filename, message)
        return send_file("../"+filename, as_attachment=True)

@main.route('/decryptsuccess', methods = ['POST'])
@login_required
def decryptsuccess():
    if request.method == 'POST':  
        f = request.files['file']
        f.save("decrypt")
        secret = request.form['secret']
        crypto_steganography = CryptoSteganography(secret)  
        decryptsecret = crypto_steganography.retrieve("decrypt")
        return render_template("decryptsuccess.html", name = decryptsecret)

@main.route('/<imgid>', methods = ['GET', 'POST'])
def get_image(imgid="encrypt.png"):
    print(imgid)
    return send_file("../"+ imgid, as_attachment=True)
