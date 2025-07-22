<?php session_start(); ?>
<!DOCTYPE html>
<html lang="ja" dir="ltr">
<head>
    <meta charset="utf-8">
    <title>Simple BBS</title>
    <link rel="stylesheet" href="bbs.css">
</head>
<body>

<?php

// include_once('ml.php');
include_once('myps.php');
$db = new mysqli('iis.edu.tama.ac.jp', $myid, $mypass, $mydb);

// ログインしていない場合の処理
if( empty($_SESSION['uid']) ) {
    echo '<p>書き込みたいなら <a href="login.php">ログインページ</a> へ。</p>';
} else {
    // // ログインしている場合の案内
    // echo '<p>' . htmlspecialchars($_SESSION['uid']) . ' さんでない場合は <a href="login.php">ログアウト</a> して。</p>';

}
// 書き込みフォーム
if( !empty($_SESSION['uid']) )
{
    echo <<<EOD
    <hr>
    <form action="" method="post">
        <input type="text" name="newpost" size="60">
        <input type="submit" name="submit" value="書き込み">
    </form>
    EOD;
}

// 投稿処理
if( !empty($_SESSION['uid']) && !empty($_POST['newpost']) )
{
    // 頑張ってインサート文を実行しよう。クエリはこんな感じ
    // insert into messages (uid, body) values (?,?)');
    $stmt = $db->prepare('INSERT INTO messages (uid, body) VALUES (?, ?)');
    $stmt->bind_param('ss', $_SESSION['uid'], $_POST['newpost']);
    $stmt->execute();
    $stmt->close();
}

// 投稿一覧表示（名前を取得する例も込み）
$res = $db->query('
    SELECT messages.body, users.name 
    FROM messages 
    LEFT JOIN users ON messages.uid = users.uid 
    ORDER BY messages.mid DESC
');

while( $mes = $res->fetch_assoc() )
{
    $name = isset($mes['name']) ? htmlspecialchars($mes['name']) : '（名前未登録）';
    $body = htmlspecialchars($mes['body']);
    echo "<div class='message'><strong>{$name}</strong>：{$body}</div>\n";
}

// // 書き込みフォーム
// if( !empty($_SESSION['uid']) )
// {
//     echo <<<EOD
//     <hr>
//     <form action="" method="post">
//         <input type="text" name="newpost" size="60">
//         <input type="submit" name="submit" value="書き込み">
//     </form>
//     EOD;
// }

?>

</body>
</html>
