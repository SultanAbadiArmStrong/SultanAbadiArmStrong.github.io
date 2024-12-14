<?php
// Database Connection
$conn = new mysqli("localhost", "root", "", "pertanian_db");
if ($conn->connect_error) {
    die("Koneksi gagal: " . $conn->connect_error);
}

// User Session
session_start();

// Handle User Registration
if (isset($_POST['register'])) {
    $username = $_POST['username'];
    $password = password_hash($_POST['password'], PASSWORD_BCRYPT);
    $role = $_POST['role'];
    $conn->query("INSERT INTO users (username, password, role) VALUES ('$username', '$password', '$role')");
    echo "Registrasi berhasil!";
}

// Handle User Login
if (isset($_POST['login'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    $result = $conn->query("SELECT * FROM users WHERE username='$username'");
    if ($result->num_rows > 0) {
        $user = $result->fetch_assoc();
        if (password_verify($password, $user['password'])) {
            $_SESSION['username'] = $user['username'];
            $_SESSION['role'] = $user['role'];
            header("Location: index.php");
        } else {
            echo "Password salah!";
        }
    } else {
        echo "Pengguna tidak ditemukan!";
    }
}

// Logout
if (isset($_GET['logout'])) {
    session_destroy();
    header("Location: index.php");
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistem Informasi Potensi Pertanian</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 0; }
        .container { width: 80%; margin: 20px auto; }
        .nav { background: #28a745; padding: 10px; color: white; text-align: center; }
        .nav a { color: white; margin: 0 10px; text-decoration: none; }
    </style>
</head>
<body>
    <div class="nav">
        <h1>Sistem Informasi Potensi Pertanian</h1>
        <?php if (isset($_SESSION['username'])): ?>
            <a href="?logout=1">Logout</a>
        <?php endif; ?>
    </div>
    <div class="container">
        <?php if (!isset($_SESSION['username'])): ?>
            <h2>Login</h2>
            <form method="post">
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit" name="login">Login</button>
            </form>
            <h2>Registrasi</h2>
            <form method="post">
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <select name="role" required>
                    <option value="petani">Petani</option>
                    <option value="admin">Admin</option>
                </select>
                <button type="submit" name="register">Register</button>
            </form>
        <?php else: ?>
            <h2>Selamat datang, <?= $_SESSION['username']; ?> (<?= $_SESSION['role']; ?>)</h2>
            <?php if ($_SESSION['role'] == 'admin'): ?>
                <h3>Menu Admin</h3>
                <p><a href="?manage_users=1">Kelola Pengguna</a></p>
            <?php else: ?>
                <h3>Menu Petani</h3>
                <p><a href="?input_lahan=1">Input Lahan</a></p>
                <p><a href="?lihat_informasi=1">Lihat Informasi Pertanian</a></p>
            <?php endif; ?>
        <?php endif; ?>
    </div>
</body>
</html>