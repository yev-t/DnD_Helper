$(document).ready(function(){

	$("#registration_button").click(function(){
		$('#log_in_form').hide();
		$('#registration_form').show();
	});

	$("#log_in_button").click(function(){
		$('#registration_form').hide();
		$('#log_in_form').show();
	});

});