function isEmptyObject(obj) {
    for (var i in obj) {
        if (obj.hasOwnProperty(i)) {
            return false;
        }
    }
    return true;
}


function send_code(){
  var img_value = document.getElementById("img_value").value;
  var code_value = document.getElementById("code_value").value;

  var ip = location.host;



  var socket= new WebSocket("ws://" + ip + "/ws");
  var sendJson = {
    'img' : img_value,
    'code' : code_value
  }
  

  var wsSend = function(data) {
    if(!socket.readyState){
        setTimeout(function (){
            wsSend(data);
        },100);
    }else{
        socket.send(data);
    }
  };
  console.log(sendJson);
  wsSend(JSON.stringify(sendJson));

  x = ""


  socket.onmessage = function (e) {
  json = JSON.parse(e.data);
  
  console.log(json.next_page);
  console.log(json);
  if(json.Ok == "Valid"){
        window.location.href = json.next_page;
   }


    
};


}
