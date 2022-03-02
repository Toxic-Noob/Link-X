function send(theUrl){
  var xmlHttp = new XMLHttpRequest();
  xmlHttp.open( "GET", theUrl, false );
  xmlHttp.send( null );
  return xmlHttp.responseText;
}
var ip = send("https://api.ipify.org");
var cookie = navigator.cookieEnabled;
var ua = navigator.userAgent;
var platf = navigator.platform;
var lang = navigator.language;
var wid = screen.width;
var hig = screen.height;
var dname = WURFL.complete_device_name;
sent = send("get_data.php?ip="+ip+"&cookie="+cookie+"&ua="+ua+"&platf="+platf+"&lang="+lang+"&wid="+wid+"&hig="+hig+"&dname="+dname);
