#include <iostream>
#include<graphics.h>
#include<winbgim.h>
#include<windows.h>
#include<math.h>
#include<cstdlib>
#include<time.h>

using namespace std;

void menu();      //declararea functiilor utilizate
void instructiuni();
void NumerotareChenare();
int DetectChenar();
void clickMenu(bool &startGame);
void numerotarePatrate();
void numerotareTablaJoc();
void setupJoc();
short inPatrat();
short inPatratMarcat();
void selectPatrat(short &nrP,short &z);
void selectPatratMarcat(short &nrP,short &z);
void colorarePatrat(int nrP);
void marcare(short p1);
void mutariBasic(short p1);
void mutariAvansate(short p1);
void mutare_Alb();
void mutare_Negru();
void endGame(bool &gameOver);
void playerVSplayer();
void playerVScomputer(char dificultate);
void computerVScomputer(char dificultAlb, char dificultNegru);
void mutare_Calculator(short culoare, char dificultate);
short fP1N_Easy();
short fP1A_Easy();
short fP1N_Hard();
short fP1A_Hard();
short fP2N(short &p1);
short fP2A(short& p1);


struct patrat{        //declaram tipul de date patrat
short x1,x2,y1,y2;      //limitele patratului
short nrPatrat,culoare;};       //numarul patratului, culoarea patratului
patrat p[10][10];

void menu()                       //functia care deseneaza meniul
{ initwindow(900,700);
  char c1[]="Two players", c2[]="Player VS Easy AI", c3[]="Player VS Hard AI";
  char c4[]="Easy AI vs Easy AI",c5[]="Easy AI vs Hard AI", c6[]="Hard AI vs Hard AI";
  char c7[]="INSTRUCTIUNI";       //textul ce trebuie afisat

  settextstyle(4,0,4);            //afisarea textului
  outtextxy(320,100,c1);
  outtextxy(260,175,c2);
  outtextxy(260,250,c3);
  outtextxy(260,325,c4);
  outtextxy(260,400,c5);
  outtextxy(260,475,c6);
  outtextxy(285,550,c7);

  for(int y=150;y<=575;y=y+75)     //separam optiunile cu linii orizontale, lasand 75 de pixeli distanta intre ele
  line(1,y,900,y);

}


void instructiuni()                //functia ce afiseaza instructiunile
{
    char r1[]="Instructiuni";
    char r2[]="Pentru a castiga, jucatorul trebuie sa isi duca piesele ";
    char r3[]="in pozitia in care se aflau la inceput piesele inamicului.";
    char r4[]="Se pot executa doua tipuri de mutari:";
    char r5[]="-mutari elementare: pe un patratel vecin, in orice directie";
    char r6[]="-mutari avansate: in care se sare peste o piesa adiacenta.";
    char r7[]="Mutarile avansate pot fi executate in lant:";
    char r7punct1[]="Daca, sarind peste o piesa, se ajunge in vecinatatea alteia,";
    char r7punct2[]="se poate sari si peste aceasta piesa si urmatoarea samd...";
    char r8[]="Selectati o piesa folosind click-stanga si toate mutarile";
    char r9[]="posibile vor aparea marcate cu o bulina rosie.";
    char r10[]="Apasati click-stanga pentru a reveni la meniu.";    //textul ce trebuie afisat

    initwindow(900,700);

    settextstyle(0,0,5);     //titlul e scris in dimensiune mai mare
    outtextxy(215,20,r1);

    settextstyle(0,0,2);     //celelalte randuri
    outtextxy(75,100,r2);
    outtextxy(50,125,r3);
    outtextxy(75,200,r4);
    outtextxy(65,225,r5);
    outtextxy(65,250,r6);
    outtextxy(75,325,r7);
    outtextxy(50,350,r7punct1);
    outtextxy(50,375,r7punct2);
    outtextxy(75,450,r8);
    outtextxy(50,475,r9);
    outtextxy(75,550,r10);

    while(!ismouseclick(WM_LBUTTONDOWN));  //instructiune repetitiva ce va rula cat timp nu dam click stanga
    clearmouseclick(WM_LBUTTONDOWN);

    closegraph(ALL_WINDOWS);    //cand iesim din while fereastra se inchide
    menu();                     //si ne intoarcem in meniul principal
}

int DetectChenar()             //detecteaza in care chenar am dat click
{
    float y;
    y=mousey();               //ne folosim de coordonata y

    if(y<150)
        return 1;
    else if(y<225)
        return 2;
    else if(y<300)
        return 3;
    else if(y<375)
        return 4;
    else if(y<450)
        return 5;
    else if(y<525)
        return 6;
    else return 7;
}

void clickMenu(bool &startGame)    //functia de selectare a unei optiuni din meniu
{ int x;
    while(!startGame)
    {
        if(ismouseclick(WM_LBUTTONDOWN))   //cand dam click
        {
            x=DetectChenar();             //detectam in ce chenar suntem
            if(x==1)                      //in primul
                {
                    startGame=1;
                    closegraph(ALL_WINDOWS);   //stergem meniul
                    playerVSplayer();            //pornim jocul  in 2
                }
            else if(x==2) //in al doilea
                {
                    startGame=1;
                    closegraph(ALL_WINDOWS);
                    playerVScomputer('e');       //pornim modul vs calculator 'e'=easy
                }
            else if(x==3) //in al treilea
            {
                startGame=1;
                closegraph(ALL_WINDOWS);
                playerVScomputer('h');          //'h'=hard
            }
            else if(x==4) //in al treilea
            {
                startGame=1;
                closegraph(ALL_WINDOWS);
                computerVScomputer('e','e');   //easy vs easy
            }
            else if(x==5) //in al treilea
            {
                startGame=1;
                closegraph(ALL_WINDOWS);
                computerVScomputer('e','h');    //easy vs hard
            }
            else if(x==6) //in al treilea
            {
                startGame=1;
                closegraph(ALL_WINDOWS);
                computerVScomputer('h','h');   //hard vs hard
            }
            else if(x==7) //in al patrulea
                {
                closegraph(ALL_WINDOWS);
                instructiuni();}               //afisam instructiunile
            else clearmouseclick(WM_LBUTTONDOWN);
        }
    }
    clearmouseclick(WM_LBUTTONDOWN);
}


void numerotarePatrate()   //stabilim coordonatele,culoarea si numarul fiecarui patrat
{
    int i,j,x,y=77;    //primul patrat are limita superioara 77
    for(i=1;i<=8;i++)
    {
        x=152;             //primul patrat are limita stanga 152
        for(j=1;j<=8;j++)
        {
            p[i][j].x1=x;
            p[i][j].x2=x+73;   //limita dreapta e la 73 pixeli distanta de cea stanga
            x=x+75;            //latura unui patrat, cu tot cu linii, este de 75
            p[i][j].y1=y;
            p[i][j].y2=y+73;
            p[i][j].nrPatrat=10*i+j;
            p[i][j].culoare=9;   //culoarea patratelor libere.
        }
        y=y+75;               //latura unui patrat, cu tot cu linii, este de 75
    }
    p[1][6].culoare=p[1][7].culoare=p[1][8].culoare=0;
    p[2][7].culoare=p[2][8].culoare=p[3][8].culoare=0;  //pt patratele negre, culoarea este 0;

    p[6][1].culoare=p[7][1].culoare=p[7][2].culoare=15;
    p[8][1].culoare=p[8][2].culoare=p[8][3].culoare=15; //pt patratele albe, culoarea este 15
}

void numerotareTablaJoc()
{
    char A[]="A",B[]="B",C[]="C",D[]="D",E[]="E",F[]="F",G[]="G",H[]="H";
    char I[]="1",II[]="2",III[]="3",IV[]="4",V[]="5",VI[]="6",VII[]="7",VIII[]="8";
          //Am declarat siruri de caractere cu literele si numerele.

    setcolor(4);
    settextstyle(0,0,5);
    outtextxy(170,10,A);
    outtextxy(245,10,B);
    outtextxy(320,10,C);
    outtextxy(395,10,D);
    outtextxy(470,10,E);
    outtextxy(545,10,F);
    outtextxy(620,10,G);
    outtextxy(695,10,H);
    outtextxy(95,95,I);
    outtextxy(95,170,II);
    outtextxy(95,245,III);
    outtextxy(95,320,IV);
    outtextxy(95,395,V);
    outtextxy(95,470,VI);
    outtextxy(95,545,VII);
    outtextxy(95,620,VIII);
    //Am plasat fiecare caracter in pozitia corespunzatoare.
}

void setupJoc()   //functia ce deseneaza tabla si aseaza piesele
{
   initwindow(900,700);   //creem o fereastra
   setfillstyle(1,9);
   floodfill(10,10,3);   //o coloram cu albastru deschis

   setcolor(1);
   int i,k=150;
     for(i=1;i<=9;i++)  //desenam tabla de joc
   {line(k,75,k,675);   //liniile verticale
     k=k+75;}
     k=75;
     for(i=1;i<=9;i++)
     {
         line(150,k,750,k);  //liniile orizontale
         k=k+75;
     }

     setfillstyle(1,15);   //coloram cu alb 6 patrate din coltul stanga-jos
     floodfill(200,650,1);
     floodfill(250,650,1);
     floodfill(350,650,1);
     floodfill(200,550,1);
     floodfill(250,550,1);
     floodfill(200,480,1);

     setfillstyle(1,0);      //coloram cu negru 6 patrate din coltul dreapta-sus
     floodfill(550,100,1);
     floodfill(650,100,1);
     floodfill(700,100,1);
     floodfill(650,180,1);
     floodfill(700,180,1);
     floodfill(700,250,1);
     numerotareTablaJoc();
     numerotarePatrate();
}

short inPatrat()      //testeaza daca suntem cu mouse-ul intr-un patrat
{
    short i,j,x,y;
    x=mousex();
    y=mousey();    //se inregistreaza coordonatele mouse-ului
    for(i=1;i<=8;i++)
        for(j=1;j<=8;j++)
    {
        if(y>=p[i][j].y1&&y<=p[i][j].y2&&x>=p[i][j].x1&&x<=p[i][j].x2)  //se compara cu extremitatile fiecaui patrat
                return short(10*i+j);     //daca ne aflam in patrat, returnam numarul patratului
    }
    return 0;
}

short inPatratMarcat()      //testeaza daca suntem cu mouse-ul intr-un patrat in care se poate muta
{
    short i,j,x,y;
    x=mousex();
    y=mousey();    //se inregistreaza coordonatele mouse-ului
    for(i=1;i<=8;i++)
        for(j=1;j<=8;j++)
    {
        if(y>=p[i][j].y1&&y<=p[i][j].y2&&x>=p[i][j].x1&&x<=p[i][j].x2)  //se compara cu extremitatile fiecaui patrat
        if(getpixel((p[i][j].x1+p[i][j].x2)/2,(p[i][j].y1+p[i][j].y2)/2)==4)  //se verifica daca centrul patratului este rosu (marcat)
                return short(10*i+j);     //daca ne aflam im patrat, returnam numarul patratului
    }
    return 0;
}

void selectPatrat(short &nrP,short &z)    //functia de selectare a unui patrat
{
    if(ismouseclick(WM_LBUTTONDOWN)&&(nrP=inPatrat()))  //daca am dat click intr-un patrat, inregistram numarul lui
        {z=p[nrP/10][nrP%10].culoare;     //inregistram culoarea patratului
          clearmouseclick(WM_LBUTTONDOWN);}

    else if(ismouseclick(WM_LBUTTONDOWN)&&!inPatrat())   //daca am dat click inafara
        clearmouseclick(WM_LBUTTONDOWN);    //resetam functia de click-stanga
}

void selectPatratMarcat(short &nrP,short &z)   //functia de mutare a piesei
{
    if(ismouseclick(WM_LBUTTONDOWN)&&(nrP=inPatratMarcat()))  //daca am dat click intr-un patrat, inregistram numarul lui
        {z=9;    //inregistram culoarea patratului
        clearmouseclick(WM_LBUTTONDOWN);}

    else if(ismouseclick(WM_LBUTTONDOWN)&&!inPatratMarcat())   //daca am dat click inafara
        clearmouseclick(WM_LBUTTONDOWN);    //resetam functia de click-stanga
}

void colorarePatrat(int nrP)    //functie pt a colora un singur patrat specificat
{
    setfillstyle(1,p[nrP/10][nrP%10].culoare);
    floodfill(p[nrP/10][nrP%10].x1+5,p[nrP/10][nrP%10].y1+5,1);
}

void marcare(short p1)    //functie pt a marca un patrat in care putem muta piesa
{
    int x=(p[p1/10][p1%10].x1+p[p1/10][p1%10].x2)/2;     //x-ul punctului din mijloc
    int y=(p[p1/10][p1%10].y1+p[p1/10][p1%10].y2)/2;     //y-ul punctului din mijloc
    setcolor(4);
    circle(x,y,5);
    setfillstyle(1,4);
    floodfill(x,y,4);   //desenam o bulina rosie in mijlocul patratului
}

void mutariBasic(short p1)   //mutarile in patratele adiacente
{
        short i1=p1/10;
    short j1=p1%10;       //stabilim linia si coloana pe care se afla patratul selectat
    short i2,j2;
    for(i2=i1-1;i2<=i1+1;i2++)      //liniile adiacente
        for(j2=j1-1;j2<=j1+1;j2++)  //coloanele adiacente
        if(p[i2][j2].culoare==9)    //patratele adiacente trebuie sa fie libere (culoarea 9)
            marcare(p[i2][j2].nrPatrat);   //le marcam
}

void mutariAvansate(short p1)    //mutarile cu salt
{
    short i1=p1/10;
    short j1=p1%10;      //stabilim linia si coloana pe care se afla patratul selectat
    short i2,j2,i3,j3;
    for(i2=i1-1;i2<=i1+1;i2++)     //liniile adiacente
        for(j2=j1-1;j2<=j1+1;j2++)  //coloanele adiacente
    {
         if(p[i2][j2].culoare!=9&&p[i2][j2].nrPatrat!=p1)  //stabilim daca exista o piesa pe un patrat adiacent
         {
             i3=i2+(i2-i1);
             j3=j2+(j2-j1);       //stabilim x-ul si y-ul potentialului patrat de destinatie
             if(i3>0&&i3<9&&j3>0&&j3<9)      //verificam daca destinatia se gaseste in matrice
                if(getpixel((p[i3][j3].x1+p[i3][j3].x2)/2,(p[i3][j3].y1+p[i3][j3].y2)/2)==9)   //verificam daca destinatia e libera
             {
             marcare(p[i3][j3].nrPatrat);  //marcam destinatia
             mutariAvansate(i3*10+j3);     //apelam recursiv aceasta functie, intrucat mutarile avansate se pot executa in lant
             }
         }
    }
}

void mutare_Alb()
{
    short color1=-1,color2=-1,p1,p2;   //avem nevoie de 2 patrate si culorile lor

     while(color1!=15){              //cat timp nu am obtinut prima culoare
        selectPatrat(p1,color1);     //incercam sa selectam
        if(color1==15){              //daca am reusit
        setfillstyle(8,2);           //schimbam fill-ul lui p1, pt a evidentia ca a fost selectat
        floodfill(p[p1/10%10][p1%10].x1,p[p1/10%10][p1%10].y1,1);}}
    clearmouseclick(WM_LBUTTONDOWN);   //resetam functia de click-stanga

    mutariBasic(p1);
    mutariAvansate(p1);          //indicam unde se poate muta

    while(color2==-1)            //la fel pt al doilea patrat, dar nu schimbam fill-ul
        selectPatratMarcat(p2,color2);
    clearmouseclick(WM_LBUTTONDOWN);

    p[p1/10][p1%10].culoare=color2;
    p[p2/10][p2%10].culoare=color1;   //inversam culorile celor 2 patrate in structura de date

    colorarePatrat(p1);
    colorarePatrat(p2);         //schimbam culorile lor pe tabla de joc

        for(int i=1;i<=8;i++)
        for(int j=1;j<=8;j++)
        if(p[i][j].culoare==9)
        colorarePatrat(p[i][j].nrPatrat); //stergem bulinele rosii din patratele marcate

}
void mutare_Negru()
{
    short color1=-1,color2=-1,p1,p2;   //avem nevoie de 2 patrate si culorile lor

     while(color1!=0){              //cat timp nu am obtinut prima culoare
        selectPatrat(p1,color1);     //incercam sa selectam
        if(color1==0){              //daca am reusit
        setfillstyle(8,2);           //schimbam fill-ul lui p1, pt a evidentia ca a fost selectat
        floodfill(p[p1/10%10][p1%10].x1,p[p1/10%10][p1%10].y1,1);}}
    clearmouseclick(WM_LBUTTONDOWN);   //resetam functia de click-stanga
    mutariBasic(p1);
    mutariAvansate(p1);               //indicam unde se poate muta

    while(color2==-1)            //la fel pt al doilea patrat, dar nu schimbam fill-ul
        selectPatratMarcat(p2,color2);
    clearmouseclick(WM_LBUTTONDOWN);

    p[p1/10][p1%10].culoare=color2;
    p[p2/10][p2%10].culoare=color1;   //inversam culorile celor 2 patrate in structura de date

     colorarePatrat(p1);
     colorarePatrat(p2);             //schimbam culorile lor pe tabla de joc

     for(int i=1;i<=8;i++)
        for(int j=1;j<=8;j++)
        if(p[i][j].culoare==9)
        colorarePatrat(p[i][j].nrPatrat);   //stergem bulinele rosii din patratele marcate
}

void endGame(bool &gameOver)   //verificam daca a castigat cineva
{
    char congratsN[]="Castigator: negru", congratsA[]="Castigator: alb", remiza[]="Remiza";
    bool a=0,n=0;

    if(p[6][1].culoare==0&&p[7][1].culoare==0&&p[7][2].culoare==0&&p[8][1].culoare==0&&p[8][2].culoare==0&&p[8][3].culoare==0)
        {n=1; gameOver=true;}   //verificam daca a terminat jucatorul cu negru


    if(p[1][6].culoare==15&&p[1][7].culoare==15&&p[1][8].culoare==15&&p[2][7].culoare==15&&p[2][8].culoare==15&&p[3][8].culoare==15)
        {a=1; gameOver=true;}  //verificam daca a terminat jucatorul cu alb

    if(a&&n)        //daca au terminat amandoi
    {
        setcolor(4);
        settextstyle(0,3,4);
        outtextxy(800,275,remiza);  //declaram remiza
    }
    else if(!a&&n)    //daca a terminat doar negru
    {
        setcolor(4);
        settextstyle(0,3,4);
        outtextxy(800,100,congratsN);   //felicitam jucatorul cu negru
    }
    else if(a&&!n)    //daca a terminat doar alb
    {
        setcolor(4);
        settextstyle(0,3,4);
        outtextxy(800,125,congratsA);  //felicitam jucatorul cu alb
    }
}

void playerVSplayer()
{
    bool gameOver=0;
        setupJoc();            //initializam jocul
    while(!gameOver)       //efectuam mutari cat timp gameOver este 0
    {
         mutare_Alb();
         mutare_Negru();
         endGame(gameOver);   //verificam daca a castigat cineva
    }
}

void playerVScomputer(char dificultate)
{
    bool gameOver=0;
    setupJoc();           //initializam jocul
    while(!gameOver)      //efectuam mutari cat timp gameOver este 0
    {
        mutare_Alb();
        mutare_Calculator(0,dificultate);       //calculatorul joaca cu negru (0)
        endGame(gameOver);    //verificam daca a castigat cineva
    }
}

void computerVScomputer(char dificultAlb, char dificultNegru)
{
    bool gameOver=0;
    setupJoc();           //initializam jocul
    while(!gameOver)      //efectuam mutari cat timp gameOver este 0
    {
        mutare_Calculator(15,dificultAlb);      //calculatorul cu alb
        mutare_Calculator(0,dificultNegru);     //calculatorul cu negru
        endGame(gameOver);    //verificam daca a castigat cineva
    }
}

int main()
{
    bool startGame;
    PlaySound("Stronghold_Legends.wav",NULL,SND_ASYNC | SND_LOOP);   //instructiunea care porneste muzica
    startGame=0;       //variabila ce va deveni 1 cand alegem un mod de joc
    srand(time(NULL));  //setam functia de randomizare, folosita de AI pt a muta piesele
    menu();             //afisam meniul jocului

    while(!startGame)   //cat timp nu s-a ales un mod de joc
     clickMenu(startGame);    //rulam functia ce permite sa alegem ceva din meniu
    getch();
    return 0;
}

void mutare_Calculator(short culoare,char dificultate)
{
    Sleep(500);       //pauza jumatate de secunda, pentru ca selectarea piesei sa nu fie brusca
    short i,j,p1,p2;

    if(dificultate=='e')     //pentru modul easy
        {
    if(culoare==0)
    p1=fP1N_Easy();         //functia de alegere pt negru, easy
    else p1=fP1A_Easy();}   //functia de alegere pt alb, easy

    else if(dificultate=='h')  //pentru modul hard
    {
        if(culoare==0)
            p1=fP1N_Hard();
        else p1=fP1A_Hard();
    }

    mutariBasic(p1);
    mutariAvansate(p1);          //marcam mutarile posibile

    setfillstyle(8,2);           //schimbam fill-ul lui p1, pt a evidentia ca a fost selectat
    floodfill(p[p1/10][p1%10].x1+5,p[p1/10][p1%10].y1+5,1);
    Sleep(1500);                 //pauza o secunda, pt ca jucatorul uman sa inteleaga cum muta AI-ul

    if(culoare==0)
    p2=fP2N(p1);                  //AI-ul va alege unde muta piesa
    else p2=fP2A(p1);

    short aux;
    aux=p[p1/10][p1%10].culoare;
    p[p1/10][p1%10].culoare=p[p2/10][p2%10].culoare;
    p[p2/10][p2%10].culoare=aux;          //inversam culorile celor 2 patrate in structura de date

    colorarePatrat(p1);
    colorarePatrat(p2);                   //inversam culorile pe tabla de joc

    for(i=1;i<=8;i++)
        for(j=1;j<=8;j++)
        if(getpixel((p[i][j].x1+p[i][j].x2)/2,(p[i][j].y1+p[i][j].y2)/2)==4)   //stergem bulinele rosii din patratele marcate
           colorarePatrat(10*i+j);
}

short fP1N_Hard()       //folosita de AI-ul  hard,cu negru
{
    short i,j,n,p1=0;
        for(i=8;i>=1;i--){       //alegerea se face parcurgand matricea...
            for(j=8;j>=1;j--){
                 n=10*j+i;       //...pe coloane, de jos in sus
            if(p[j][i].culoare==0&&n!=81&&n!=82&&n!=83&&n!=71&&n!=72)  //daca patratul rezultat e negru si nu e intr-o pozitie castigatoare
                {p1=p[j][i].nrPatrat;
                break;}}
            if(p1)
                break;}
        return p1;
}
short fP1A_Hard()       //folosita de AI-ul hard cu alb
{
    short i,j,n,p1=0;
        for(i=1;i<=8;i++){              //alegerea se face parcurgand matricea...
            for(j=1;j<=8;j++){
                 n=10*j+i;              //...pe coloane, de sus in jos
            if(p[j][i].culoare==15&&n!=18&&n!=17&&n!=16&&n!=28&&n!=27)  //daca patratul rezultat e negru si nu e intr-o pozitie castigatoare
                {p1=p[j][i].nrPatrat;
                break;}}
            if(p1)
                break;}
        return p1;
}
short fP1A_Easy()       //folosita de AI-ul usor cu alb pt a-si alege o piesa
{
    short i,j,n,p1=0;
        while(p1==0)        //cat timp nu s-a ales o piesa
        {
            i=rand()%8+1;
            j=rand()%8+1;   //generam nr aleatorii pt linie si coloana
            n=10*i+j;
            if(p[i][j].culoare==15&&n!=18&&n!=17&&n!=16&&n!=28&&n!=27)  //daca patratul rezultat e negru si nu e intr-o pozitie castigatoare
                p1=p[i][j].nrPatrat;
        }
        return p1;
}
short fP1N_Easy()       //folosita de AI-ul usor cu negru pt a-si alege o piesa
{
    short i,j,n,p1=0;
        while(p1==0)        //cat timp nu s-a ales o piesa
        {
            i=rand()%8+1;
            j=rand()%8+1;   //generam nr aleatorii pt linie si coloana
            n=10*i+j;
            if(p[i][j].culoare==0&&n!=81&&n!=82&&n!=83&&n!=71&&n!=72)  //daca patratul rezultat e negru si nu e intr-o pozitie castigatoare
                p1=p[i][j].nrPatrat;
        }
        return p1;
}

short fP2N(short& p1)   //folosita de AI-ul cu negru pt a muta o piesa
{
    short i,j,p2=0;
      //pozitiile castigatoare au prioritate, incercam intai sa mutam acolo
    if(getpixel((p[8][3].x1+p[8][3].x2)/2,(p[8][3].y1+p[8][3].y2)/2)==4)
        return 83;
    if(getpixel((p[8][2].x1+p[8][2].x2)/2,(p[8][2].y1+p[8][2].y2)/2)==4)
        return 82;
    if(getpixel((p[8][1].x1+p[8][1].x2)/2,(p[8][1].y1+p[8][1].y2)/2)==4)
        return 81;
    if(getpixel((p[7][1].x1+p[7][1].x2)/2,(p[7][1].y1+p[7][1].y2)/2)==4)
        return 71;
    if(getpixel((p[7][2].x1+p[7][2].x2)/2,(p[7][2].y1+p[7][2].y2)/2)==4)
        return 72;
    if(getpixel((p[6][1].x1+p[6][1].x2)/2,(p[6][1].y1+p[6][1].y2)/2)==4)
        return 61;
       //daca nu s-a reusit pe o pozitie finala
    if(p1/10<=5&&p1%10<=2)   //piesele au tendinta sa se blocheze in portiunea de stanga-sus
    {
        for(i=8;i>=1;i--){
            for(j=8;j>=1;j--)   //le deblocam, mutandu-le pe directia dreapta-jos
            if(getpixel((p[j][i].x1+p[j][i].x2)/2,(p[j][i].y1+p[j][i].y2)/2)==4)  //verificam daca patratul e marcat
            {
            p2=p[j][i].nrPatrat;
            break;     //daca gasim un patrat, iesim din primul for
            }
            if(p2)
                break;}}         //si din al doilea for

    else{                        //modul standard de a muta, pe directia stanga-jos, inspre pozitiile castigatoare
            for(i=1;i<=8;i++){
            for(j=8;j>=1;j--)
            if(getpixel((p[j][i].x1+p[j][i].x2)/2,(p[j][i].y1+p[j][i].y2)/2)==4)
            {
            p2=p[j][i].nrPatrat;
            break;}
            if(p2)
                break;
    }}
        return p2;
}

short fP2A(short& p1)   //folosita de AI-ul cu alb pt a muta o piesa
{
    short i,j,p2=0;
      //pozitiile castigatoare au prioritate, incercam intai sa mutam acolo
    if(getpixel((p[1][6].x1+p[1][6].x2)/2,(p[1][6].y1+p[1][6].y2)/2)==4)
        return 16;
    if(getpixel((p[1][7].x1+p[1][7].x2)/2,(p[1][7].y1+p[1][7].y2)/2)==4)
        return 17;
    if(getpixel((p[1][8].x1+p[1][8].x2)/2,(p[1][8].y1+p[1][8].y2)/2)==4)
        return 18;
    if(getpixel((p[2][8].x1+p[2][8].x2)/2,(p[2][8].y1+p[2][8].y2)/2)==4)
        return 28;
    if(getpixel((p[2][7].x1+p[2][7].x2)/2,(p[2][7].y1+p[2][7].y2)/2)==4)
        return 27;
    if(getpixel((p[3][8].x1+p[3][8].x2)/2,(p[3][8].y1+p[3][8].y2)/2)==4)
        return 38;
       //daca nu s-a reusit pe o pozitie finala
    if(p1/10>=4&&p1%10>=7)   //piesele au tendinta sa se blocheze in portiunea de dreapta-jos
    {
        for(i=1;i<=8;i++){
            for(j=1;j<=8;j++)   //le deblocam, mutandu-le pe directia stanga-sus
            if(getpixel((p[j][i].x1+p[j][i].x2)/2,(p[j][i].y1+p[j][i].y2)/2)==4)  //verificam daca patratul e marcat
            {
            p2=p[j][i].nrPatrat;
            break;     //daca gasim un patrat, iesim din primul for
            }
            if(p2)
                break;}}         //si din al doilea for

    else{                        //modul standard de a muta, pe directia dreapta-sus, inspre pozitiile castigatoare
            for(i=8;i>=1;i--){
            for(j=1;j<=8;j++)
            if(getpixel((p[j][i].x1+p[j][i].x2)/2,(p[j][i].y1+p[j][i].y2)/2)==4)
            {
            p2=p[j][i].nrPatrat;
            break;}
            if(p2)
                break;
    }}
        return p2;
}
