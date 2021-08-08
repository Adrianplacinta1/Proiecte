var app=angular.module("myApp",[]);
app.controller("myCtrl",function($scope){
    $scope.score=0;
    $scope.clickedButton='';
    $scope.workers=['refugeeButton','peasantButton']

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

    $scope.reduceButton=function(cine){
        var button=document.getElementById(cine);
        button.style.width="3.4vmin";
        button.style.height="3.4vmin";
        button.style.backgroundSize="3.4vmin 3.4vmin";
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

        for(i=0;i<$scope.workers.length;i++){
            if($scope.clickedButton==$scope.workers[i].name){
                button.style.width="3.7vmin";
                button.style.height="3.7vmin";
                button.style.backgroundSize="3.7vmin 3.7vmin";
                return;
            }

        }
    };

    $scope.addGold=function(){
        $scope.score+=1;
    }

    $scope.workers=workerList;

    $scope.buyWorker=function(x){
        x.number+=1;
        console.log(workerList[0].number)
    }

});