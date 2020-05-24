$(document).ready(function(){

	function SwitcherLoginForm() {
		$("#login-btn-form").toggle("fade", 300);
		console.log()
	};

	$("#login-btn").on("click", function(){
		SwitcherLoginForm();
	});

	
});