$(document).ready(function(){

    setInterval(function() {update()}, 1000);

    var counter = 0;

    function update() {
        counter += 1;
        console.log(counter);
    }
    
});








$( "#ledOn" ).click(function() {
        
    // Fire off the request
    request = $.ajax({
        url: "/led_on",
        type: "get",
        // data: serializedData
    });

    // Callback handler that will be called on success
    request.done(function (response, textStatus, jqXHR){
        // Log a message to the console
        console.log("Hooray, it worked!");
        $("#lightBulb").attr("src","images/light-bulb-on.jpg");
    });

    // Callback handler that will be called on failure
    request.fail(function (jqXHR, textStatus, errorThrown){
        // Log the error to the console
        console.error(
            "The following error occurred: "+
            textStatus, errorThrown
        );
    });

    // Callback handler that will be called regardless
    // if the request failed or succeeded
    // request.always(function () {
        // Reenable the inputs
        // $inputs.prop("disabled", false);
    // });

});

$( "#ledOff" ).click(function() {
    alert( "Led Off" );
});