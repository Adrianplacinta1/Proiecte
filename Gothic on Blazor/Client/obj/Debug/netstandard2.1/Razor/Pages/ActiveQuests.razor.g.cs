#pragma checksum "A:\Proiecte Visual Studio\Gothic\Client\Pages\ActiveQuests.razor" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "2ff189759dbf4eb26efc6b0602ac4e9d0e78cb07"
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
    [Microsoft.AspNetCore.Components.RouteAttribute("/ActiveQuests")]
    public partial class ActiveQuests : Microsoft.AspNetCore.Components.ComponentBase
    {
        #pragma warning disable 1998
        protected override void BuildRenderTree(Microsoft.AspNetCore.Components.Rendering.RenderTreeBuilder __builder)
        {
            __builder.OpenComponent<Gothic.Client.Components.GothicTitle>(0);
            __builder.AddAttribute(1, "BackgroundImage", "../Images/GothicHomeTitle2.jpg");
            __builder.CloseComponent();
            __builder.AddMarkupContent(2, "\r\n");
            __builder.OpenElement(3, "body");
            __builder.AddMarkupContent(4, "\r\n    ");
            __builder.AddMarkupContent(5, "<div class=\"align\">\r\n        <h1> <u>Active Quests</u></h1>\r\n    </div>\r\n    ");
            __builder.OpenElement(6, "div");
            __builder.AddAttribute(7, "style", "display:flex; flex-direction:row; justify-content:space-between;");
            __builder.AddMarkupContent(8, "\r\n        <img src=\"../Images/questSide2.png\" class=\"sideImage\">\r\n        ");
            __builder.OpenComponent<Gothic.Client.Components.QuestCardDiv>(9);
            __builder.CloseComponent();
            __builder.AddMarkupContent(10, "\r\n        <img src=\"../Images/questSide2r.png\" class=\"sideImage\">\r\n    ");
            __builder.CloseElement();
            __builder.AddMarkupContent(11, "\r\n\r\n\r\n    ");
            __builder.OpenComponent<Gothic.Client.Components.ImageText>(12);
            __builder.AddAttribute(13, "ImageSource", "../Images/questBottom.png");
            __builder.AddAttribute(14, "ImgHeight", "260px");
            __builder.AddAttribute(15, "ChildContent", (Microsoft.AspNetCore.Components.RenderFragment)((__builder2) => {
                __builder2.AddMarkupContent(16, "\r\n\r\n        ");
                __builder2.OpenElement(17, "div");
                __builder2.AddAttribute(18, "style", "display:flex; flex-direction:column; transform:translate(-3vw)");
                __builder2.AddMarkupContent(19, "\r\n            ");
                __builder2.OpenComponent<Gothic.Client.Components.Butoane>(20);
                __builder2.AddAttribute(21, "Text", "NEW QUEST");
                __builder2.CloseComponent();
                __builder2.AddMarkupContent(22, "\r\n            ");
                __builder2.OpenComponent<Gothic.Client.Components.Butoane>(23);
                __builder2.AddAttribute(24, "Text", "Home Page");
                __builder2.AddAttribute(25, "Href", "/");
                __builder2.CloseComponent();
                __builder2.AddMarkupContent(26, "\r\n        ");
                __builder2.CloseElement();
                __builder2.AddMarkupContent(27, "\r\n\r\n    ");
            }
            ));
            __builder.CloseComponent();
            __builder.AddMarkupContent(28, " \r\n\r\n");
            __builder.CloseElement();
            __builder.AddMarkupContent(29, "\r\n\r\n\r\n");
            __builder.AddMarkupContent(30, @"<style>
    body{
        background-color:black;
    }
    .align {
        margin: 0;
        background-color: black;
        display: flex;
        flex-direction: column;
        align-content: stretch;
    }

    h1 {
        color: rgb(199, 180, 180);
        text-shadow: 1px 1px 8px gray;
        align-self: center;
    }

    .sideImage{
        width:200px;
        margin-left:2vw;
        margin-right:2vw;
    }
</style>");
        }
        #pragma warning restore 1998
    }
}
#pragma warning restore 1591
