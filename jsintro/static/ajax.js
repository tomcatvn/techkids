/**
 * Created by Administrator on 30/12/2016.
 */
// alert('thanh dan choi')
function loadData() {
    console.log(">> LoadData");
    console.log("Loading data");
    $.ajax({
        url : "/api/hrc",
        type : "get",
        dataType: "json",
        contentType :"json",
        success : function (data) {
            console.log("OK");


        }
    })
}
