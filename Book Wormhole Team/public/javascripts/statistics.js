//apelul de redirect daca userul nu e logat
window.onload = function () {
    var receiveduserID = document.cookie.toString();
    receiveduserID2 = receiveduserID.split('=')[1];
    console.log(receiveduserID2);
    var checkLogin = new XMLHttpRequest();
    checkLogin.open('POST', '/checkLogin');
    checkLogin.setRequestHeader("Content-Type", "application/javascript");
    checkLogin.onload = function () {
        console.log(checkLogin.responseText);
        var ok = checkLogin.responseText;
        console.log(ok);
        if (ok == 1);
        else {
            window.location.href = "/pages/login.html";
        }
    };

    checkLogin.send(receiveduserID2);
}



//apelul de logout
var logoutButton = document.getElementById("logoutButton");

logoutButton.onclick = function () {
    var receiveduserID = document.cookie.toString();
    var receiveduserID2 = receiveduserID.split('=')[1];
    console.log(receiveduserID2);
    var logoutRequest = new XMLHttpRequest();
    logoutRequest.open('POST', '/logoutRequest');
    logoutRequest.setRequestHeader("Content-Type", "application/javascript");
    logoutRequest.onload = function () {
        console.log(logoutRequest.responseText);
        var ok = logoutRequest.responseText;
        console.log(ok);
        if (ok == -1) {
            document.cookie.toString();
            receiveduserID2 = receiveduserID.split('=')[1];
            console.log(receiveduserID2);
            alert("Logout Successful");
            window.location.href = "/pages/index.html";
        }
        else {
            alert(ok);
            window.location.href = "/pages/index.html";
        }


    }
    logoutRequest.send(receiveduserID2.toString());
}