#pragma checksum "A:\Proiecte Visual Studio\Gothic\Client\Pages\StatXP.razor" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "66797f563be9544a5abeeac077028c233383539c"
// <auto-generated/>
#pragma warning disable 1591
#pragma warning disable 0414
#pragma warning disable 0649
#pragma warning disable 0169

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
    [Microsoft.AspNetCore.Components.RouteAttribute("/StatXPCounter")]
    public partial class StatXP : Microsoft.AspNetCore.Components.ComponentBase
    {
        #pragma warning disable 1998
        protected override void BuildRenderTree(Microsoft.AspNetCore.Components.Rendering.RenderTreeBuilder __builder)
        {
        }
        #pragma warning restore 1998
#nullable restore
#line 139 "A:\Proiecte Visual Studio\Gothic\Client\Pages\StatXP.razor"
      
    public List<string> StrValues { get; set; } = new List<string> { "15 (4.VI.2020)", "19 (12.VII.2020)", "23 (6.VIII.2020)" };

    public List<string> CașValues { get; set; } = new List<string> { "1000 (4.VI.2020)", "3500 (22.VI.2020)", "6000 (17.VII.2020)", "5800 (5.VIII.2020)" };

    public List<string> DisplayValues { get; set; } = new List<string> { "none", "none", "none", "none" };

    public string DiscValues { get; set; } = "0 + 250 =250 + 175 = 425";

    public string ValhollValues { get; set; } = "0 + 250 =250 + 200 = 450";

    public string AddedValue { get; set; } = "";





    public void ShowSTRBox()
    {
        DisplayValues[0] = "flex";
    }

    public void HideSTRBox()
    {
        StrValues.Add(AddedValue);
        AddedValue = "";
        DisplayValues[0] = "none";
    }

    public void ShowDiscBox()
    {
        DisplayValues[1] = "flex";
    }

    public void HideDiscBox()
    {
        var total = DiscValues.Split("=");
        int Total = int.Parse(total[total.Length - 1]);
        int added = int.Parse(AddedValue.Split("(")[0]);
        Total += added;
        DiscValues += " + " + AddedValue +" = " + Total.ToString();
        AddedValue = "";
        DisplayValues[1] = "none";
    }

    public void ShowValhollBox()
    {
        DisplayValues[2] = "flex";
    }

    public void HideValhollBox()
    {
        var total = ValhollValues.Split("=");
        int Total = int.Parse(total[total.Length - 1]);
        int added = int.Parse(AddedValue.Split("(")[0]);
        Total += added;
        ValhollValues += " + " + AddedValue + " = " + Total.ToString();
        AddedValue = "";
        DisplayValues[2] = "none";
    }



    public void ShowCașBox()
    {
        DisplayValues[3] = "flex";
    }

    public void HideCașBox()
    {
        CașValues.Add(AddedValue);
        AddedValue = "";
        DisplayValues[3] = "none";
    }

#line default
#line hidden
#nullable disable
    }
}
#pragma warning restore 1591