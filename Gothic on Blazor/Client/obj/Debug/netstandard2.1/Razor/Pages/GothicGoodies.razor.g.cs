#pragma checksum "A:\Proiecte Visual Studio\Gothic\Client\Pages\GothicGoodies.razor" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "f76303591ee45db444de2f8b2dc92ff99c3fb768"
// <auto-generated/>
#pragma warning disable 1591
namespace Gothic.Client.Pages
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Components;
#nullable restore
#line 1 "A:\Proiecte Visual Studio\Gothic\Client\_Imports.razor"
using System.Net.Http;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "A:\Proiecte Visual Studio\Gothic\Client\_Imports.razor"
using System.Net.Http.Json;

#line default
#line hidden
#nullable disable
#nullable restore
#line 3 "A:\Proiecte Visual Studio\Gothic\Client\_Imports.razor"
using Microsoft.AspNetCore.Components.Forms;

#line default
#line hidden
#nullable disable
#nullable restore
#line 4 "A:\Proiecte Visual Studio\Gothic\Client\_Imports.razor"
using Microsoft.AspNetCore.Components.Routing;

#line default
#line hidden
#nullable disable
#nullable restore
#line 5 "A:\Proiecte Visual Studio\Gothic\Client\_Imports.razor"
using Microsoft.AspNetCore.Components.Web;

#line default
#line hidden
#nullable disable
#nullable restore
#line 6 "A:\Proiecte Visual Studio\Gothic\Client\_Imports.razor"
using Microsoft.AspNetCore.Components.WebAssembly.Http;

#line default
#line hidden
#nullable disable
#nullable restore
#line 7 "A:\Proiecte Visual Studio\Gothic\Client\_Imports.razor"
using Microsoft.JSInterop;

#line default
#line hidden
#nullable disable
#nullable restore
#line 8 "A:\Proiecte Visual Studio\Gothic\Client\_Imports.razor"
using Gothic.Client;

#line default
#line hidden
#nullable disable
#nullable restore
#line 9 "A:\Proiecte Visual Studio\Gothic\Client\_Imports.razor"
using Gothic.Client.Shared;

#line default
#line hidden
#nullable disable
#nullable restore
#line 10 "A:\Proiecte Visual Studio\Gothic\Client\_Imports.razor"
using Gothic.Client.Components;

#line default
#line hidden
#nullable disable
    [Microsoft.AspNetCore.Components.RouteAttribute("/GothicGoodies")]
    public partial class GothicGoodies : Microsoft.AspNetCore.Components.ComponentBase
    {
        #pragma warning disable 1998
        protected override void BuildRenderTree(Microsoft.AspNetCore.Components.Rendering.RenderTreeBuilder __builder)
        {
            __builder.AddMarkupContent(0, "<div id=\"singleImageDisplayer\">\r\n    <img id=\"largeGothicImage\">\r\n</div>\r\n");
            __builder.OpenComponent<Gothic.Client.Components.Row>(1);
            __builder.AddAttribute(2, "BackgroundImage", "../Images/goodies.png");
            __builder.CloseComponent();
            __builder.AddMarkupContent(3, "\r\n\r\n");
            __builder.AddMarkupContent(4, "<div class=\"align\">\r\n    <h1> <u style=\"font-size: 2em;\">Gothic Goodies</u></h1>\r\n</div>\r\n\r\n");
            __builder.AddMarkupContent(5, "<h2 style=\"margin-bottom: 2vh; margin-top:10vh;\"><u class=\"text\">Gothic I</u></h2>\r\n");
            __builder.OpenElement(6, "div");
            __builder.AddAttribute(7, "class", "imageDisplayer");
            __builder.AddMarkupContent(8, "\r\n");
#nullable restore
#line 15 "A:\Proiecte Visual Studio\Gothic\Client\Pages\GothicGoodies.razor"
     foreach (var image in Gothic1)
    {

#line default
#line hidden
#nullable disable
            __builder.AddContent(9, "        ");
            __builder.OpenElement(10, "img");
            __builder.AddAttribute(11, "src", 
#nullable restore
#line 17 "A:\Proiecte Visual Studio\Gothic\Client\Pages\GothicGoodies.razor"
                   image

#line default
#line hidden
#nullable disable
            );
            __builder.AddAttribute(12, "class", "gothicImage");
            __builder.CloseElement();
            __builder.AddMarkupContent(13, "\r\n");
#nullable restore
#line 18 "A:\Proiecte Visual Studio\Gothic\Client\Pages\GothicGoodies.razor"
    }

#line default
#line hidden
#nullable disable
            __builder.CloseElement();
            __builder.AddMarkupContent(14, "\r\n\r\n");
            __builder.AddMarkupContent(15, "<h2 style=\"margin-bottom: 2vh;margin-top:10vh;\"><u class=\"text\">Gothic II</u></h2>\r\n");
            __builder.OpenElement(16, "div");
            __builder.AddAttribute(17, "class", "imageDisplayer");
            __builder.AddMarkupContent(18, "\r\n");
#nullable restore
#line 23 "A:\Proiecte Visual Studio\Gothic\Client\Pages\GothicGoodies.razor"
     foreach (var image in Gothic2)
    {

#line default
#line hidden
#nullable disable
            __builder.AddContent(19, "        ");
            __builder.OpenElement(20, "img");
            __builder.AddAttribute(21, "src", 
#nullable restore
#line 25 "A:\Proiecte Visual Studio\Gothic\Client\Pages\GothicGoodies.razor"
                   image

#line default
#line hidden
#nullable disable
            );
            __builder.AddAttribute(22, "class", "gothicImage");
            __builder.CloseElement();
            __builder.AddMarkupContent(23, "\r\n");
#nullable restore
#line 26 "A:\Proiecte Visual Studio\Gothic\Client\Pages\GothicGoodies.razor"
    }

#line default
#line hidden
#nullable disable
            __builder.CloseElement();
            __builder.AddMarkupContent(24, "\r\n\r\n");
            __builder.AddMarkupContent(25, "<h2 style=\"margin-bottom: 2vh; margin-top:10vh;\"><u class=\"text\">Arcania Gothic IV</u></h2>\r\n");
            __builder.OpenElement(26, "div");
            __builder.AddAttribute(27, "class", "imageDisplayer");
            __builder.AddMarkupContent(28, "\r\n");
#nullable restore
#line 31 "A:\Proiecte Visual Studio\Gothic\Client\Pages\GothicGoodies.razor"
     foreach (var image in Gothic4)
    {

#line default
#line hidden
#nullable disable
            __builder.AddContent(29, "        ");
            __builder.OpenElement(30, "img");
            __builder.AddAttribute(31, "src", 
#nullable restore
#line 33 "A:\Proiecte Visual Studio\Gothic\Client\Pages\GothicGoodies.razor"
                   image

#line default
#line hidden
#nullable disable
            );
            __builder.AddAttribute(32, "class", "gothicImage");
            __builder.CloseElement();
            __builder.AddMarkupContent(33, "\r\n");
#nullable restore
#line 34 "A:\Proiecte Visual Studio\Gothic\Client\Pages\GothicGoodies.razor"
    }

#line default
#line hidden
#nullable disable
            __builder.CloseElement();
            __builder.AddMarkupContent(34, "\r\n\r\n");
            __builder.AddMarkupContent(35, "<div style=\"display:flex; align-items:center; justify-content:center; min-width:100vw;\">\r\n    <button style=\"font-size:2em; margin-top:2vh; margin-bottom:2vh;\"><a style=\"text-decoration: none; color: black;\" href=\"/\">Back</a></button>\r\n</div>\r\n\r\n\r\n\r\n\r\n");
            __builder.AddMarkupContent(36, @"<style>
    body {
        background-color: black;
    }

    #singleImageDisplayer {
        position: fixed;
        z-index: 10;
        display: none;
        align-items: center;
        justify-content: center;
        background-color: rgba(0, 0, 0, 0.7);
        min-width: 100vw;
        min-height: 100vh;
    }

    #largeGothicImage {
        max-width: 95vw;
        max-height: 95vh;
    }

    .align {
        margin: 0;
        background-color: black;
        display: flex;
        flex-direction: column;
        align-content: stretch;
    }

    h1 {
        margin-top: 5vh;
        margin-bottom: 5vh;
        color: rgb(199, 180, 180);
        text-shadow: 1px 1px 8px gray;
        align-self: center;
    }

    .text {
        margin-left: 5vw;
        color: rgb(199, 180, 180);
        text-shadow: 1px 1px 8px gray;
        font-size: 2em;
    }

    .imageDisplayer {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: space-around;
    }

    .gothicImage {
        min-height: 20vh;
        max-height: 20vh;
        margin-left: 2vw;
        margin-right: 2vw;
        margin-bottom: 2vh;
    }
</style>");
        }
        #pragma warning restore 1998
#nullable restore
#line 43 "A:\Proiecte Visual Studio\Gothic\Client\Pages\GothicGoodies.razor"
       
    public List<string> Gothic1 { get; set; } = new List<string> {"../Images/characters/Babe_A.jpg","../Images/characters/Babe_B.jpg", "../Images/characters/Babe_C.jpg", "../Images/characters/Babe_D.jpg",
"../Images/characters/Babe_E.jpg","../Images/characters/Babe_F.jpg","../Images/characters/Babe_Latino_A.jpg","../Images/characters/Babe_Latino_B.jpg","../Images/characters/Baron_Babes.jpg",
    "../Images/characters/Beggar.jpg","../Images/characters/Couple.jpg","../Images/characters/Demonmage.jpg","../Images/characters/Firemage.jpg","../Images/characters/Guard.jpg","../Images/characters/Guru.jpg",
    "../Images/characters/Judge.jpg","../Images/characters/Novice.jpg","../Images/characters/Orebaron.jpg","../Images/characters/Orebarons.jpg","../Images/characters/Organisator.jpg","../Images/characters/Shadow_A.jpg",
    "../Images/characters/Shadow_B.jpg","../Images/characters/soldier.jpg","../Images/characters/Templar.jpg","../Images/characters/Watermage.jpg" ,"../Images/graduation/Diego.png" ,"../Images/graduation/Diego2.jpg"
     ,"../Images/graduation/Gorn.jpg" ,"../Images/graduation/Lester2.jpg"  ,"../Images/graduation/Milten.jpg" ,"../Images/graduation/orcWarrior.jpg" ,"../Images/monsters/Demon_A.jpg"
     ,"../Images/monsters/Demon_B.jpg" ,"../Images/monsters/Firegolem.jpg" ,"../Images/monsters/Firewaran.jpg" ,"../Images/monsters/Gobbo.jpg" ,"../Images/monsters/Gobbos.jpg" ,"../Images/monsters/Golem.jpg"
     ,"../Images/monsters/Harpy.jpg" ,"../Images/monsters/Icegolem.jpg" ,"../Images/monsters/Minecrawler.jpg" ,"../Images/monsters/Orc_Shaman.jpg" ,"../Images/monsters/Orc_Undead_Highpriest.jpg"
     ,"../Images/monsters/Scavenger.jpg" ,"../Images/monsters/Shadowbeast.jpg" ,"../Images/monsters/Skeleton_A.jpg" ,"../Images/monsters/Skeleton_B.jpg" ,"../Images/monsters/Skeleton_Flying.jpg"
     ,"../Images/monsters/Sleeper.jpg" ,"../Images/monsters/Snapper.jpg" ,"../Images/monsters/Sumpfhai.jpg" ,"../Images/monsters/Troll_A.jpg" ,"../Images/monsters/Troll_B.jpg" ,"../Images/monsters/Troll_Babe_A.jpg"
     ,"../Images/monsters/Troll_Babe_B.jpg" ,"../Images/monsters/Troll_Babe_C.jpg" ,"../Images/monsters/Troll_Babe_D.jpg" ,"../Images/monsters/Waran.jpg" ,"../Images/monsters/Zombie_A.jpg"
        ,"../Images/monsters/Zombie_B.jpg","../Images/11-6-trainonehanded.jpg", "../Images/Demon_Mage.jpg" ,"../Images/Diego1.jpg" ,"../Images/goodies.png" ,"../Images/goodies2.png"
        ,"../Images/GoofyBunch.jpg" ,"../Images/GothicHomeTitle.jpg" ,"../Images/King.jpg"  ,"../Images/quest1.jpg" ,"../Images/skillLevelUp.jpg" ,"../Images/Skull.jpg" ,"../Images/solvedFailed.png"};

    public List<string> Gothic2 { get; set; } = new List<string> { "../Images/blacksmith.jpg", "../Images/Failed quests.jpg", "../Images/Failed Quests2.jpg", "../Images/failedQuests.png", "../Images/Intro.jpg"
     ,"../Images/Intro.png" ,"../Images/MainQuest.png" ,"../Images/MainQuest2.png" ,"../Images/mineEntrance.jpg" ,"../Images/quest2.jpg" ,"../Images/quest3.jpg" ,"../Images/quest6.jpg" ,"../Images/readingBooks.jpg"
     ,"../Images/solvedQuests.jpg" ,"../Images/spare.jpg" ,"../Images/statScreen.jpg"};

    public List<string> Gothic4 { get; set; } = new List<string> { "../Images/Arcaniaquests.jpg", "../Images/Arcaniaquests2jpg.jpg", "../Images/Arcaniaquests3.jpg", "../Images/Arcaniaquests4.jpg"
    ,"../Images/fightingSkill.jpg" ,"../Images/fightingSkill0.5.jpg" ,"../Images/fightingSkill2.jpg" ,"../Images/forgingSword.jpg" ,"../Images/gothic4monastery.jpg" ,"../Images/forgingSword.jpg"
     ,"../Images/mageSkill.jpg" ,"../Images/mageSkill2.jpg" ,"../Images/proveSkilltoDiego.jpg" ,"../Images/quest5.png" ,"../Images/quest6.png"  ,"../Images/questBottom.png"
     ,"../Images/questSideLarge.png" ,"../Images/skillBottom.png" ,"../Images/skills.jpg" ,"../Images/skillSide.png" ,"../Images/skillSideR.png" ,"../Images/Swampshark.jpg"
     ,"../Images/Tooshoo.jpg"};

#line default
#line hidden
#nullable disable
#nullable restore
#line 129 "A:\Proiecte Visual Studio\Gothic\Client\Pages\GothicGoodies.razor"
      
    protected override void OnInitialized()
    {
        JsRuntime.InvokeVoidAsync("onclick");
    }

#line default
#line hidden
#nullable disable
        [global::Microsoft.AspNetCore.Components.InjectAttribute] private IJSRuntime JsRuntime { get; set; }
    }
}
#pragma warning restore 1591
