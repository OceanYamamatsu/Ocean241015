<?php session_start(); ?>
<!-- 一番最初にsession_startする（これより先に何かを通信してはいけない） -->
<!DOCTYPE html>
<html lang="ja" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Sample 08-5</title>
    </head>
    <body>


<?php
//include_once('ml.php');//元文
require_once('myps.php');//取り出し
$db = new mysqli('iis.edu.tama.ac.jp', $myid, $mypass, $mydb);

if( !empty($_GET['clear']) && $_GET['clear']=='終了' )
    $_SESSION = array();
// crearボタンが押されるとセッションの中身を空に（廃棄）

if( !empty($_GET['id']) )
{
    $statement = $db->prepare('select name from fruits where id=?');
    if( $statement == false )
        print($db->error . '<hr />');

    $statement->bind_param('i', $_GET['id']);
    if( $statement->execute() === false )
        print($db->error . '<hr />');
    $res = $statement->get_result();

    $seikai = false;
    print('検索結果数 ' . $res->num_rows . '<br />' );

    if($res->num_rows == 1)
    {
        $d = $res->fetch_assoc();   //  あっても１個なのでループで回す必要なし
        if( $d['name'] == $_GET['name'] )
            $seikai = true;
    }


    if( $seikai )
    {
        print('正解！');
        $_SESSION['right']++;
        //アンダースコアセッション、セッション中は使用できる勝手にセッション変数を交換してくれる
    }
    else
    {
        print('ハズレ！');
        $_SESSION['wrong']++;
    }
    print('<hr />');
    print( $_SESSION['right']+$_SESSION['wrong'] . ' 問中 ' . $_SESSION['right'] . ' 問正解');

    $db->close();
}

 ?>


<form action='' method='get'>
    <input type="text" name="id" value="">
    <input type="text" name="name" value="">
    <input type="submit" name="submit" value="submit">

    <input type="submit" name="clear" value="終了">
    <!-- sample09-2のボタン、clearという名前を付けた -->
</form>

<?php
    var_dump($_SESSION)
    //よくデバッグで使用する
?>

</body>
</html>