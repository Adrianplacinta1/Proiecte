#pragma checksum "A:\Proiecte Visual Studio\Gothic\Client\Components\Card.razor" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "4fca48da10dc745614331d1e84770c0c2e639ec4"
// <auto-generated/>
#pragma warning disable 1591
namespace Gothic.Client.Components
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
    public partial class Card : Microsoft.AspNetCore.Components.ComponentBase
    {
        #pragma warning disable 1998
        protected override void BuildRenderTree(Microsoft.AspNetCore.Components.Rendering.RenderTreeBuilder __builder)
        {
            __builder.AddMarkupContent(0, "<div class=\"cardTitle text \">\r\n    <h3><u>Quest Name</u></h3>\r\n    <div class=\"container\">\r\n        <h4><b>Description:</b> Something to do</h4>\r\n        <p>⤷Bonus: Some other thing to do</p>\r\n    </div>\r\n</div>\r\n\r\n");
            __builder.AddMarkupContent(1, @"<style>
    .text {
        color: rgb(199, 180, 180);
        text-shadow: 1px 1px 8px gray;
    }

    .cardTitle {
        box-shadow: 0 4px 8px 0 gray;
        transition: 0.3s;
        border-radius: 5px; /* 5px rounded corners */
        background-color: rgb(34, 2, 2);
        min-width: 90%;
        align-self: center;
        margin-bottom: 2vh;
        text-indent: 2vw;
    }

        .cardTitle:hover {
            box-shadow: 0 8px 16px 0 gray;
        }
</style>");
        }
        #pragma warning restore 1998
    }
}
#pragma warning restore 1591
