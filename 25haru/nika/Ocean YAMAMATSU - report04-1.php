
<?php

$maxCount = 0;
$maxValue = 0;
$count = 0;

for($i = 1; $i <= 1000; $i++) {
    $x = $i;
    while ($x != 1) {
        if ($x % 2 == 1) {
            $x = $x + 1;
        } 
        else {
            $x = $x / 2;
        }
        $count++;
    }
    print("$i について $count 回まわりました<br>\n");
    if ($count > $maxCount) {
        $maxCount = $count;
        $maxValue = $i;
    }
    $count = 0;
}
print("<hr>\n");
print("繰り返し回数が最大なのは $maxValue で、$maxCount 回まわりました。<br>\n");

?>
