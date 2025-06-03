<!DOCTYPE html>
<html lang="ja" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

<?php
  $accounts = array(
  //[0番、１番、２番、]
    [1001, 'tama01', '多摩太郎'],
    [1002, 'naga02', '永山進'],
    [1003, 'seiseki', '聖花子']
  );

  print("<pre>");
  var_dump($accounts);
  print("</pre><hr />");

  // いったん入力は忘れて、$accounts 配列から一つ一つ要素を取り出して、
  // その０番目と１番目を表示しよう。
  // キーはまったく指定されていないので、すべて０番からの数字で呼ばれることに注意

 ?>

  </body>
</html>