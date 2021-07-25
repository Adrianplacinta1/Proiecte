window.onload=function(){

var logoutRequest = new XMLHttpRequest();
logoutRequest.open('POST', '/logoutRequest');
logoutRequest.setRequestHeader("Content-Type", "application/javascript");
logoutRequest.onload = function () {
    console.log(logoutRequest.responseText);
};
logoutRequest.send("GO");



var butoane = document.getElementsByClassName("nav-item");
butoane[2].addEventListener("click", function () {
    alert("Please log in first.");
});
butoane[3].addEventListener("click", function () {
    alert("Please log in first.");
});
butoane[4].addEventListener("click", function () {
    alert("Please log in first.");
});
butoane[5].addEventListener("click", function () {
    alert("Please log in first.");
});

butoane[6].addEventListener("click", function () {
    alert("Please log in first.");
});

};

