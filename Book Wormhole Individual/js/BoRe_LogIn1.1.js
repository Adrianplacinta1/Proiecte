var submitButton = document.getElementById("submitButton");

submitButton.onclick=function(){
    var userName=document.getElementById("userName");
    var userEmail=document.getElementById("userEmail");
    var userPassword=document.getElementById("userPassword");
    console.log(userName.value);
    console.log(userEmail.value);
    console.log(userPassword.value);

    var data =userName.value+'~'+userEmail.value+'~'+userPassword.value;

    var loginRequest = new XMLHttpRequest();
    loginRequest.open('POST', '/loginRequest');
    loginRequest.setRequestHeader("Content-Type", "application/javascript");
    loginRequest.onload=function(){
        console.log(loginRequest.responseText);
        var ok=loginRequest.responseText;
        if(ok>0){
            window.location.href="BoRe_home_LoggedIn1.1.html";
        }
        else{
            alert("User does not exist");
        }
       };
       
    loginRequest.send(data);
}