var events = require('events');
var util = require('util');
var fs = require("fs");
const qs = require('qs');
var http = require('http');
var path = require('path');
const sqlite3 = require('sqlite3').verbose();
let db = new sqlite3.Database('./dataBase/DB.db');

/*sesiune*/
var session = { userID: ' ', userName: '', email: '', password: '' };
var bookID = -1;  //variabila globala ce retine ID-ul unei carti, pentru a sti ce sa incarce in Book_Page1.1.html
var userID = -1; //variabila globala ce retine ID-ul unui User, pentru a sti ce sa incarce in MY_Account1.1.html

//css-urile si js-urile paginilor + coperta cartii

const imgGenericBook = fs.readFileSync("./images/genericBook.jpg");

const indexCSS = fs.readFileSync("./css/index.css", "UTF8");
const myAccountCSS = fs.readFileSync("./css/My_Account1.1.css", "UTF8");
const whatSHotCSS = fs.readFileSync("./css/What's_Hot1.1.css", "UTF8");
const usersFollowedCSS = fs.readFileSync("./css/Users_Followed1.1.css", "UTF8");
const myGroupsCSS = fs.readFileSync("./css/My_Groups1.1.css", "UTF8");
const groupPageCSS = fs.readFileSync("./css/Group_Page1.1.css", "UTF8");
const bookPageCSS = fs.readFileSync("./css/Book_Page1.1.css", "UTF8");

const bookPagejs = fs.readFileSync("./js/Book_Page1.1.js", "UTF8");
const BoRe_Loginjs = fs.readFileSync("./js/BoRe_Login1.1.js", "UTF8");
const BoRe_homejs = fs.readFileSync("./js/BoRe_home1.1.js", "UTF8");
const BoRe_home_LoggedInjs = fs.readFileSync("./js/BoRe_home_LoggedIn1.1.js", "UTF8");
const usersFollowedjs = fs.readFileSync("./js/Users_followed1.1.js", "UTF8");
const myGroupsjs = fs.readFileSync("./js/My_Groups1.1.js", "UTF8");
const groupPagejs = fs.readFileSync("./js/Group_Page1.1.js", "UTF8");
const newAccountjs = fs.readFileSync("./js/New_Account1.1.js", "UTF8");
const whatSHotjs = fs.readFileSync("./js/What's_Hot1.1.js", "UTF8");
const myAccountjs = fs.readFileSync("./js/My_Account1.1.js", "UTF8");




//aici extragem din baza de date path-urile imaginilor pt cati, useri si grupuri

var bookCovers = [];
var counter = 0;
var userImages = [];
var groupImages = [];

db.all('select Cover from Books', [], (err, rows) => {           //pentru carti
    if (err) {
        throw err;
    }
    rows.forEach((row) => {
        counter++;
        bookCovers[counter] = row.Cover;
    });
});

counter = 0;
db.all('select Photo from Users', [], (err, rows) => {        //pentru useri
    if (err) {
        throw err;
    }
    rows.forEach((row) => {
        counter++;
        userImages[counter] = row.Photo;
    });
});

counter = 0;
db.all('select Picture from Groups', [], (err, rows) => {        //pentru grupuri
    if (err) {
        throw err;
    }
    rows.forEach((row) => {
        counter++;
        groupImages[counter] = row.Picture;
    });
});

db.close();


//aici este serverul
var server = http.createServer(function (req, res) {
    console.log('request was made ' + req.url);

    //////////////////Intai avem requesturile scurte, pentru incarcarea paginilor si imaginilor//////////////////
    //requesturi pentru BoRe_home
    if (req.url === '/BoRe_home1.1.html' || req.url === '/' || req.url === '/bookWormhole') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('BoRe_home1.1.html').pipe(res);
    }

    if (req.url === '/css/index.css') {
        res.writeHead(200, { 'Content-Type': 'text/css' });
        res.write(indexCSS);
        res.end();
    }

    if (req.url === '/js/BoRe_home1.1.js') {
        res.writeHead(200, { 'Content-Type': 'text/css' });
        res.write(BoRe_homejs);
        res.end();
    }

    if (req.url === '/images/genericBook.jpg') {
        res.writeHead(200, { 'Content-Type': 'image/jpeg' });
        res.write(imgGenericBook);
        res.end();
    }


    //requesturi pentru BoRe_LogIn

    if (req.url === '/BoRe_LogIn1.1.html') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('BoRe_LogIn1.1.html').pipe(res);
    }

    if (req.url === '/js/BoRe_Login1.1.js') {
        res.writeHead(200, { 'Content-Type': 'text/css' });
        res.write(BoRe_Loginjs);
        res.end();
    }


    //requesturi pentru BoRe_home_loggedIn

    if (req.url === '/BoRe_home_LoggedIn1.1.html?' || req.url === '/BoRe_home_LoggedIn1.1.html') {
        if (session.userName == '' && session.password == '' && session.email == '') {   //daca nu avem user logat, il redirectionam la homepage
            res.writeHead(200, { 'Content-Type': 'text/html' });
            fs.createReadStream('BoRe_home1.1.html').pipe(res);
        }
        else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            fs.createReadStream('BoRe_home_LoggedIn1.1.html').pipe(res);
        }
    }

    if (req.url === '/js/BoRe_home_LoggedIn1.1.js') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(BoRe_home_LoggedInjs);
        res.end();
    }



    //requesturi pentru New_Account                            
    if (req.url === '/New_Account1.1.html') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('New_Account1.1.html').pipe(res);
    }

    if (req.url === '/js/New_Account1.1.js') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(newAccountjs);
        res.end();
    }



    //requesturi pentru MY_Account
    if (req.url === '/My_Account1.1.html') {
        if (session.userName == '' && session.password == '' && session.email == '') {   //daca nu avem user logat, il redirectionam la homepage
            res.writeHead(200, { 'Content-Type': 'text/html' });
            fs.createReadStream('BoRe_home1.1.html').pipe(res);
        }
        else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            fs.createReadStream('My_Account1.1.html').pipe(res);
        }
    }

    if (req.url === '/css/My_Account1.1.css') {
        res.writeHead(200, { 'Content-Type': 'text/css' });
        res.write(myAccountCSS);
        res.end();
    }

    if (req.url === '/js/My_Account1.1.js') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(myAccountjs);
        res.end();
    }

    //requesturi pentru What's_Hot
    if (req.url === "/What's_hot1.1.html") {
        if (session.userName == '' && session.password == '' && session.email == '') {   //daca nu avem user logat, il redirectionam la homepage
            res.writeHead(200, { 'Content-Type': 'text/html' });
            fs.createReadStream('BoRe_home1.1.html').pipe(res);
        }
        else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            fs.createReadStream("What's_Hot1.1.html").pipe(res);
        }
    }

    if (req.url === "/css/What's_Hot1.1.css") {
        res.writeHead(200, { 'Content-Type': 'text/css' });
        res.write(whatSHotCSS);
        res.end();
    }

    if (req.url === "/js/What's_Hot1.1.js") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(whatSHotjs);
        res.end();
    }

    //requesturi pentru Users_Followed
    if (req.url === "/Users_Followed1.1.html") {
        if (session.userName == '' && session.password == '' && session.email == '') {   //daca nu avem user logat, il redirectionam la homepage
            res.writeHead(200, { 'Content-Type': 'text/html' });
            fs.createReadStream('BoRe_home1.1.html').pipe(res);
        }
        else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            fs.createReadStream("Users_Followed1.1.html").pipe(res);
        }
    }

    if (req.url === "/css/Users_Followed1.1.css") {
        res.writeHead(200, { 'Content-Type': 'text/css' });
        res.write(usersFollowedCSS);
        res.end();
    }

    if (req.url === '/js/Users_followed1.1.js') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(usersFollowedjs);
        res.end();
    }



    //requesturi pentru My_Groups
    if (req.url === "/My_Groups1.1.html") {
        if (session.userName == '' && session.password == '' && session.email == '') {   //daca nu avem user logat, il redirectionam la homepage
            res.writeHead(200, { 'Content-Type': 'text/html' });
            fs.createReadStream('BoRe_home1.1.html').pipe(res);
        }
        else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            fs.createReadStream("My_Groups1.1.html").pipe(res);
        }
    }

    if (req.url === "/css/My_Groups1.1.css") {
        res.writeHead(200, { 'Content-Type': 'text/css' });
        res.write(myGroupsCSS);
        res.end();
    }

    if (req.url === '/js/My_Groups1.1.js') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(myGroupsjs);
        res.end();
    }




    //requesturi pentru Group_Page
    if (req.url === "/Group_Page1.1.html") {
        if (session.userName == '' && session.password == '' && session.email == '') {   //daca nu avem user logat, il redirectionam la homepage
            res.writeHead(200, { 'Content-Type': 'text/html' });
            fs.createReadStream('BoRe_home1.1.html').pipe(res);
        }
        else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            fs.createReadStream("Group_Page1.1.html").pipe(res);
        }
    }

    if (req.url === "/css/Group_Page1.1.css") {
        res.writeHead(200, { 'Content-Type': 'text/css' });
        res.write(groupPageCSS);
        res.end();
    }

    if (req.url === '/js/Group_Page1.1.js') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(groupPagejs);
        res.end();
    }



    //requesturi pentru Book_Page
    if (req.url === "/Book_Page1.1.html") {
        if (session.userName == '' && session.password == '' && session.email == '') {   //daca nu avem user logat, il redirectionam la homepage
            res.writeHead(200, { 'Content-Type': 'text/html' });
            fs.createReadStream('BoRe_home1.1.html').pipe(res);
        }
        else {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            fs.createReadStream("Book_Page1.1.html").pipe(res);
        }
    }

    if (req.url === "/css/Book_Page1.1.css") {
        res.writeHead(200, { 'Content-Type': 'text/css' });
        res.write(bookPageCSS);
        res.end();
    }

    if (req.url === '/js/Book_Page1.1.js') {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(bookPagejs);
        res.end();
    }




    //requesturile pentru copertile cartilor

    for (i = 1; i <= bookCovers.length; i++) {
        if (req.url === "/" + bookCovers[i]) {
            console.log(bookCovers[i]);
            res.writeHead(200, { 'Content-Type': 'image/jpeg' });
            var imagine = fs.readFileSync("./" + bookCovers[i]);
            res.write(imagine);
            res.end();
        }
    }



    //requesturi pentru imaginile grupurilor
    for (i = 1; i <= groupImages.length; i++) {
        if (req.url === "/" + groupImages[i]) {
            console.log(groupImages[i]);
            res.writeHead(200, { 'Content-Type': 'image/jpeg' });
            var imagine = fs.readFileSync("./" + groupImages[i]);
            res.write(imagine);
            res.end();
        }
    }

    //requesturi pentru imaginile userilor
    for (i = 1; i <= userImages.length; i++) {
        if (req.url === "/" + userImages[i]) {
            console.log(userImages[i]);
            res.writeHead(200, { 'Content-Type': 'image/jpeg' });
            var imagine = fs.readFileSync("./" + userImages[i]);
            res.write(imagine);
            res.end();
        }
    }

    //////////////////////Sfarsitul requesturilor scurte////////////////////













    ////////////Requesturile lungi, care trateaza functionalitati ale paginilor/////////////////

    //requestul de LOGIN, care vine de la js/BoRe_Login1.1.js
    if (req.url === '/loginRequest') {
        console.log("DA FAQ?");
        var loginInfo = '';
        var userInfo;
        req.on('data', function (chunk) {
            loginInfo += chunk;
        });
        req.on('end', () => {
            userInfo = loginInfo.split("~");
            //console.log(loginInfo);
            // console.log(userInfo[0]); //userName
            // console.log(userInfo[1]); //email
            // console.log(userInfo[2]); //password



            // cautam userul in baza de date

            var ok = 0;
            let db = new sqlite3.Database('./dataBase/DB.db');
            db.all('select Name, email, password, ID from Users', [], (err, rows) => {
                if (err) {
                    throw err;
                }
                rows.forEach((row) => {                 //verificam fiecare row daca corespunde
                    console.log(row.Name);
                    console.log(row.email);
                    console.log(row.password);
                    if (row.Name == userInfo[0] && row.email == userInfo[1] && row.password == userInfo[2]) {
                        session.userID = row.ID;
                        ok++;          //daca am gasit userul, incrementam ok.
                    }
                });
                console.log(ok);
                if (ok > 0) {                    //Daca am gasit userul, acceptam conexiunea
                    console.log("Exista user");
                    session.userName = userInfo[0];
                    session.email = userInfo[1];
                    session.password = userInfo[2];           //si trecem userul in sesiune

                }
                res.setHeader('Content-Type', 'application/json');
                res.write(ok.toString());                  //trimitem raspuns la client cu ok (0 sau 1 in functie daca nu am gasit, respectiv am gasit userul).
                res.end();
            });
            db.close();
        });
        req.on('error', (error) => {
            console.error(error);
        });
    }










    //requestul de New Account , care vine de la js/New_Account1.1.js
    if (req.url === '/newAccountRequest') {
        console.log("DA FAQ?");
        var newAccountInfo = '';
        var userInfo;
        req.on('data', function (chunk) {
            newAccountInfo += chunk;
        });
        req.on('end', () => {
            userInfo = JSON.parse(newAccountInfo);
            console.log(userInfo);



            // cautam daca exista deja un user cu acelasi email

            var ok = 0;
            let db = new sqlite3.Database('./dataBase/DB.db');
            db.all('select email from Users', [], (err, rows) => {
                if (err) {
                    throw err;
                }
                rows.forEach((row) => {                 //verificam fiecare row daca corespunde
                    console.log(row.email);
                    if (row.email == userInfo.userEmail) {
                        ok++;          //daca am gasit un user cu acelasi email, incrementam ok.
                    }
                });
                console.log(ok);
                if (ok == 0) {                    //Daca emailul e unic, deci facem user
                    console.log("Exista user");
                    session.userName = userInfo.userName;
                    session.email = userInfo.userEmail;
                    session.password = userInfo.userPassword;           //si trecem userul in sesiune
                }
                res.setHeader('Content-Type', 'application/json');
                res.write(ok.toString());                  //trimitem raspuns la client cu ok (0 sau 1 in functie daca nu am gasit, respectiv am gasit user cu acelasi email).
                res.end();
            });
            db.close();
        });
        req.on('error', (error) => {
            console.error(error);
        });
    }













    //requestul de LOGOUT, care vine de la BoRe_home, intrucat aici ajungi cand apesi butonul de Log Out 
    if (req.url == '/logoutRequest') {
        var loginInfo = '';
        req.on('data', function (chunk) {
            loginInfo += chunk;
        });
        session.userName = '';
        session.userID = '';
        session.email = '';
        session.password = '';
        console.log(session.userName);
        req.on('end', () => {
            res.setHeader('Content-Type', 'application/json');
            res.write('Logout successful');                  //trimitem raspuns la client, ca asa-i frumos.
            res.end();
        });
    };














    //requestul de Search, folosit ca sa cautam carti
    if (req.url === '/searchRequest') {
        console.log("DA FAQ?");
        var receivedData = '';
        var convert;
        req.on('data', function (chunk) {
            receivedData += chunk;
        });
        req.on('end', () => {
            convert = JSON.parse(receivedData);
            receivedData = convert;

            var htmlString = '';   //o sa creem un html cu cartile gasite, ce va fi apoi introdus in pagina

            // cautam cartile


            let db = new sqlite3.Database('./dataBase/DB.db');
            db.all('select ID, Title, Author, Genre, Rating, NrPag, Publisher, Edition, Cover from Books', [], (err, rows) => {
                if (err) {
                    throw err;
                }
                rows.forEach((row) => {                 //verificam fiecare row daca corespunde
                    if (receivedData.searchCriterium == 'Books') {                  //daca avem de cautat carti dupa titlu
                        if (row.Title.toLowerCase().indexOf(receivedData.searchName.toLowerCase()) != -1) {
                            htmlString += '<div class="book"><img class="bookImage" src="' + row.Cover + '"><p class="hiddenID">' + row.ID + '</p>'
                            htmlString += '<p> Title: ' + row.Title + ' <br> Author: ' + row.Author + ' <br> Genre: ' + row.Genre + '<br> Rating: ' + row.Rating + '</p></div>';
                        }
                    }


                    else if (receivedData.searchCriterium == 'By Author') {            //daca avem de cautat dupa autor
                        if (row.Author.toLowerCase().indexOf(receivedData.searchName.toLowerCase()) != -1) {
                            htmlString += '<div class="book"><img class="bookImage" src="' + row.Cover + '"><p class="hiddenID">' + row.ID + '</p>'
                            htmlString += '<p> Title: ' + row.Title + ' <br> Author: ' + row.Author + ' <br> Genre: ' + row.Genre + '<br> Rating: ' + row.Rating + '</p></div>';
                        }
                    }


                    else if (receivedData.searchCriterium == 'By Genre') {             //daca avem de cautat dupa gen
                        if (row.Genre.toLowerCase().indexOf(receivedData.searchName.toLowerCase()) != -1) {
                            htmlString += '<div class="book"><img class="bookImage" src="' + row.Cover + '"><p class="hiddenID">' + row.ID + '</p>'
                            htmlString += '<p> Title: ' + row.Title + ' <br> Author: ' + row.Author + ' <br> Genre: ' + row.Genre + '<br> Rating: ' + row.Rating + '</p></div>';
                        }
                    }
                });
                res.setHeader('Content-Type', 'application/json');
                res.write(htmlString);                  //trimitem stringul html la sursa;
                res.end();
            });
            db.close();
        });
        req.on('error', (error) => {
            console.error(error);
        });
    }













    //requestul de What's Hot, care iti arata cele mai bine cotate 30 de carti dintr-un anumit gen;
    if (req.url === '/hotRequest') {
        console.log("DA FAQ?");
        var receivedData = '';        // nu e nevoie sa convertim in json, ca nu e un obiect, e doar text, anume genul ales

        req.on('data', function (chunk) {
            receivedData += chunk;
        });
        req.on('end', () => {

            var htmlString = '';   //o sa creem un html cu cartile gasite, ce va fi apoi introdus in pagina
            var hotBooks = [];       //un vector in care vom sorta cartile
            var aux;
            var indice = 0;

            // cautam cartile


            let db = new sqlite3.Database('./dataBase/DB.db');
            db.all('select ID, Title, Author, Genre, Rating, NrPag, Publisher, Edition, Cover from Books', [], (err, rows) => {
                if (err) {
                    throw err;
                }
                rows.forEach((row) => {                 //verificam fiecare row daca corespunde

                    if (receivedData == 'All') {                  //daca avem de cautat carti de toate genurile
                        hotBooks[indice] = {
                            ID: row.ID,
                            Title: row.Title,
                            Author: row.Author,
                            Genre: row.Genre,
                            Rating: row.Rating,
                            nrPag: row.nrPag,
                            Publisher: row.Publisher,
                            Edition: row.Edition,
                            Cover: row.Cover
                        }
                        indice++;
                    }

                    else {             //daca avem de cautat dupa un gen anume
                        if (row.Genre.toLowerCase().indexOf(receivedData.toLowerCase()) != -1) {
                            hotBooks[indice] = {
                                ID: row.ID,
                                Title: row.Title,
                                Author: row.Author,
                                Genre: row.Genre,
                                Rating: row.Rating,
                                nrPag: row.nrPag,
                                Publisher: row.Publisher,
                                Edition: row.Edition,
                                Cover: row.Cover
                            }
                            indice++;
                        }
                    }

                });
                db.close();
                for (i = 0; i < indice; i++)
                    for (j = i; j < indice; j++)
                        if (hotBooks[i].Rating < hotBooks[j].Rating) {
                            aux = hotBooks[i];
                            hotBooks[i] = hotBooks[j];
                            hotBooks[j] = aux;
                        }

                for (i = 0; i < indice; i++) {
                    if (i < 30) {
                        htmlString += '<div class="card text "><h3><u>' + hotBooks[i].Title + '</u></h3>';
                        htmlString += '<div class=cardBody>';
                        htmlString += '<a href="Book_Page1.1.html">';
                        htmlString += '<img class="bookImage" src="' + hotBooks[i].Cover + '"></a>';
                        htmlString += '<div class="containedText">';
                        htmlString += '<p class ="hiddenID">' + hotBooks[i].ID + '</p>';
                        htmlString += '<p>⤷ Rating: ' + hotBooks[i].Rating + '/5</p>';
                        htmlString += '<p>⤷ Author: ' + hotBooks[i].Author + '</p>';
                        htmlString += '<p>⤷ Genre: ' + hotBooks[i].Genre + '</p>';
                        htmlString += '</div></div></div>';
                    }
                }
                res.setHeader('Content-Type', 'application/json');
                res.write(htmlString);                  //trimitem stringul html la sursa;
                res.end();
            });
        });
        req.on('error', (error) => {
            console.error(error);
        });
    }








    //requestul de Find User, folosit ca sa cautam useri, in Pagina Users_Followed1.1.html
    if (req.url === '/findUserRequest') {
        console.log("DA FAQ?");
        var receivedData = '';        // nu e nevoie sa convertim in json, ca nu e un obiect, e doar text

        req.on('data', function (chunk) {
            receivedData += chunk;
        });
        req.on('end', () => {

            var htmlString = '';   //o sa creem un html cu cartile gasite, ce va fi apoi introdus in pagina
            var usersFound = [];       //un vector in care vom sorta cartile
            var aux;
            var indice = 0;

            // cautam cartile


            let db = new sqlite3.Database('./dataBase/DB.db');
            db.all('select ID, Name, email, Photo from Users', [], (err, rows) => {
                if (err) {
                    throw err;
                }
                rows.forEach((row) => {                 //verificam fiecare row daca corespunde

                    if (row.Name.toLowerCase().indexOf(receivedData.toLowerCase()) != -1 || row.email.toLowerCase().indexOf(receivedData.toLowerCase()) != -1) {
                        usersFound[indice] = {
                            ID: row.ID,
                            Name: row.Name,
                            email: row.email,
                            Photo: row.Photo
                        };
                        indice++;
                    }

                });
                db.close();
                for (i = 0; i < indice; i++)
                    for (j = i; j < indice; j++)
                        if (usersFound[i].Name.toLowerCase() > usersFound[j].Name.toLowerCase()) {
                            aux = usersFound[i];
                            usersFound[i] = usersFound[j];
                            usersFound[j] = aux;
                        }

                for (i = 0; i < indice; i++) {
                    htmlString += '<div class="usersFound">';
                    htmlString += '<img src="' + usersFound[i].Photo + '">';
                    htmlString += '<p class="hiddenID">' + usersFound[i].ID + '</p>';
                    htmlString += '<p class="text">' + usersFound[i].Name + '</p>';
                    htmlString += '<p class="text">' + usersFound[i].email + '</p>';
                    htmlString += '<p><button class="viewUserButton">View User</button></p></div>';
                }
                res.setHeader('Content-Type', 'application/json');
                res.write(htmlString);                  //trimitem stringul html la sursa;
                res.end();
            });
        });
        req.on('error', (error) => {
            console.error(error);
        });
    }

















    //requestul de Find Group, folosit ca sa cautam grupuri, in Pagina My_Groups1.1.html
    if (req.url === '/findGroupRequest') {
        console.log("DA FAQ?");
        var receivedData = '';        // nu e nevoie sa convertim in json, ca nu e un obiect, e doar text

        req.on('data', function (chunk) {
            receivedData += chunk;
        });
        req.on('end', () => {

            var htmlString = '';   //o sa creem un html cu cartile gasite, ce va fi apoi introdus in pagina
            var groupsFound = [];       //un vector in care vom sorta cartile
            var aux;
            var indice = 0;

            // cautam cartile


            let db = new sqlite3.Database('./dataBase/DB.db');
            db.all('select ID, Name, Picture from Groups', [], (err, rows) => {
                if (err) {
                    throw err;
                }
                rows.forEach((row) => {                 //verificam fiecare row daca corespunde

                    if (row.Name.toLowerCase().indexOf(receivedData.toLowerCase()) != -1) {
                        groupsFound[indice] = {
                            ID: row.ID,
                            Name: row.Name,
                            email: row.email,
                            Picture: row.Picture
                        };
                        indice++;
                    }

                });
                db.close();
                for (i = 0; i < indice; i++)
                    for (j = i; j < indice; j++)
                        if (groupsFound[i].Name.toLowerCase() > groupsFound[j].Name.toLowerCase()) {
                            aux = groupsFound[i];
                            groupsFound[i] = groupsFound[j];
                            groupsFound[j] = aux;
                        }

                for (i = 0; i < indice; i++) {
                    htmlString += '<div class="groupsFound">';
                    htmlString += '<img src="' + groupsFound[i].Picture + '">';
                    htmlString += '<p class="hiddenID">' + groupsFound[i].ID + '</p>';
                    htmlString += '<p class="text aliniatOleaca">' + groupsFound[i].Name + '</p>';
                    htmlString += '<p><button class="viewGroupButton">View Group</button></p></div>';
                }
                res.setHeader('Content-Type', 'application/json');
                res.write(htmlString);                  //trimitem stringul html la sursa;
                res.end();
            });
        });
        req.on('error', (error) => {
            console.error(error);
        });
    };









    //requestul care primeste ID-ul unei carti, pentru a prelua informatia din tabel si a o incarca in pagina Book_Page1.1.html
    if (req.url == '/sendBookID') {
        var receivedID = '';
        req.on('data', function (chunk) {
            receivedID += chunk;
        });


        req.on('end', () => {
            bookID = receivedID;
            console.log(bookID);
            res.setHeader('Content-Type', 'application/json');
            res.write('OK');                  //trimitem raspuns la client, ca asa-i frumos.
            res.end();
        });
    };







    //requestul de incarcare pt Book_Page1.1.html, caruia ii vom furniza informatii despre carti.
    if (req.url === '/initiateBook_Page') {
        console.log("DA FAQ?");
        var receivedData = '';        // nu e nevoie sa convertim in json, ca nu e un obiect, e doar text

        req.on('data', function (chunk) {
            receivedData += chunk;
        });
        req.on('end', () => {

            var bookInfo = {    //ce o sa preluam noi din tabel
                ID: bookID,
                Title: '',
                Author: '',
                Genre: '',
                Rating: '',
                NrPag: '',
                Publisher: '',
                Edition: '',
                Cover: '',
                Review: []
            };

            var i = 0;
            console.log(bookID);

            // cautam cartea


            let db = new sqlite3.Database('./dataBase/DB.db');
            let sql = 'select Books.ID, Books.Title, Books.Author, Books.Genre, Books.Rating, Books.NrPag, Books.Publisher, Books.Edition, Books.Cover, My_Books.Review, My_Books.UserID, Users.Name, Users.Photo from Books LEFT OUTER JOIN My_Books on Books.ID=My_Books.BookID left outer join Users on My_Books.UserID=Users.ID where Books.ID = ?';
            let parametru = bookID;
            db.all(sql, [parametru], (err, rows) => {
                if (err) {
                    throw err;
                }
                rows.forEach((row) => {

                    bookInfo.Title = row.Title;
                    bookInfo.Author = row.Author;
                    bookInfo.Genre = row.Genre;
                    bookInfo.Rating = row.Rating;
                    bookInfo.NrPag = row.NrPag;
                    bookInfo.Publisher = row.Publisher;
                    bookInfo.Edition = row.Edition;
                    bookInfo.Cover = row.Cover;

                    if (row.Review != 'N/A' && row.Review != null) {
                        console.log(row.Review);
                        bookInfo.Review[i] = {
                            userID: row.UserID,
                            userName: row.Name,
                            userPhoto: row.Photo,
                            userReview: row.Review
                        }
                        i++;
                    }
                });
                db.close();
                var data = JSON.stringify(bookInfo);
                console.log(data);
                res.setHeader('Content-Type', 'application/json');
                res.write(data);                  //trimitem stringul html la sursa;
                res.end();
            });


        });
        req.on('error', (error) => {
            console.error(error);
        });
    };






    //requestul de get usersfollowed, care incarca in pagina Users_Followed1.1.
    if (req.url === '/getUsersFollowed') {
        console.log("DA FAQ?");
        var receivedData = '';        // nu e nevoie sa convertim in json, ca nu e un obiect, e doar text

        req.on('data', function (chunk) {
            receivedData += chunk;
        });
        req.on('end', () => {

            var usersFound = [];

            var i = 0;
            console.log(bookID);

            // cautam useri


            let db = new sqlite3.Database('./dataBase/DB.db');
            let sql = 'select Users_Followed.UserID, Users_Followed.Followed_UserID, Users.ID, Users.Name, Users.Photo from Users_Followed INNER JOIN Users on Users_Followed.Followed_UserID=Users.ID where Users_Followed.UserID = ?';
            let parametru = session.userID;
            db.all(sql, [parametru], (err, rows) => {
                if (err) {
                    throw err;
                }
                rows.forEach((row) => {
                    usersFound[i] = {
                        userID: row.Followed_UserID,
                        userName: row.Name,
                        userPhoto: row.Photo
                    };
                    i++;
                });
                db.close();
                var data = JSON.stringify(usersFound);
                console.log(data);
                res.setHeader('Content-Type', 'application/json');
                res.write(data);                  //trimitem stringul html la sursa;
                res.end();
            });


        });
        req.on('error', (error) => {
            console.error(error);
        });
    };



    //requestul care primeste ID-ul unui user, pentru a prelua informatia din tabel si a o incarca in pagina My_Account1.1.html
    if (req.url == '/sendUserID') {
        var receivedID = '';
        req.on('data', function (chunk) {
            receivedID += chunk;
        });


        req.on('end', () => {
            userID = receivedID;
            console.log(userID);
            res.setHeader('Content-Type', 'application/json');
            res.write('OK');                  //trimitem raspuns la client, ca asa-i frumos.
            res.end();
        });
    };


});

server.listen(3000, '127.0.0.1');              //punem serverul sa asculte la localhost, portul 3000
console.log('Server Activated');               //cand serverul e activat, va afias acest mesaj in consola







