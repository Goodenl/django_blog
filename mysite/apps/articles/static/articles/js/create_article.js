$(document).ready(function(){

	$('#draft-btn').on('click', function(){

		if($('input[type="checkbox"]').prop("checked")){

			$('#uncheck').css("opacity", "0");
			$('#check').css("opacity", "100%");

		}else{

			$('#uncheck').css("opacity", "100%");
			$('#check').css("opacity", "0");
		};
	});

	$("#return-btn").mousemove(function(){
		$(this).css("opacity", "100");
	});

	$("#draft-btn").mousemove(function(){
		$(this).css("opacity", "100");
	});

	$("#create-title-article, #create-tags-article").mousemove(function(){
		$("#return-btn").css("opacity", "100");
		$("#draft-btn").css("opacity", "100");
	});

	$("#create-text-article").mousemove(function(){
		$("#return-btn").css("opacity", "0");
		$("#draft-btn").css("opacity", "0");
	});
	
})