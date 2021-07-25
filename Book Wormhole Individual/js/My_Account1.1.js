window.onload = function(event) {
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "/initiateMy_Account");
    xmlhttp.onload = function() {
        var bookData = JSON.parse(xmlhttp.responseText);
        var everythingAboutBook=document.getElementById("everythingAboutBook");
        everythingAboutBook.innerHTML='';
        var htmlString='';
        htmlString+='<p><img class="bookImage" src="'+bookData.Cover+'"></p>';
        htmlString+='<p><label>Title: </label><label id="getTitle">'+bookData.Title+'</label></p>';
        htmlString+='<p><label>Author: </label><label id="getAuthor">'+bookData.Author+'</label></p>';
        htmlString+='<p><label>Rating: </label><label id="getRating">'+bookData.Rating+'/5</label></p>';
        htmlString+='<p><label>Genre: </label><label id="getGenre">'+bookData.Genre+'</label></p>';
        htmlString+='<p><label>Number of Pages: </label><label id="getGenre">'+bookData.NrPag+'</label></p>';
        htmlString+='<p><label>Publisher: </label><label id="getPublisher">'+bookData.Publisher+'</label></p>';
        htmlString+='<p><label>Edition: </label><label id="getEdition">'+bookData.Edition+'</label></p>';
        htmlString+='<p><button>Add to my books</button></p>';
        htmlString+='<p><button id="reviewButton">Write a review</button></p>';
        htmlString+='<div id="reviewDiv">';
        htmlString+='<p><textarea id="reviewTextArea"></textarea></p>';
        htmlString+='<p><button id="postReview">Post Review</button></p>';
        htmlString+='<p><button id="cancel">Cancel</button></p>';
        htmlString+='</div>';
        everythingAboutBook.innerHTML=htmlString;

        var whereMyReviewsAt=document.getElementById("whereMyReviewsAt");
        whereMyReviewsAt.innerHTML='';
        var htmlString2='<div class="individualReview"><H1>REVIEWS:</H1></div>';
        for(i=0;i<bookData.Review.length;i++)
        {
            htmlString2+='<div class="individualReview"><div class="usersFound">';
            htmlString2+='<img src="'+bookData.Review[i].userPhoto+'">';
            htmlString2+='<p class="text">'+bookData.Review[i].userName+'</p></div>';
            htmlString2+='<p><textarea class="userReviewsTextArea" readonly>'+bookData.Review[i].userReview+'</textarea></p><br><br></div>';
        }
        whereMyReviewsAt.innerHTML=htmlString2;
    };
    xmlhttp.send("1");
    
}
