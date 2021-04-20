function doButtonClick(){
   // document.getElementById("plant").innerHTML = "House Plants!";
  // $.get("/text",getTextCallBack);
  $.get("/thing",getThingCallBack);

  // $('#plant').text("House Plants!:)");

}
function getTextCallBack(textString){
    $('#plant').text(textString);
    //alert("data "+textString);
}
function getThingCallBack(thing){
    $('#plant').text(thing['text']);
    $('#plant').css({'color': thing['color']});
}

function testPostCallBack(){
   // alert("this worked");
}

function testPostError(){
    alert("This did not work");
}

function saveInfo(){
    var text=$('#thingText').val();
    var color=$("#thingColor").val();
    var body = { "text": text, "color":color };
 

    $.ajax({
        type: "POST",
        url: "/testPost",
        data: JSON.stringify(body),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: testPostCallBack,
        failure: testPostError
    });
    
    
}