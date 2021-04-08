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