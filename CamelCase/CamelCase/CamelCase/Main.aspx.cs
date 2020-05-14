using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

namespace CamelCase
{
    public partial class Main : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            

        }

        protected void btnCamelCase_Click(object sender, EventArgs e)
        {
            string txtInput = txtEnterSomething.Text;
            string CamelCase = "";

            
            if (txtInput.Length > 0 && txtInput[0] != ' ')
               CamelCase += Char.ToUpper(txtInput[0]);
            
            for (int i = 1; i < txtInput.Length; i++)
            {                               

                if (txtInput[i] != ' ' && txtInput[i - 1] == ' ')
                    CamelCase += Char.ToUpper(txtInput[i]);

                else if (txtInput[i] != ' ' && txtInput[i - 1] != ' ')
                    CamelCase += Char.ToLower(txtInput[i]);
            }
            txtShow.Visible = true;
            txtShow.Text = CamelCase;


        }

        protected void btnGoogleCase_Click(object sender, EventArgs e)
        {

            string txtInput = txtEnterSomething.Text;
            string googleCase = "";

            if (txtInput.Length > 0 && txtInput[0] != ' ')
                googleCase += Char.ToUpper(txtInput[0]);
            for (int i = 1; i < txtInput.Length; i++)
            {

                if (txtInput[i] != ' ' && txtInput[i - 1] == ' ')
                    googleCase += Char.ToLower(txtInput[i]);

                else if (txtInput[i] != ' ' && txtInput[i - 1] != ' ')
                    googleCase += Char.ToUpper(txtInput[i]);
            }
            txtShow.Visible = true;
            txtShow.Text = googleCase;
        }

       

    

        protected void btnClear_Click(object sender, EventArgs e)
        {
            txtEnterSomething.Text = "";
            txtShow.Text = "";
            txtShow.Visible = false;
        }
    }
}