$(document).ready(function(){

    setInterval(function() {update()}, 1000);

    var counter = 0;

    function update() {
        counter += 1;
        console.log(counter);
}
  
});

