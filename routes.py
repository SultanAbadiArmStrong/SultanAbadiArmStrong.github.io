from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
from app.models import User, Lahan

# Halaman Utama
@app.route('/')
def index():
    return render_template('index.html')

# Registrasi pengguna
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')  # 'petani' atau 'admin'

        # Periksa jika username sudah ada
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username sudah terdaftar!', 'danger')
            return redirect(url_for('register'))

        # Tambahkan pengguna baru
        new_user = User(username=username, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()
        flash('Registrasi berhasil!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

# Login pengguna
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Periksa kredensial pengguna
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            session['role'] = user.role
            flash('Login berhasil!', 'success')
            if user.role == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('petani_dashboard'))
        else:
            flash('Username atau password salah!', 'danger')

    return render_template('login.html')

# Logout pengguna
@app.route('/logout')
def logout():
    session.clear()
    flash('Logout berhasil!', 'success')
    return redirect(url_for('index'))

# Dashboard Petani
@app.route('/petani')
def petani_dashboard():
    if 'role' not in session or session['role'] != 'petani':
        flash('Akses tidak diizinkan!', 'danger')
        return redirect(url_for('login'))
    return render_template('petani_dashboard.html')

# Dashboard Admin
@app.route('/admin')
def admin_dashboard():
    if 'role' not in session or session['role'] != 'admin':
        flash('Akses tidak diizinkan!', 'danger')
        return redirect(url_for('login'))
    return render_template('admin_dashboard.html')

# Tambah Lahan dan Rekomendasi
@app.route('/add_lahan', methods=['POST'])
def add_lahan():
    if 'role' not in session or session['role'] != 'petani':
        flash('Akses tidak diizinkan!', 'danger')
        return redirect(url_for('login'))

    lokasi = request.form.get('lokasi')
    jenis_tanah = request.form.get('jenis_tanah')

    # Contoh logika rekomendasi sederhana
    if jenis_tanah.lower() == 'lempung':
        rekomendasi = 'Padi, Jagung'
    else:
        rekomendasi = 'Tanaman tidak tersedia'

    # Simpan data ke database
    new_lahan = Lahan(lokasi=lokasi, jenis_tanah=jenis_tanah, tanaman_rekomendasi=rekomendasi)
    db.session.add(new_lahan)
    db.session.commit()

    flash('Data lahan berhasil ditambahkan!', 'success')
    return redirect(url_for('petani_dashboard'))

# Lihat Semua Lahan (untuk petani atau admin)
@app.route('/list_lahan')
def list_lahan():
    if 'role' not in session:
        flash('Akses tidak diizinkan!', 'danger')
        return redirect(url_for('login'))

    lahan_list = Lahan.query.all()
    return render_template('list_lahan.html', lahan_list=lahan_list)