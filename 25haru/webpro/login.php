<?php session_start(); ?>
<!DOCTYPE html>
<html lang="ja" dir="ltr">
    <head>
        <meta charset="utf-8">
        <title>Login</title>
    </head>
    <body>


<?php

//include_once('ml.php');
include_once('myps.php');
$db = new mysqli('iis.edu.tama.ac.jp', $myid, $mypass, $mydb);

// password_hash('password')

// POST で呼ばれた＝ログインボタンが押された
if( !empty($_POST['uid']) )
{
    // ひとまずログインは失敗するものと仮定する
    $login = false;

    // 「uid を条件に users テーブルからその人のパスワードを持ってくる」SQL を prepare する
    // ???????? の部分の SQL を書いてみよう
    //$statement = $db->prepare( ???????? );
    $statement = $db->prepare( 'select password from users where uid =?' );
    $statement->bind_param('s', $_POST['uid']);

    // データベースエラーが起きたら表示
    if( $statement->execute() === false )
        print($db->error . '<hr />');
    else
    {
        $res = $statement->get_result();
        // 結果が１件だけ存在したら、パスワードを入力値と比較
        if( $res->num_rows == 1 )
        {
            $d = $res->fetch_assoc();   //  １個なのでループで回す必要なし
            // 「データベースから取ってきたパスワードと、入力されたパスワードが一致するならば」
            // と ???????? の中に書こう
            // if(????????)
            //if( $_POST['password']===$d['password'] )//'='二つでもよい
            if( $_POST['password'] === $d['password'] )
            //if(password_verify ( $_post['password'],$b['password'] ) )//ハッシュのほう,そもそもusersにハッシュのpassが入っているときに有用
                // ログイン成功
                $login = true;// ログイン成功にする
        }
    }

    // ログイン成功なら、SESSION 変数に、送られてきたユーザ ID を保存しておこう
    if( $login )
    {
        // 「セッション変数に、ユーザ ID を保存」と書きたい。
        // ？？？？？？？？
        $_SESSION['uid']=$_POST['uid'];
        print('Welcome ' . $_SESSION['uid']);
    }
    // 失敗なら、エラー表示
    else {
        print("Password Error<br />\n");
    }
    $db->close();
}

 ?>


<form action='' method='post'>
    <input type="text" name="uid" value="">
    <input type="password" name="password" value="">
    <input type="submit" name="LOGIN" value="submit">
</form>


</body>
</html>