const selected = document.querySelector(".selected");
const optionsContainer = document.querySelector(".options-container");
const optionsList = document.querySelectorAll(".option");
optionsContainer.style.display = "none";

selected.addEventListener("click", () => {
  optionsContainer.classList.toggle("active");
  optionsContainer.style.display = "initial";
});

optionsList.forEach(o => {
  o.addEventListener("click", () => {
    selected.innerHTML = o.querySelector("label").innerHTML + "<img src=\"../images/arrow-down.png\" alt=\"arrow\" class=\"arrow\">";
    optionsContainer.classList.remove("active");
    optionsContainer.style.display = "none";
  });
});

var i = true;
function read() {
  if (i == true) {
    document.getElementById("more").style.display = "inline";
    document.getElementById("dots").style.display = "none";
    document.getElementById("read-more-btn").innerHTML = "Read Less";
    i = false;
  }
  else {
    document.getElementById("read-more-btn").innerHTML = "Read More";
    document.getElementById("more").style.display = "none";
    document.getElementById("dots").style.display = "inline";
    i = true;
  }
};

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