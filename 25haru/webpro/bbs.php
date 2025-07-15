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

include_once('ml.php');
$db = new mysqli('iis.edu.tama.ac.jp', $myid, $mypass, $mydb);

if( !empty($_SESSION['uid']) )
{
    // よくある「〜さんでない場合はログインページへ」を表示しよう
}

if( empty($_SESSION['uid']) )
{
    // 「書き込みたいならログインページへ」を表示しよう
}

if( !empty($_SESSION['uid']) && !empty($_POST['newpost']) )
{
    // 頑張ってインサート文を実行しよう。クエリはこんな感じ
    // insert into messages (uid, body) values (?,?)');
}

// 「全部取ってくる」系は、インジェクションに気を使わなくてよいので、単純に query を呼ぶ。
// いける人は、頑張って「名前」を取ってこよう
$res = mysqli_query($db, 'select * from messages');
while( $mes = mysqli_fetch_assoc($res) )
{
    // 適宜整形
    print($mes['body']);
}

// ログインしているなら書き込みＯＫ！
if( !empty($_SESSION['uid']) )
{
    print('<hr><form acton="" method="post"><input type="text" name="newpost" size=60><input type="submit" name="submit" value="書き込み"></form>');
}

?>