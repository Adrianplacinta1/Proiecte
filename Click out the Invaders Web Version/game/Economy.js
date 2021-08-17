var app=angular.module("myApp",['ngSanitize']);
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

    $scope.reduceButton=function(cine){
        var button=document.getElementById(cine);
        button.style.width="5vmin";
        button.style.height="5vmin";
        button.style.backgroundSize="5vmin 5vmin";
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
            if($scope.clickedButton==$scope.workers[i].name ||$scope.clickedButton==$scope.workers[i].upgrade){
                button.style.width="6vmin";
                button.style.height="6vmin";
                button.style.backgroundSize="6vmin 6vmin";
                return;
            }

        }

        for(i=0;i<$scope.soldiers.length;i++){
            if($scope.clickedButton==$scope.soldiers[i].name ||$scope.clickedButton==$scope.soldiers[i].upgrade){
                button.style.width="6vmin";
                button.style.height="6vmin";
                button.style.backgroundSize="6vmin 6vmin";
                return;
            }

        }
    };

    $scope.gold=gold;

    $scope.addGold=function(){
        $scope.score+=$scope.gold.coinProduction;
    }

    $scope.workers=workerList;

    $scope.buyWorker=function(x){
        x.number+=1;
    }

    $scope.soldiers=soldierList;    

    //.......................................PARTEA DE UMPLUT INFO BOX.....................................

    $scope.infoBoxContent="";

    $scope.infoBox=function(x){


        if(x=='coin'){
            $scope.infoBoxContent="Magic Gold Coin  <br> <br> Each click gives you"+$scope.gold.coinProduction+ "gold";
            return
        }
            for(i=0;i<$scope.workers.length;i++){
                if(x==$scope.workers[i].name){
                    $scope.infoBoxContent=$scope.workers[i].name;
                    return;
                }
                else if(x==$scope.workers[i].upgrade){
                    $scope.infoBoxContent=$scope.workers[i].name+ " Upgrade";
                    return;
                }
    
            }

            for(i=0;i<$scope.soldiers.length;i++){
                if(x==$scope.soldiers[i].name){
                    $scope.infoBoxContent=$scope.soldiers[i].name;
                    return;
                }
                else if(x==$scope.soldiers[i].upgrade){
                    $scope.infoBoxContent=$scope.soldiers[i].name+ " Upgrade";
                    return;
                }
    
            }

            $scope.infoBoxContent="INFO BOX <br><br> Place mouse over something to find out what it does";
    }
});