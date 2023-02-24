<?php

if (!empty($_SERVER['HTTP_CLIENT_IP'])) {
  $ipaddress = $_SERVER['HTTP_CLIENT_IP']."\r\n";
} elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
  $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR']."\r\n";
} else
{
  $ipaddress = $_SERVER['REMOTE_ADDR']."\r\n";
}

if (@$_GET["echo"] == "true"){
  echo $ipaddress;
} else{
  $file = 'ip.txt';
  $fp = fopen($file, 'w');
  fwrite($fp, $ipaddress);
  fclose($fp);
}