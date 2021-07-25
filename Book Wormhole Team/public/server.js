var events = require('events');
var util = require('util');
var fs = require("fs");
const qs = require('qs');
var http = require('http');
var https = require('https');
var path = require('path');
const sqlite3 = require('sqlite3').verbose();              //pentru baza de date


var connectedUsers = [];   //useri conectati
var connectedUsersNr = 0;


//imagini:
const siteImages = ["/images/arches.png", "/images/arrow-down.png", "/images/book-cover.png", "/images/bookmarks.png", "/images/diagmonds.png", "/images/diagmonds-light.png",
    "/images/facebook.png", "/images/google.png", "/images/help1.png", "/images/help2.png", "/images/help3.png", "/images/help4.png", "/images/help5.png", "/images/help6.png", "/images/help7.png",
    "/images/help8.png", "/images/help9.png", "/images/loginBook.png", "/images/logo.png", "/images/logo-light.png", "/images/lowerBooCase.png", "/images/newAccount.png", "/images/notebook.png", "/images/profile.png",
    "/images/registerBook.png", "/images/shattered.png", "/images/shelf.png", "/images/solaris-cover.png", "/images/twitter.png"];

//css-uri:
const siteStylesheets = ["/stylesheets/about-us.css", "/stylesheets/account.css", "/stylesheets/account-edit.css", "/stylesheets/bookfeed.css", "/stylesheets/comunity.css", "/stylesheets/conditions.css",
    "/stylesheets/friends.css", "/stylesheets/genres.css", "/stylesheets/global.css", "/stylesheets/group.css", "/stylesheets/group-edit.css", "/stylesheets/help.css", "/stylesheets/index.css", "/stylesheets/login.css", "/stylesheets/messages.css", "/stylesheets/myBooks.css",
    "/stylesheets/notifications.css", "/stylesheets/privacy.css", "/stylesheets/recomandation.css", "/stylesheets/register.css", "/stylesheets/search.css", "/stylesheets/singlebooktemplate.css", "/stylesheets/statistics.css", "/stylesheets/terms.css"];

//javascripturi
const siteJavaScripts = ["/javascripts/about-us.js","/javascripts/account.js", "/javascripts/account-edit.js", "/javascripts/bookfeed.js", "/javascripts/comunity.js", "/javascripts/friends.js", "/javascripts/genres.js", "/javascripts/global.js", "/javascripts/group.js", 
"/javascripts/group-edit.js","/javascripts/index.js", "/javascripts/login.js", "/javascripts/messages.js", "/javascripts/myBooks.js", "/javascripts/notifications.js","/javascripts/privacy.js", "/javascripts/recomandations.js", "/javascripts/search.js", "/javascripts/singlebooktemplate.js",
"/javascripts/statistics.js","/javascripts/terms.js"];


//aici este serverul
var server = http.createServer(function (req, res) {
    console.log('request was made ' + req.url);
    res.setHeader("Access-Control-Allow-Origin", "*");

    //////////////////Intai avem requesturile scurte, pentru incarcarea paginilor si imaginilor//////////////////

    //requesturi pentru imagini

    for (i = 0; i < siteImages.length; i++) {
        if (req.url === siteImages[i]) {
            var addressString = '.' + siteImages[i];
            var loadImage = fs.readFileSync(addressString);
            res.writeHead(200, { 'Content-Type': 'image/jpeg' });
            res.write(loadImage);
            res.end();
        }
    }

    //requesturi pentru css-uri
    for (i = 0; i < siteStylesheets.length; i++) {
        if (req.url === siteStylesheets[i]) {
            var addressString = '.' + siteStylesheets[i];
            var loadCSS = fs.readFileSync(addressString, "UTF8");
            res.writeHead(200, { 'Content-Type': 'text/css' });
            res.write(loadCSS);
            res.end();
        }
    }

    //requesturi pentru javascripturi
    for (i = 0; i < siteJavaScripts.length; i++) {
        if (req.url === siteJavaScripts[i].toString()) {
            var addressString = '.' + siteJavaScripts[i];
            var loadJS = fs.readFileSync(addressString, "UTF8");
            res.writeHead(200, { 'Content-Type': 'text/css' });
            res.write(loadJS);
            res.end();
        }
    }





    //requesturi pentru pagini

    //request pentru about-us.html
    if (req.url === "/pages/about-us.html" || req.url === "/about-us" || req.url === "/about-us.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/about-us.html').pipe(res);
    }

    //request pentru account.html
    if (req.url === "/pages/account.html" || req.url === "/account" || req.url === "/account.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/account.html').pipe(res);
    }

    //request pentru account-edit.html
    if (req.url === "/pages/account-edit.html" || req.url === "/account-edit" || req.url === "/account-edit.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/account-edit.html').pipe(res);
    }

    //request pentru bookfeed.html
    if (req.url === "/pages/bookfeed.html" || req.url === "/bookfeed" || req.url === "/bookfeed.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/bookfeed.html').pipe(res);
    }

    //request pentru comunity.html
    if (req.url === "/pages/comunity.html" || req.url === "/comunity" || req.url === "/comunity.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/comunity.html').pipe(res);
    }

    //request pentru conditions.html
    if (req.url === "/pages/conditions.html" || req.url === "/conditions" || req.url === "/conditions.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/conditions.html').pipe(res);
    }

    //request pentru friends.html
    if (req.url === "/pages/friends.html" || req.url === "/friends" || req.url === "/friends.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/friends.html').pipe(res);
    }

    //request pentru genres.html
    if (req.url === "/pages/genres.html" || req.url === "/genres" || req.url === "/genres.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/genres.html').pipe(res);
    }

    //request pentru group.html
    if (req.url === "/pages/group.html" || req.url === "/group" || req.url === "/group.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/group.html').pipe(res);
    }

    //request pentru group-edit.html
    if (req.url === "/pages/group-edit.html" || req.url === "/group-edit" || req.url === "/group-edit.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/group-edit.html').pipe(res);
    }

    //request pentru help.html
    if (req.url === "/pages/help.html" || req.url === "/help" || req.url === "/help.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/help.html').pipe(res);
    }

    //request pentru index.html
    if (req.url === "/BookWormhole" || req.url === "/pages/index.html" || req.url === "/index" || req.url === "/index.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/index.html').pipe(res);
    }

    //request pentru login.html
    if (req.url === "/pages/login.html" || req.url === "/login" || req.url === "/login.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/login.html').pipe(res);
    }

    //request pentru messages.html
    if (req.url === "/pages/messages.html" || req.url === "/messages" || req.url === "/messages.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/messages.html').pipe(res);
    }

    //request pentru myBooks.html
    if (req.url === "/pages/myBooks.html" || req.url === "/myBooks" || req.url === "/myBooks.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/myBooks.html').pipe(res);
    }

    //request pentru notifications.html
    if (req.url === "/pages/notifications.html" || req.url === "/notifications" || req.url === "/notifications.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/notifications.html').pipe(res);
    }

    //request pentru privacy.html
    if (req.url === "/pages/privacy.html" || req.url === "/privacy" || req.url === "/privacy.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/privacy.html').pipe(res);
    }

    //request pentru recomandations
    if (req.url === "/pages/recomandations.html" || req.url === "/recomandations" || req.url === "/recomandations.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/recomandations.html').pipe(res);
    }

    //request pentru register
    if (req.url === "/pages/register.html" || req.url === "/register" || req.url === "/register.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/register.html').pipe(res);
    }

    //request pentru search.html
    if (req.url === "/pages/search.html" || req.url === "/search" || req.url === "/search.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/search.html').pipe(res);
    }

    //request pentru singlebooktemplate
    if (req.url === "/pages/singlebooktemplate.html" || req.url === "/singlebooktemplate" || req.url === "/singlebooktemplate.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/singlebooktemplate.html').pipe(res);
    }

    //request pentru statistics
    if (req.url === "/pages/statistics.html" || req.url === "/statistics" || req.url === "/statistics.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/statistics.html').pipe(res);
    }

    //request pentru terms
    if (req.url === "/pages/terms.html" || req.url === "/terms" || req.url === "/terms.html") {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        fs.createReadStream('pages/terms.html').pipe(res);
    }

    //////////////////////Sfarsitul requesturilor scurte////////////////////


    ////////////Requesturile lungi, care trateaza functionalitati ale paginilor/////////////////

    //requestul de LOGIN, care vine de la javascripts/login.js
    if (req.url === '/loginRequest') {
        console.log("/loginRequest");
        var loginInfo = '';
        var userInfo;
        req.on('data', function (chunk) {
            loginInfo += chunk;
        });
        req.on('end', () => {
            userInfo = JSON.parse(loginInfo);
            console.log(loginInfo);
            console.log(userInfo.email); //email
            console.log(userInfo.password); //password



            // cautam userul in baza de date

            var userID = -1;
            let db = new sqlite3.Database('./dataBase/DB.db');
            db.all('select Name, email, password, ID from Users', [], (err, rows) => {
                if (err) {
                    throw err;
                }
                rows.forEach((row) => {                 //verificam fiecare row daca corespunde
                    console.log(row.Name);
                    console.log(row.email);
                    console.log(row.password);
                    if (row.email == userInfo.email && row.password == userInfo.password) {
                        connectedUsers[connectedUsersNr] = {
                            ID: row.ID,
                            email: row.email,
                            password: row.password
                        }
                        userID = row.ID;
                        connectedUsersNr++;
                    }
                });
                console.log(userID);
                if (userID != -1) {                    //Daca am gasit userul, acceptam conexiunea
                    console.log("Exista user");
                }
                console.log(userID);
                res.setHeader('Content-Type', 'application/json');
                res.setHeader('Set-Cookie', ['userIDCookie=' + userID]);
                res.write(userID.toString());                  //trimitem raspuns la client cu ok (0 sau 1 in functie daca nu am gasit, respectiv am gasit userul).

                res.end();
            });
            db.close();
        });
        req.on('error', (error) => {
            console.error(error);
        });
    }

    //requestul Check Login, care vine de la toate paginile ce necesita ca userul sa fie conectat 
    if (req.url == '/checkLogin') {
        console.log('/checkLogin');
        var userID = '';
        req.on('data', function (chunk) {
            userID += chunk;
        });

        req.on('end', () => {
            console.log(userID);
            var ok = 0;
            for (i = 0; i < connectedUsers.length; i++) {
                if (connectedUsers[i].ID == userID)
                    ok = 1;
            }
            res.setHeader('Content-Type', 'application/json');
            res.write(ok.toString());                  //trimitem raspuns la client
            res.end();
        });
    };





    //requestul de LOGOUT, care vine de la apasarea butonului de logout
    if (req.url === '/logoutRequest') {
        var logoutStatus="Something went wrong";
        console.log("/logoutRequest");
        var logoutInfo = '';
        req.on('data', function (chunk) {
            logoutInfo += chunk;
        });
        req.on('end', () => {
            console.log(logoutInfo);
            for(i=0;i<connectedUsers.length;i++){
                if(connectedUsers[i].ID==logoutInfo){
                    for(j=i+1;j<connectedUsers.length;j++)
                    {connectedUsers[j-1]=connectedUsers[j];}
                    connectedUsersNr--;
                    logoutStatus=-1;
                }
            }
                res.setHeader('Content-Type', 'application/json');
                res.setHeader('Set-Cookie', ['userIDCookie=' + logoutStatus.toString()]);
                res.write(logoutStatus.toString());                  //trimitem raspuns la client cu ok (0 sau 1 in functie daca nu am gasit, respectiv am gasit userul).
                res.end();
        });
        req.on('error', (error) => {
            console.error(error);
        });
    }


});
server.listen(3000, '127.0.0.1');              //punem serverul sa asculte la localhost, portul 3000
console.log('Server Activated');               //cand serverul e activat, va afias acest mesaj in consola







