<!DOCTYPE html>
<html lang="ja" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

<?php
  $array1 = array(
    'lemon'  => array('color'=>'yellow', 'price'=>  80, 'weight' => 20),
    'apple'  => array('color'=>'red'   , 'price'=> 150, 'weight' => 35),
    'orange' => array('color'=>'orange', 'price'=> 120, 'weight' => 25)
  );

  $array2 = array(
      array('name'=>'lemon' , 'color' => 'yellow', 'price' =>  80, 'weight' => 20),
      array('name'=>'apple' , 'color' => 'red'   , 'price' => 150, 'weight' => 35),
      array('name'=>'orange', 'color' => 'orange', 'price' => 120, 'weight' => 25)
  );

  print("<pre>");
  var_dump($array1);
  var_dump($array2);
  print("</pre><hr />");

  print("<pre>");
// $array1 から、フルーツの名前と色と値段を取り出して表示しよう
  print("</pre><hr />");

  print("<pre>");
// $array2 から、フルーツの名前と色と値段を取り出して表示しよう
  print("</pre><hr />");

 ?>

  </body>
</html>