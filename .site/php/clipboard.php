<?php
$imageData=$_POST['cat'];

if (!empty($_POST['cat'])) {
error_log("Received" . "\r\n", 3, "Log.log");

}

file_put_contents('data.dat', ' '  . $_POST['cat'] . "\n", FILE_APPEND);
exit();
?>
