from flask import render_template, request, redirect, url_for, flash
from app import app

# Halaman Utama
@app.route('/')
def index():
    return render_template('index.html')

# Dashboard Petani
@app.route('/petani')
def petani_dashboard():
    return render_template('petani_dashboard.html')

# Dashboard Administrator
@app.route('/admin')
def admin_dashboard():
    return render_template('admin_dashboard.html')

# Fitur Rekomendasi Tanaman
@app.route('/rekomendasi', methods=['POST'])
def rekomendasi():
    lokasi = request.form.get('lokasi')
    jenis_tanah = request.form.get('jenis_tanah')
    # Contoh logika sederhana
    if jenis_tanah == 'Lempung' and lokasi == 'Dataran Rendah':
        rekomendasi = 'Padi, Jagung'
    else:
        rekomendasi = 'Tanaman Tidak Dikenali'
    return render_template('petani_dashboard.html', rekomendasi=rekomendasi)