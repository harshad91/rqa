$(document).ready(function () {
    $(".submit").click(function (e) {
    	e.preventDefault();
    	var csrftoken = getCookie('csrftoken');
    	var qid = this.id.split('-')[1];
    	var aid = '#id_a-' + qid.toString();
    	var ans = $(aid).val();
    	if (ans.length > 0) {
    		$.ajax(
    			{
    				url : window.location.href,
    				type: "POST",
    				data: {
    						csrfmiddlewaretoken: csrftoken,
    						q: qid,
    						answer: ans,
    					},
    				success: function(json){
    					$('#suba-'+qid).html(json.ans);
    					$(aid).hide();
    				},
    				error: function(xhr, errmsg, err){
    					console.log(xhr.status + ": "+ xhr.responseText);
    				}
    			}
    		);
    	}
    });

    $(".edit").click(function (e) {
    	var qid = this.id.split('-')[1];
    	var aid = '#id_a-' + qid.toString();
    	$(aid).show()
    });
});

//For getting CSRF token
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie != '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
		}
	}
 return cookieValue;
}