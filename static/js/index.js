$(document).ready(function(){
	$("aside a").attr("onclick","test()")
});

function test(){
	$("section").html('<div class="dialog"><p>ytw</br>hello</div>')
};