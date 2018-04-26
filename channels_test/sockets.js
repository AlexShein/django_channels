socket = new WebSocket("ws://127.0.0.1:8000/ws/test/");
socket.onmessage = function(e) {
    alert(e.data);
}
socket.onopen = function() {
    socket.send(JSON.stringify({'message':'2'}));
}


socket.send(JSON.stringify({'message':'3456'}));

socket.close(1000)
