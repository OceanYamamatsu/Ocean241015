<!DOCTYPE html>
<html lang="ja" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

<?php
  $simple_array = array(
    'lemon' => 'yellow',
    'apple' => 'red',
    'orange' => 'orange'
  );

  $double_array = array(
    'lemon' => array('color' => 'yellow', 'price' => 80, 'weight' => 20),
    'apple' => array('color' => 'red', 'price' => 150, 'weight' => 35),
    'orange' => array('color' => 'orange', 'price' => 120, 'weight' => 25)
  );

  print("<pre>");
  var_dump($simple_array);
  print("</pre><hr />");

  print("<pre>");
// $simple_array から、フルーツの名前と色のペアを取り出して表示すると……
  foreach ($simple_array as $key => $value) {
    print("$key $value\n");
  }
  print("</pre><hr />");

  print("<pre>");

// では、$double_array から、フルーツの名前と色と値段を取り出して表示しよう

  print("</pre><hr />");


 ?>

  </body>
</html>