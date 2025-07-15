| 空欄                  | 内容                                           |
| ------------------- | -------------------------------------------- |
| `????????`（prepare） | `"SELECT password FROM users WHERE uid = ?"` |
| `????????`（if 文）    | `$_POST['password'] === $d['password']`      |
| `？？？？？？？？`          | `$_SESSION['uid'] = $_POST['uid'];`          |
"SELECT password FROM users WHERE uid = ?"
"select password from users where uid =?"

`$_POST['password'] === $d['password']`
$_post['password'] == $d['password']

$_SESSION['uid'] = $_POST['uid'];

$_session['uid'] = $_post['uid'];