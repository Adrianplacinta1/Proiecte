var submitButton=document.getElementById("submit-button");

submitButton.onclick=function(){
    var userEmail=document.getElementById("email");
    var userPassword=document.getElementById("password");
    console.log(userEmail.value);
    console.log(userPassword.value);

    var data ={
        email : userEmail.value,
        password : userPassword.value
    };
    var stringify=JSON.stringify(data);
    data=stringify;

    var loginRequest = new XMLHttpRequest();
    loginRequest.open('POST', '/loginRequest');
    loginRequest.setRequestHeader("Content-Type", "application/javascript");
    loginRequest.onload=function(){
        console.log(loginRequest.responseText);
        var ok=loginRequest.responseText;
        if(ok>0){
            console.log(document.cookie.toString());
            var receiveduserID=document.cookie.toString();
            receiveduserID2=receiveduserID.split('=')[1];
            console.log(receiveduserID2);
            window.location.href="/pages/recomandations.html";
        }
        else{
            alert("User does not exist");
        }
       };
       
    loginRequest.send(data);
}