

function tinhbmi(){
    chieucao= parseInt(document.getElementById("height").value)/100;
    cannang= parseInt(document.getElementById("weight").value);
    bmi = cannang / (chieucao*chieucao).toFixed(2);
    return document.getElementById("bmi").value = bmi;


}