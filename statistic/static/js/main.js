function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

var csrftoken = getCookie('csrftoken');

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).ready(function(){
    console.log('bbb');
    

    $.ajax({
        url: '/get_client_info/',
        cache: 'false',
        dataType: 'json',
        type: 'POST',
        // data: data,
        success: function(data) {
            console.log(data);

            shop_string = '';
            shops = data.result.shops;
            for (key in shops){
                shop_string = shop_string + '<li class="list-group-item">'+shops[key]+'</li>';
            }
        
            $('#main').append('<div class="row">'+
                '<div class="col-12">'+
                '<h3>Мої магазини</h3>'+
                '</div>'+
                '<div class="col-6">'+
                    '<ul class="list-group">'+shop_string+
                    '</ul>'+
                '</div>'+
                
            '</div>');

        },
        error: function(error) {}
      });
});