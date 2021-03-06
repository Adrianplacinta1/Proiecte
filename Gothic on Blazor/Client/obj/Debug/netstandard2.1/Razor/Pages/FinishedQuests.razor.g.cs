#pragma checksum "A:\Proiecte Visual Studio\Gothic\Client\Pages\FinishedQuests.razor" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "e44266bd700635f8e1a1f701cb34a87d215640a1"
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
    [Microsoft.AspNetCore.Components.RouteAttribute("/FinishedQuests")]
    public partial class FinishedQuests : Microsoft.AspNetCore.Components.ComponentBase
    {
        #pragma warning disable 1998
        protected override void BuildRenderTree(Microsoft.AspNetCore.Components.Rendering.RenderTreeBuilder __builder)
        {
            __builder.AddMarkupContent(0, "<head>\r\n    <meta charset=\"UTF-8\">\r\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\r\n\r\n\r\n\r\n    <title>Finished Quests</title>\r\n</head>\r\n\r\n");
            __builder.OpenComponent<Gothic.Client.Components.GothicTitle>(1);
            __builder.AddAttribute(2, "BackgroundImage", "../Images/GothicHomeTitle2.jpg");
            __builder.CloseComponent();
            __builder.AddMarkupContent(3, "\r\n\r\n");
            __builder.OpenElement(4, "body");
            __builder.AddMarkupContent(5, "\r\n    ");
            __builder.AddMarkupContent(6, "<div class=\"align\">\r\n        <h1> <u>Finished Quests</u></h1>\r\n    </div>\r\n    ");
            __builder.AddMarkupContent(7, @"<div style=""display:flex; align-items:center; justify-content:center; min-width:100vw;"">
        <button style=""font-size:2em; margin-top:2vh; margin-bottom:2vh;""><a style=""text-decoration: none; color: black;"" href=""/"">Back</a></button>
    </div>
    ");
            __builder.OpenComponent<Gothic.Client.Components.ImageText>(8);
            __builder.AddAttribute(9, "ImageSource", "../Images/solvedFailed.png");
            __builder.AddAttribute(10, "ImgHeight", "700px");
            __builder.AddAttribute(11, "ChildContent", (Microsoft.AspNetCore.Components.RenderFragment)((__builder2) => {
                __builder2.AddMarkupContent(12, "\r\n\r\n        ");
                __builder2.OpenElement(13, "button");
                __builder2.AddAttribute(14, "onclick", Microsoft.AspNetCore.Components.EventCallback.Factory.Create<Microsoft.AspNetCore.Components.Web.MouseEventArgs>(this, 
#nullable restore
#line 25 "A:\Proiecte Visual Studio\Gothic\Client\Pages\FinishedQuests.razor"
                          SetSolved

#line default
#line hidden
#nullable disable
                ));
                __builder2.AddAttribute(15, "class", "solvedFailedButtons");
                __builder2.AddContent(16, "SOLVED");
                __builder2.CloseElement();
                __builder2.AddMarkupContent(17, "\r\n        ");
                __builder2.OpenElement(18, "button");
                __builder2.AddAttribute(19, "onclick", Microsoft.AspNetCore.Components.EventCallback.Factory.Create<Microsoft.AspNetCore.Components.Web.MouseEventArgs>(this, 
#nullable restore
#line 26 "A:\Proiecte Visual Studio\Gothic\Client\Pages\FinishedQuests.razor"
                          SetFailed

#line default
#line hidden
#nullable disable
                ));
                __builder2.AddAttribute(20, "class", "solvedFailedButtons");
                __builder2.AddContent(21, "FAILED");
                __builder2.CloseElement();
                __builder2.AddMarkupContent(22, "\r\n\r\n    ");
            }
            ));
            __builder.CloseComponent();
            __builder.AddMarkupContent(23, "\r\n\r\n\r\n    ");
            __builder.OpenComponent<Gothic.Client.Components.SolvedFailed>(24);
            __builder.AddAttribute(25, "SolvedDisplay", Microsoft.AspNetCore.Components.CompilerServices.RuntimeHelpers.TypeCheck<System.String>(
#nullable restore
#line 31 "A:\Proiecte Visual Studio\Gothic\Client\Pages\FinishedQuests.razor"
                                  Solved

#line default
#line hidden
#nullable disable
            ));
            __builder.AddAttribute(26, "FailedDisplay", Microsoft.AspNetCore.Components.CompilerServices.RuntimeHelpers.TypeCheck<System.String>(
#nullable restore
#line 31 "A:\Proiecte Visual Studio\Gothic\Client\Pages\FinishedQuests.razor"
                                                          Failed

#line default
#line hidden
#nullable disable
            ));
            __builder.CloseComponent();
            __builder.AddMarkupContent(27, "\r\n");
            __builder.CloseElement();
            __builder.AddMarkupContent(28, "\r\n\r\n\r\n");
            __builder.AddMarkupContent(29, @"<style>
    body {
        background-color: black;
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

    .solvedFailedButtons {
        width: 10vw;
        margin-left: 2vw;
        margin-right: 2vw;
    }
</style>");
        }
        #pragma warning restore 1998
#nullable restore
#line 63 "A:\Proiecte Visual Studio\Gothic\Client\Pages\FinishedQuests.razor"
      

    [Parameter]
    public string Solved { get; set; } = "flex";
    [Parameter]
    public string Failed { get; set; } = "none";

    public void SetSolved()
    {
        Solved = "flex";
        Failed = "none";
    }

    public void SetFailed()
    {
        Solved = "none";
        Failed = "flex";
    }


#line default
#line hidden
#nullable disable
        [global::Microsoft.AspNetCore.Components.InjectAttribute] private IJSRuntime JsRuntime { get; set; }
    }
}
#pragma warning restore 1591
