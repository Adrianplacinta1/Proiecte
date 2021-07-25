window.onload=function(){
var searchButton=document.getElementById("searchButton");
var results=document.getElementById("results");
var createNewGroupButton=document.getElementById("createNewGroupButton");
var newGroup=document.getElementById("newGroup");
var cancel = document.getElementById("cancel");

searchButton.addEventListener("click",function(){
    var groupName=document.getElementById("typeGroupName");                  //preluam ce a scris userul
    console.log(groupName.value);


    var findGroupRequest = new XMLHttpRequest();                        //facem un request
    findGroupRequest.open('POST', '/findGroupRequest');
    findGroupRequest.setRequestHeader("Content-Type", "application/javascript");
    findGroupRequest.onload = function () {
        console.log(findGroupRequest.responseText);
        results.innerHTML='';
        results.innerHTML=findGroupRequest.responseText;
        results.style.display="flex";
    };

    findGroupRequest.send(groupName.value);    //trimitem doar ce a scris userul, nu e nevoie de obiect, JSON, etc

});

createNewGroupButton.addEventListener("click",function(){
    newGroup.style.display="flex";
});

cancel.addEventListener("click",function(){
    newGroup.style.display="none";
});

};

window.onclick=function(event){
    if(event.target.matches(".viewGroupButton")){
        window.location.href="Group_Page1.1.html";
    }
}