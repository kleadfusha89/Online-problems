<%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Main.aspx.cs" Inherits="CamelCase.Main" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>


        </div>
        
        <p>
            <asp:RequiredFieldValidator ID="reqtxtEnterSomething" runat="server" ErrorMessage="Please Enter Something" Visible="false" ControlToValidate="txtEnterSomething" OnDataBinding="btnCamelCase_Click"></asp:RequiredFieldValidator>
            <asp:TextBox ID="txtEnterSomething" runat="server" Height="300px" Width="300px" BackColor="#E5E5E5" BorderColor="#37B3C8" BorderStyle="Inset" BorderWidth="3px" Columns="40" TextMode="MultiLine"></asp:TextBox><br />
            <asp:Button ID="btnCamelCase" runat="server" Text="CamelCase" OnClick="btnCamelCase_Click" Width="308.4px" BackColor="#E5E5E5" BorderColor="#37B3C8" BorderStyle="Inset" BorderWidth="3px" /><br />
            <asp:Button ID="btnGoogleCase" runat="server" Text="gOOGLEcASE" OnClick="btnGoogleCase_Click" Width="308.4px" BackColor="#E5E5E5" BorderColor="#37B3C8" BorderStyle="Inset" BorderWidth="3px" />
            
            <br /><br />
            <asp:TextBox ID="txtShow" ReadOnly="true" runat="server" Visible="false" Height="300px" Width="300px" BackColor="#E5E5E5" BorderColor="#37B3C8" BorderStyle="Inset" BorderWidth="3px" TextMode="MultiLine" ></asp:TextBox>
            
           
            <asp:Button ID="btnClearCamelgOOGLE" runat="server" Text="cLEAR" OnClick="btnClear_Click" Width="308.4px" BackColor="#E5E5E5" BorderColor="#37B3C8" BorderStyle="Inset" BorderWidth="3px" />
        </p>
    </form>
</body>
</html>
