var submitButton = document.getElementById("submitButton");

submitButton.onclick = function () {
    var userName = document.getElementById("userName");
    var userEmail = document.getElementById("userEmail");
    var userPassword = document.getElementById("userPassword");
    var userRetypePassword = document.getElementById("userRetypePassword");
    var genderCheckboxes = document.getElementsByName("gender");
    var userGender = '';
    var userBirthday = '';
    var userAddress = document.getElementById("userAddress");
    var userCountry = document.getElementById("userCountry");
    var userGenre1 = document.getElementById("userGenre1");
    var userGenre2 = document.getElementById("userGenre2");
    var userGenre3 = document.getElementById("userGenre3");
    var picture = document.getElementById("Picture");            //path-ul initial al pozei
    var picture2 = picture.value.split("\\");                    //impartim adresa
    var picture3 = picture2[picture2.length - 1];                  //doar numele pozei

    if (genderCheckboxes[0].checked == true)
        userGender = "M";
    else if (genderCheckboxes[1].checked == true)
        userGender = "F";
    else if (genderCheckboxes[2].checked == true)
        userGender = "AH";


    var D = document.getElementById("D");
    var M = document.getElementById("M");
    var Y = document.getElementById('Y');

    if (Y.value == '');
    else if (Y.value != '') {
        userBirthday = D.value + '.' + M.value + '.' + Y.value;
    }



    /*
      console.log(userName.value);
      console.log(userEmail.value);
      console.log(userPassword.value);
      console.log(userRetypePassword.value);
      console.log(userGender);
      console.log(userBirthday);
      console.log(userAddress.value);
      console.log(userCountry.value);
      console.log(userGenre1.value);
      console.log(userGenre2.value);
      console.log(userGenre3.value);
      console.log(picture3);
      */

    if (userName.value.length < 1) {
        alert("User Name can not be null");
    }
    else if (userEmail.value.length < 1) {
        alert("User Email can not be null");
    }

    else if (userPassword.value.length < 5) {
        alert("Password must be at least 5 characters long");
    }

    else if (userPassword.value != userRetypePassword.value) {
        alert("Passwords don't match");
    }

    else {

        var data = {                                   //construim obiectul de trimis
            userName: userName.value,
            userEmail: userEmail.value,
            userPassword: userPassword.value,
            userRetypePassword: userRetypePassword.value,
            userGender: userGender,
            userAddress: userAddress.value,
            userCountry: userCountry.value,
            userGenre1: userGenre1.value,
            userGenre2: userGenre2.value,
            userGenre3: userGenre3.value,
            userPicture: picture3
        };

        var stringify = JSON.stringify(data);
        data = stringify;
        console.log(data);
        
        if(picture3!=''){/*
            var jpegRequest = new XMLHttpRequest();
            jpegRequest.open('POST', '/pictureRequest');
            jpegRequest.setRequestHeader("Content-Type", "image");
            };
            newAccountRequest.send(picture.value);
            */
        }


        /*
        var newAccountRequest = new XMLHttpRequest();
        newAccountRequest.open('POST', '/newAccountRequest');
        newAccountRequest.setRequestHeader("Content-Type", "application/javascript");
        newAccountRequest.onload = function () {
            console.log(newAccountRequest.responseText);
            var ok = newAccountRequest.responseText;
            if (ok == 0) {
                alert("Account created");
                window.location.href = "BoRe_home_LoggedIn1.1.html";
            }
            else {
                alert("Could not create account");
            }
        };
    
        newAccountRequest.send(data);
        */
    }

}