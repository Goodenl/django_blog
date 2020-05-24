$(document).ready(function(){
	var sliderbar_hover_posX = 50;
		sliderbar_unhover_posX = 250;

	$("#left-sidebar").hide();
	$("#comment-box").hide();


	$(document).mousemove(function( event ) {
		
		if (event.pageX <= sliderbar_hover_posX) {
			$("#left-sidebar").css("left", "0");
			$("#left-sidebar").show("drop", 400);
		}else if (event.pageX >= sliderbar_unhover_posX) {
			$("#left-sidebar").hide("drop", 200);
		}

	});

	$("#comment-hover-space").mousemove(function(){
		$("#comment-hover-space").hide("fade", 200);
		$("#comment-box").show("fade", 600);
	});

	$("#return-btn").mousemove(function(){
		$("#return-btn").css("opacity", "100");
	});

	$("#article-btn").mousemove(function(){
		$("#article-btn").css("opacity", "100");
	});

	$("#title-article").mousemove(function(){
		$("#return-btn").css("opacity", "100");
		$("#article-btn").css("opacity", "100");
	});

	$("#text-title").mousemove(function(){
		$("#return-btn").css("opacity", "0");
		$("#article-btn").css("opacity", "0");
	});

})