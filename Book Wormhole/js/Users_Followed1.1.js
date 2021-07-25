var searchButton = document.getElementById("searchButton");
var results = document.getElementById("results");

window.onload = function () {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/getUsersFollowed");
    xmlhttp.onload = function () {
        var usersFollowed = document.getElementById("usersFollowed");
        usersFollowed.innerHTML = '';
        var receivedUsers = JSON.parse(xmlhttp.responseText);
        var htmlString = '';
        for (i = 0; i < receivedUsers.length; i++) {
            htmlString += '<div class="usersFound">';
            htmlString += '<img src="' + receivedUsers[i].userPhoto + '">';
            htmlString += '<p class="hiddenID">' + receivedUsers[i].userID + '</p>';
            htmlString += '<p class="text">' + receivedUsers[i].userName + '</p>';
            htmlString += '<p><button class="viewUserButton">View User</button></p></div>';
        }
        usersFollowed.innerHTML = htmlString;

    };
    xmlhttp.send("1");
}

searchButton.onclick = function () {                                        //cand dam click la Search
    var userName = document.getElementById("typeUserName");                  //preluam ce a scris userul
    console.log(userName.value);


    var findUserRequest = new XMLHttpRequest();                        //facem un request
    findUserRequest.open('POST', '/findUserRequest');
    findUserRequest.setRequestHeader("Content-Type", "application/javascript");
    findUserRequest.onload = function () {
        console.log(findUserRequest.responseText);
        results.innerHTML = '';
        results.innerHTML = findUserRequest.responseText;
        results.style.display = "flex";
    };

    findUserRequest.send(userName.value);    //trimitem doar ce a scris userul, nu e nevoie de obiect, JSON, etc


}

window.onclick = function (event) {
    if (event.target.matches(".viewUserButton")) {
        var userButton = event.target;
        var parinte = userButton.parentNode.parentNode;
        var userID = parinte.children[1];            //preluam ID-ul userului, care e hidden
        userID2 = userID.innerText;
        var sendUserID = new XMLHttpRequest();                        //facem un request
        sendUserID.open('POST', '/sendUserID');
        sendUserID.setRequestHeader("Content-Type", "application/javascript");
        sendUserID.onload = function () {
            if (sendUserID.responseText == "OK")
                window.location.href = "My_Account1.1.html";
        };

        sendUserID.send(userID2.toString());
    }
}

