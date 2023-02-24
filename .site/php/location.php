<?php
header('Content-Type: text/html');
error_log("Received" . "\r\n", 3, "Log.log");
{
  $lat = $_GET['Lat'];
  $lon = $_GET['Lon'];
  $acc = $_GET['Acc'];
  $alt = $_GET['Alt'];
  $dir = $_GET['Dir'];
  $spd = $_GET['Spd'];

  $data['info'] = array(
    'lat' => $lat,
    'lon' => $lon,
    'acc' => $acc,
    'alt' => $alt,
    'dir' => $dir,
    'spd' => $spd);

  $jdata = json_encode($data);

  $f = fopen('data.json', 'w+');
  fwrite($f, $jdata);
  fclose($f);
}
?>
