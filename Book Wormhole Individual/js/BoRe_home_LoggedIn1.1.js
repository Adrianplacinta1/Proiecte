var deschis=document.getElementById('deschis');
deschis.style.transition="1s";
    deschis.style.transform="rotateY(-145deg)";

var card=document.getElementById('card');
card.style.transition="1s";
card.style.boxShadow="inset 20px 0 50px rgba(0,0,0,.5)";

var searchResults=document.getElementById("searchResults");

var searchButton=document.getElementById("searchButton");





searchButton.onclick=function(){                                        //cand dam click la Search
    var searchName=document.getElementById("search");                  //preluam ce a scris userul
    var searchCriterium=document.getElementById("What");               //preluam ce categorie a ales sa caute (Books, By Author, By Genre)
    console.log(searchName.value);
    console.log(searchCriterium.value);

    var data={
        searchName : searchName.value,
        searchCriterium : searchCriterium.value
    }
    var stringify=JSON.stringify(data);
    var data=stringify;                                               //construim obiectul si il facem string

    var searchRequest = new XMLHttpRequest();                        //facem un request
    searchRequest.open('POST', '/searchRequest');
    searchRequest.setRequestHeader("Content-Type", "application/javascript");
    searchRequest.onload = function () {
        console.log(searchRequest.responseText);
        searchResults.innerHTML='';
        searchResults.innerHTML=searchRequest.responseText;
        searchResults.style.display="flex";
    };

    searchRequest.send(data);

    
}




var clearButton=document.getElementById("clearButton");
clearButton.onclick=function(){                                   //cand dam click la Clear
    searchResults.style.display="none";
}

window.onclick=function(event){
    if(event.target.matches(".bookImage")){
        var book = event.target;
        var parinte=book.parentNode;
        var bookID=parinte.children[1];            //preluam ID-ul cartii, care e hidden
        bookID2=bookID.innerText;
        var sendBookID = new XMLHttpRequest();                        //facem un request
        sendBookID.open('POST', '/sendBookID');
        sendBookID.setRequestHeader("Content-Type", "application/javascript");
        sendBookID.onload = function () {
           if(sendBookID.responseText=="OK")
           window.location.href="Book_Page1.1.html";
        };
    
        sendBookID.send(bookID2.toString());
}
};

