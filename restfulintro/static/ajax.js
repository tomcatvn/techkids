function loadData(){
    var bigDiv = document.getElementById('bigdiv');
    $.ajax({
        type:"get",
        url:"/api/hrc",
        dataType :"json",
        contentType: "json",
        success : function(data) {
            console.log(data);
            // for (x in data){
            //     var item = data[x];
            //     var ul = document.createElement('UL');
            //     bigDiv.appendChild(ul);
            //     var li1 = document.createElement('LI');
            //     var li1text = document.createTextNode(item.id);
            //     li1.appendChild(li1text);
            //     ul.appendChild(li1);
            //     var li2 = document.createElement(document.createTextNode(item.name));
            //     ul.appendChild(li2);
            //     var li3 = document.createElement(document.createTextNode(item.desc));
            //     ul.appendChild(li3);
            //     var li4 = document.createElement(document.createTextNode(item.img));
            //     ul.appendChild(li4);


            }})}



function addData(){
    var zodiacName = document.getElementById('zodiac-name').value;
    var zodiacIMG = document.getElementById('zodiac-img').value;
    var zodiacDESC = document.getElementById('zodiac-desc').value;
    var data = {
        name : zodiacName,
        desc : zodiacDESC,
        img : zodiacIMG
    };
    console.log(zodiacName, zodiacIMG,zodiacDESC);
    $.ajax({
        type:'post',
        dataType: 'json',
        contentType: 'application/json',
        url:'/api/hrc',
        data: JSON.stringify(data),
        success : function(response){
            console.log(response)
        },
        error: function (data) {
            alert('error')
        }

    })


}
function updateData(){
    var name = document.getElementById('update-name').value;
    var desc = document.getElementById('update-desc').value;
    var img = document.getElementById('update-img').value;
    var data= {
        name :  name,
        desc : desc,
        img : img
    };
    console.log(name,desc,img);

    $.ajax({
        type:'put',
        url:'/api/hrc/'+document.getElementById('update-id').value,
        contentType : 'application/json',
        data : JSON.stringify(data),
        success : function(update){
            console.log('updated')
        }
    })
}
function deleteData(){
    $.ajax({
        type:'delete',
        url:'/api/hrc/'+document.getElementById('delete-id').value,
        success: function(data){
            console.log('deleted')
        }
    })
}