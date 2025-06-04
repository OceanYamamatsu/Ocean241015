<html>
  <head>
    <title>PHP Test</title>
  </head>
  <body>

<h1>第６レポート（２重配列）</h1>
<p>$members 配列の内容を表形式で出力するような PHP プログラムを作成しなさい</p>

<?php
  $members = array (
		array('id'=>'1001', 'name'=>'SATO'),
		array('id'=>'1002', 'name'=>'SUZUKI'),
		array('id'=>'1003', 'name'=>'TAKAHASHI'),
		array('id'=>'1004', 'name'=>'TANAKA'),
		array('id'=>'1005', 'name'=>'WATANABE')
	);
 ?>

<hr>

<p>$members 配列の中身</p>

<?php
  var_dump($members);
 ?>

<hr>

<p>ヒント１：$members 配列から一つずつ取り出すと、取り出した「値($value)」が配列。</P>

<?php
  foreach ($members as $key => $value) {
  	var_dump($value);
		print("<hr>");
  }
 ?>

 <hr>

 <p>ヒント２：$members 配列から一つ取り出した「値($value)」が配列なので、ここで id と name のキーに対応する値を探すことができる</p>

 <?php
   foreach ($members as $key => $value) {
			var_dump($value['id']);
			var_dump($value['name']);
			print("<br>");
			print("<hr>");
   }
  ?>

	</body>
</html>

<hr>
<p>完成版：$members 配列の内容を表形式で表示</p>

<table border="1">
  <tr>
    <th>ID</th>
    <th>名前</th>
  </tr>
<?php
  foreach ($members as $value) {
    print("<tr>");
    print("<td>{$value['id']}</td>");
    print("<td>{$value['name']}</td>");
    print("</tr>");
  }
?>
</table>