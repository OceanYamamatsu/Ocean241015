<!DOCTYPE html>
<html lang="ja" dir="ltr">
<head>
    <meta charset="utf-8">
    <title>メッセージ投稿</title>
</head>
<body>
<?php
ini_set('display_errors', "on"); // エラー表示（開発用）

require_once('myps.php'); // DB接続情報の読み込み
$db = new mysqli('iis.edu.tama.ac.jp', $myid, $mypass, $mydb); // DB接続

// DB接続チェック
if ($db->connect_error) {
    die("接続失敗: " . $db->connect_error);
}

// 自分の学籍番号（手動で指定）
$Puid = '22211379';

// フォームが送信されたとき
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $Pbody = $_POST['body']; // フォームから本文を取得

    // 入力チェック（空欄を防ぐ）
    if (trim($Pbody) === '') {
        echo "<p>本文が空です。入力してください。</p>";
    } else {
        // SQL準備・実行
        $sql = "INSERT INTO messages (uid, body) VALUES (?, ?)";
        $stmt = $db->prepare($sql);
        $stmt->bind_param("ss", $Puid, $Pbody);
        $stmt->execute();

        echo "<p>投稿が完了しました。</p>";
    }
}
?>

<!-- メッセージ投稿フォーム -->
<form action="" method="post">
    <label for="body">メッセージ本文：</label><br>
    <textarea name="body" id="body" rows="5" cols="50"></textarea><br>
    <button type="submit">投稿する</button>
</form>

<?php
$db->close(); // DB切断
?>
</body>
</html>
