var gold={
    Gold:0,
    coinProduction:1,
    coinUpgradeCost:30,
    coinUpgradeEffect:1
}


class Worker{
    constructor(name, number,canBeUpgraded){
        this.name=name;
        this.number=number;
        this.upgrade=name+'Upgrade';
        this.canBeUpgraded=canBeUpgraded;
    }
}

var refugee= new Worker("Refugee", 0,false);
var peasant= new Worker("Peasant", 0,true);
var hunter= new Worker("Hunter", 0,true);
var lumberjack= new Worker("Lumberjack", 0,true);
var miner= new Worker("Miner", 0,true);
var mason= new Worker("Mason", 0,true);
var blacksmith= new Worker("Blacksmith", 0,true);
var goldsmith= new Worker("Goldsmith", 0,true);
var armourer= new Worker("Armourer", 0,true);
var horse= new Worker("Horse", 0,true);
var merchant= new Worker("Merchant", 0,true);


var workerList=[refugee,peasant,hunter,lumberjack,miner,mason,blacksmith,goldsmith,armourer,horse,merchant];


class Soldier{

        constructor(name, number,canBeUpgraded){
        this.name=name;
        this.number=number;
        this.upgrade=name+'Upgrade';
        this.canBeUpgraded=canBeUpgraded;
    }

}

var rabble= new Soldier("Rabble",0,false);
var militia= new Soldier("Militia",0,true);
var archer= new Soldier("Archer",0,true);
var crossbowman= new Soldier("Crossbowman",0,true);
var arbalest= new Soldier("Arbalest",0,true);
var musketeer= new Soldier("Musketeer",0,true);
var axeman= new Soldier("Axeman",0,true);
var spearman= new Soldier("Spearman",0,true);
var pikeman= new Soldier("Pikeman",0,false);
var builder= new Soldier("Builder",0,false);
var engineer= new Soldier("Engineer",0,false);
var ballista= new Soldier("Ballista",0,true);
var maceman= new Soldier("Maceman",0,true);
var catapult= new Soldier("Catapult",0,true);
var warhammer= new Soldier("Warhammer",0,true);
var swordsman= new Soldier("Swordsman",0,true);
var lCav= new Soldier("Light_Cav",0,true);
var hCav= new Soldier("Heavy_Cav",0,true);
var cannon= new Soldier("Cannon",0,true);

var soldierList=[rabble,militia,archer,crossbowman,arbalest,musketeer,axeman,spearman,pikeman,builder, engineer, ballista,
maceman,catapult,warhammer, swordsman,lCav,hCav,cannon];

