<?php
if (isset($_POST['password'])) {
    $password = $_POST['password'];
    $hash = password_hash($password, PASSWORD_DEFAULT);
    echo "ハッシュ化したパスワード：<br>";
    echo htmlspecialchars($hash);
}
?>

<form method="post">
    パスワード: <input type="password" name="password" required>
    <input type="submit" value="ハッシュ化">
</form>
