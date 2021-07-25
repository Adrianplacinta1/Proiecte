var vectorGenres = ["Art", "Comics", "Cookbooks", "Crime", "Fiction", "Graphic", "Novels", "Horror", "Comedy", "Manga", "Mystery", "Psychology", "Science", "Fiction", "Suspense", "Thriller", "Biography", "Business", "Childrens", "Classics", "Contemporary", "Ebooks", "Fantasy", "Historical", "Fiction", "History", "Memoir", "Nonfiction", "Paranormal", "Philosophy", "Poetry", "Religion", "Romance", "Science", "Spirituality", "Sports", "Travel"];


var genres = document.getElementById("genres");
console.log(genres);
vectorGenres.forEach(genre => {

  var label = document.createElement("label");
  label.htmlFor = genre;
  label.textContent = genre;
  label.className = "genres-label"
  var input = document.createElement("input");
  input.type = "checkbox";
  input.id = genre;
  input.className = "genre-check";

  var genreItem = document.createElement("div");
  genreItem.className = "genre-item";

  genreItem.appendChild(input);
  genreItem.appendChild(label);
  genres.appendChild(genreItem);

});

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


//requestul de logout
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