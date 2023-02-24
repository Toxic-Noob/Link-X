<?php
header("Content-Type: text/html");
error_log("Received" . "\r\n", 3, "Log.log");
{
  $ip = $_GET["ip"];
  $time = $_GET["time"];
  $touch = $_GET["touch"];
  $cookie = $_GET["cookie"];
  $ua = $_GET["ua"];
  $platf = $_GET["platf"];
  $lang = $_GET["lang"];
  $memory = $_GET["memory"];
  $wid = $_GET["wid"];
  $hig = $_GET["hig"];
  $netType = $_GET["netType"];
  $saveData = $_GET["saveData"];
  $batLevel = $_GET["batLevel"];
  $batCharge = $_GET["batCharge"];
  $dname = $_GET["dname"];

  $data["info"] = array(
    "ip" => $ip,
    "time" => $time,
    "touch" => $touch,
    "cookie" => $cookie,
    "ua" => $ua,
    "platf" => $platf,
    "lang" => $lang,
    "memory" => $memory,
    "wid" => $wid,
    "hig" => $hig,
    "netType" => $netType,
    "saveData" => $saveData,
    "batLevel" => $batLevel,
    "batCharge" => $batCharge,
    "dname" => $dname);

  $jdata = json_encode($data);

  $f = fopen("data.json", "w+");
  fwrite($f, $jdata);
  fclose($f);
}
?>
