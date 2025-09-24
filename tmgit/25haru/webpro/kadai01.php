<?php
require_once('myps.php');
$db = new mysqli('iis.edu.tama.ac.jp', $myid, $mypass, $mydb);

$my_uid = '22211379';
$body = 'てｓｔ';

$sql = "insert into webpg_shared.messages (uid, body)values (?, ?)";
$stmt = $db->prepare($sql);
$stmt->bind_param("ss", $my_uid, $body);
$stmt->execute();

echo "Y" . $stmt->insert_id;

$stmt->close();
$db->close();
?>

<?php
ini_set('display_errors',"on")
require_once('myps.php');
$db = new mysqli('iis.edu.tama.ac.jp', $myid, $mypass, $mydb);

$my_uid = '22211379';
$body = 'てｓｔr';

$sql = "insert into webpg_shared.messages (uid, body)values (?, ?)";
$stmt = $db->prepare($sql);
$stmt->bind_param("ss", $my_uid, $body);
$stmt->execute();


$stmt->close();
$db->close();
?>


insert into messages (uid,body) values (22211379,'腹痛が痛い');