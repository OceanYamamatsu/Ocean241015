<?php
session_start();
?>

<!DOCTYPE html>
<html lang="ja" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Sample 08-0</title>
    </head>
    <body>

<?php
ini_set('display_errors',"on");//error表示（本番では表示すべきでない）
require_once('myps.php');//取り出し
$db = new mysqli('iis.edu.tama.ac.jp', $myid, $mypass, $mydb);//開き
// write my code here↓--------------------------------------------------------------

$Puid = '22211379';//ホルダ１
$Pbody = '何とかホルダー完全に理解した２';//ホルダ２
$sql = ("insert into messages (uid,body) values (?,?)");//sql草案？

$stmt = $db->prepare($sql);//sql準備
$stmt->bind_param("ss", $Puid, $Pbody);//準備したsqlに値を挿入（合成）
$stmt->execute();//sql実行

//----------------------------------------------------------------------------------
echo 'Ok';//止まらなかったら出る
$db->close();//締め
?>
    </body>
</html>