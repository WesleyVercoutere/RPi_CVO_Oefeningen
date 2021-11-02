window.onload = (event) => {

    var ledsLoaded = false;
    var btnsLoaded = false;

    loadLeds(function(){ledsLoaded = true});
    loadButtons(function(){btnsLoaded = true});

    // setInterval(function() {
    //     if (ledsLoaded && btnsLoaded) {
    //         getLeds();
    //     }      
    // }, 500);

}

function loadLeds(cb) {
    var xhttp = new XMLHttpRequest();

	xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 200) {
            renderLeds(JSON.parse(this.responseText));
            cb();
		}
	};
	xhttp.open("GET", "/get_led_info", true);
	xhttp.send();
}

function loadButtons(cb) {
    console.log("Load btns and render in view")
    cb();
}

function renderLeds(data) {
    var element = document.getElementById("leds");
    var html = "";

    html += "<div class='row'>";

    data.forEach(el => {
        
        var color = "primary";
        
        switch(el.color) {
            
            case "Red":
                color = "danger";
                break;
            
            case "Green":
                color = "success";
                break;

            case "Blue":
                color = "primary";
                break;

            case "Yellow":
                color = "warning";
                break;
        };

        html += `
            <div class="col-md-6 col-lg-3">
                <div class="text-center">
                    <h2>Led ${el.color}</h2>
                    <p>pin number: ${el.pin_nr}</p>
                </div>

                <div class="text-center">
                    <image id="lightBulb${el.id}" src="images/light-bulb-off.jpg">
                </div>
                
                <div class="row my-3">
                    <div class="col-6 text-center"><button id="ledOn" onclick=btnClicked("/led_on/${el.id}") type="button" class="btn btn-${color}">Led On</button></div>
                    <div class="col-6 text-center"><button id="ledOff" onclick=btnClicked("/led_off/${el.id}") type="button" class="btn btn-outline-${color}">Led Off</button></div>
                </div>
            
            </div>
        `
    });

    html += "</div>";

    element.innerHTML = html;
}

function getLeds() {

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
    var elementPrefix = 'lightBulb';

    data.forEach(el => {
        var elementName = elementPrefix + el.id;
        var element = document.getElementById(elementName);

        if (el.state) {
            element.src='images/light-bulb-on.jpg';
        }
        else {
            element.src='images/light-bulb-off.jpg';
        }

    });
}

function btnClicked(route) {
    var xhttp = new XMLHttpRequest();

	xhttp.onreadystatechange = function() {
	    if (this.readyState == 4 && this.status == 204) {
            getLeds();
		}
	};
	xhttp.open("GET", route, true);
	xhttp.send();
}