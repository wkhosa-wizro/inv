
var Vat = "9454/069/17/1";
var Tel = "071 015 8651";
var Fax = "086 759 2795";
var Email = "sales@malcam.co.za";
var CompanyReg = "2012/017435/07";
var Street = "3107 Ratama Cr";
var Line1Addr = "Brooklands Lifestyle Estates 3";
var Line2Addr = "Kosmosdal";
var ZipCode = "157";

var Subtotal = 194;
var Tax = 0;
var Total = 194;
var Balance = 194;

window.onload = function() {

    document.getElementById("sub-var").innerHTML =  "Subtotal      R ";
    document.getElementById("tax-var").innerHTML =  "Tax (15%)       ";
    document.getElementById("total-var").innerHTML =  "Total         ";
    document.getElementById("balance-var").innerHTML =  "Balance Due ";

    document.getElementById("sub-val").innerHTML =  Subtotal;
    document.getElementById("tax-val").innerHTML =  Tax;
    document.getElementById("total-val").innerHTML =  Total;
    document.getElementById("balance-val").innerHTML =  Balance;

}
