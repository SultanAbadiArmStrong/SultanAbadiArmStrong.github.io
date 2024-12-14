from app import db

# Model untuk Tabel Pengguna
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # 'petani' atau 'admin'

    def __repr__(self):
        return f'<User {self.username}>'

# Model untuk Tabel Lahan
class Lahan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lokasi = db.Column(db.String(100), nullable=False)
    jenis_tanah = db.Column(db.String(50), nullable=False)
    tanaman_rekomendasi = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f'<Lahan {self.lokasi}>'