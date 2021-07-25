var hotResults=document.getElementById("hot");

var searchButton=document.getElementById("see");





searchButton.onclick=function(){                                        //cand dam click la Search
    var genres = document.getElementById("genres");
    console.log(genres.value);

    var hotRequest = new XMLHttpRequest();                        //facem un request
    hotRequest.open('POST', '/hotRequest');
    hotRequest.setRequestHeader("Content-Type", "application/javascript");
    hotRequest.onload = function () {
        console.log(hotRequest.responseText);
        hotResults.innerHTML='';
        hotResults.innerHTML=hotRequest.responseText;
    };

    hotRequest.send(genres.value);
}



