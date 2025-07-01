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

// write my code here↓
//----------------------------------------------------------------------------------

$res = $db->query('select * from fruits');

while( $d = $res->fetch_assoc() )
{
  var_dump($d);
}

//----------------------------------------------------------------------------------
$db->close();//締め
?>
    </body>
</html>

<!-- $db->query('insert into messages (uid,body) values (22211379,'腹痛が痛い');') -->