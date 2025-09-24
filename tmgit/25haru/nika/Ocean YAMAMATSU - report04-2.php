
<?php
  $fruits = array (
	'apple' => 'red',
	'orange' => 'orange',
	'lemon' => 'yellow'
  );
 ?>

<hr>

<p>現在の $fruits 配列の中身</p>
<?php
  var_dump($fruits);
 ?>

<p>回答プログラム</p>
<table>
<tr><th>フルーツ</th><th>色</th></tr>
<?php
foreach($fruits as $k => $v)
{
	print("<tr><td>$k</td><td>$v</td></tr>\n");
}
?>