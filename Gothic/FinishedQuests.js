window.onload=function(){
    var solvedDiv=document.getElementById("solvedDiv");
    var failedDiv=document.getElementById("failedDiv");
    
    var button=document.getElementsByClassName("butoane");
    button[0].onclick=function(){
        solvedDiv.style.visibility="visible";
        failedDiv.style.visibility="hidden";
    }
    button[1].onclick=function(){
        solvedDiv.style.visibility="hidden";
        failedDiv.style.visibility="visible";
    }
    };
    