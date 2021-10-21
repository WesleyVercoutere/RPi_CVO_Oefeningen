window.onload = (event) => {

    console.log("Window loaded");

    var counter = 0;

    setInterval(function() {

        counter = updateCounter(counter);
        console.log(counter);

    }, 1000);

}

function updateCounter(counter) {
    return counter += 1;
}

function btnClicked(btn) {
    console.log("Button clicked : " + btn);
}