function go_slider(){
	window.timerId = window.setInterval(timer, 3000);
}
function timer(){
				if(window.number == undefined || window.number == 3) {//картинки от 1 до 10
					window.number = 1;
				} else window.number = window.number + 1;
				var img = document.getElementById('img');
				var partOfSrc1="{% static \u0027img/slide_\u0027";
				var partOfSrc2="\u0027.jpg\u0027 %}";
				img.src ="\u0022{% static 'img/slide_'"+window.number+"'.jpg'%}\u0022";
}

function for_register_form() {
    var name = document.getElementById('id_username');
    name.classList.add("form-control");
}