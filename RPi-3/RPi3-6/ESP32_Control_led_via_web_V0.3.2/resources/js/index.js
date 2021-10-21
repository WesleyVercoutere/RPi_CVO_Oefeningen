window.onload = (event) => {

    setInterval(function() {
        getLed();       
    }, 500);

}

function getLed() {

    var xhttp = new XMLHttpRequest();

	xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
            updateView(JSON.parse(this.responseText));
		}
	};
	xhttp.open("GET", "/get_led_info", true);
	xhttp.send();
}

function updateView(data) {
    console.log(data);

    element = document.getElementById('lightBulb');

    if (data.state) {
        element.src='images/light-bulb-on.jpg';
    }
    else {
        element.src='images/light-bulb-off.jpg';
    }
}

function btnClicked(route) {
    var xhttp = new XMLHttpRequest();

	xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 204) {
            getLed()
		}
	};
	xhttp.open("GET", route, true);
	xhttp.send();
}