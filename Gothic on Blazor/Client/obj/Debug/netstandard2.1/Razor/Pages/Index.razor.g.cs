#pragma checksum "A:\Proiecte Visual Studio\Gothic\Client\Pages\Index.razor" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "a5ba0574ff9ec1bc38f96d3c69c6c8e0b1a06080"
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
    [Microsoft.AspNetCore.Components.RouteAttribute("/")]
    public partial class Index : Microsoft.AspNetCore.Components.ComponentBase
    {
        #pragma warning disable 1998
        protected override void BuildRenderTree(Microsoft.AspNetCore.Components.Rendering.RenderTreeBuilder __builder)
        {
            __builder.OpenComponent<Gothic.Client.Components.GothicTitle>(0);
            __builder.AddAttribute(1, "BackgroundImage", "../Images/GothicHomeTitle2.jpg");
            __builder.CloseComponent();
            __builder.AddMarkupContent(2, "\r\n\r\n");
            __builder.OpenComponent<Gothic.Client.Components.StatBox>(3);
            __builder.AddAttribute(4, "MaxWidth", "33.33vw");
            __builder.AddAttribute(5, "ChildContent", (Microsoft.AspNetCore.Components.RenderFragment)((__builder2) => {
                __builder2.AddMarkupContent(6, "\r\n    <img src=\"../Images/statScreen.jpg\" class=\"statImage\">\r\n");
            }
            ));
            __builder.CloseComponent();
            __builder.AddMarkupContent(7, "\r\n");
            __builder.OpenComponent<Gothic.Client.Components.Row>(8);
            __builder.AddAttribute(9, "BackgroundImage", "../Images/spare.jpg");
            __builder.AddAttribute(10, "ChildContent", (Microsoft.AspNetCore.Components.RenderFragment)((__builder2) => {
                __builder2.AddMarkupContent(11, "\r\n    ");
                __builder2.OpenComponent<Gothic.Client.Components.Butoane>(12);
                __builder2.AddAttribute(13, "Href", "IntroMain");
                __builder2.AddAttribute(14, "Text", "Intro & Main Quest");
                __builder2.CloseComponent();
                __builder2.AddMarkupContent(15, "\r\n    ");
                __builder2.OpenComponent<Gothic.Client.Components.Butoane>(16);
                __builder2.AddAttribute(17, "Href", "ActiveQuests");
                __builder2.AddAttribute(18, "Text", "Active Quests");
                __builder2.CloseComponent();
                __builder2.AddMarkupContent(19, "\r\n    ");
                __builder2.OpenComponent<Gothic.Client.Components.Butoane>(20);
                __builder2.AddAttribute(21, "Href", "FinishedQuests");
                __builder2.AddAttribute(22, "Text", "Finished Quests");
                __builder2.CloseComponent();
                __builder2.AddMarkupContent(23, "\r\n");
            }
            ));
            __builder.CloseComponent();
            __builder.AddMarkupContent(24, "\r\n");
            __builder.OpenComponent<Gothic.Client.Components.Row>(25);
            __builder.AddAttribute(26, "BackgroundImage", "../Images/mineEntrance.jpg");
            __builder.AddAttribute(27, "ChildContent", (Microsoft.AspNetCore.Components.RenderFragment)((__builder2) => {
                __builder2.AddMarkupContent(28, "\r\n    ");
                __builder2.OpenComponent<Gothic.Client.Components.Butoane>(29);
                __builder2.AddAttribute(30, "Href", "/GothicSkills");
                __builder2.AddAttribute(31, "Text", "Gothic Skills");
                __builder2.CloseComponent();
                __builder2.AddMarkupContent(32, "\r\n    ");
                __builder2.OpenComponent<Gothic.Client.Components.Butoane>(33);
                __builder2.AddAttribute(34, "Href", "/StatXPCounter");
                __builder2.AddAttribute(35, "Text", "Stat XP Counter");
                __builder2.CloseComponent();
                __builder2.AddMarkupContent(36, "\r\n    ");
                __builder2.OpenComponent<Gothic.Client.Components.Butoane>(37);
                __builder2.AddAttribute(38, "Href", "/Rewards&Graduation");
                __builder2.AddAttribute(39, "Text", "Rewards & Graduation ");
                __builder2.CloseComponent();
                __builder2.AddMarkupContent(40, "\r\n");
            }
            ));
            __builder.CloseComponent();
            __builder.AddMarkupContent(41, "\r\n");
            __builder.OpenComponent<Gothic.Client.Components.Row>(42);
            __builder.AddAttribute(43, "BackgroundImage", "../Images/goodies.png");
            __builder.AddAttribute(44, "ChildContent", (Microsoft.AspNetCore.Components.RenderFragment)((__builder2) => {
                __builder2.AddMarkupContent(45, "\r\n    ");
                __builder2.OpenComponent<Gothic.Client.Components.Butoane>(46);
                __builder2.AddAttribute(47, "Href", "/GothicGoodies");
                __builder2.AddAttribute(48, "Text", "Gothic Goodies");
                __builder2.CloseComponent();
                __builder2.AddMarkupContent(49, "\r\n");
            }
            ));
            __builder.CloseComponent();
        }
        #pragma warning restore 1998
    }
}
#pragma warning restore 1591
