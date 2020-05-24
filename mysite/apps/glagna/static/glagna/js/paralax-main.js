$(window).scroll(function(){

	var st = $(this).scrollTop();

	$("#first-half").css({
		"transform": "translate(0%, "+ -st/10 +"%)",

	});

	$("#second-half").css({
		"transform": "translate(0%, "+ -st/13 +"%)",

	});

	$("#main-background").css({
		"transform": "translate(0%, "+ -st/32 +"%)",

	});


});