var app=angular.module("myApp",[]);
app.controller("myCtrl",function($scope){
    $scope.score=0;
    $scope.clickedButton='';

    $scope.reduceCoin=function(cine){
        var button=document.getElementById(cine);
            button.style.width="18vmin";
            button.style.height="18vmin";
            button.style.backgroundSize="18vmin 18vmin";
            $scope.clickedButton=cine;

        };

    $scope.reduceCoinUpgrade=function(cine){
        var button=document.getElementById(cine);
        button.style.width="14vw";
        button.style.height="4.5vh";
        button.style.backgroundSize="14vw 4.5vh";
        button.style.fontSize="1.5vw";
        $scope.clickedButton=cine;
        console.log("S-a redus");
    }

    $scope.resizeButton=function(){
        var button=document.getElementById($scope.clickedButton);
        console.log($scope.clickedButton);
        if($scope.clickedButton=="coin"){
            button.style.width="20vmin";
            button.style.height="20vmin";
            button.style.backgroundSize= "20vmin 20vmin";
        }
        else if($scope.clickedButton=="coinUpgrade"){
            button.style.width="15.6vw";
            button.style.height="5.1vh";
            button.style.backgroundSize="15.6vw 5.1vh";
            button.style.fontSize="1.7vw";
            console.log("S-a refacut");
        }
    };

    $scope.addGold=function(){
        $scope.score+=1;
    }

});