/**
 * Created by Administrator on 26/12/2016.
 */

var bachduong = ["Bạch Dương","năng động, sáng tạo, tiên phong, quyết đoán, mạnh mẽ, nhà lãnh đạo đầy tham vọng, hướng ngoại, cạnh tranh, nhiệt tình, tự lực, tự tin. Tuy nhiên hay nhanh nhẩu đoảng."];
    kimnguu = ["Kim Ngưu","cứng đầu, thận trọng, điềm tĩnh, kiên trì, lâu dài, hướng nội, bảo thủ, ổn định, siêng năng, đáng tin cậy, quan trọng vật chất, và thường có khả năng tài chính đáng kể."];
    songtu= ["Song Tử","thay đổi linh hoạt, nhạy bén, đa năng, sống động, tỉnh táo, khả năng giao tiếp, hòa đồng, khéo léo, nhanh nhẹn, trí tuệ, và tinh thần đầy tham vọng. Thích hợp với mọi ngành nghề"];
    cugiai = ["Cự Giải","sống nội tâm, nhạy cảm, u sầu, cảm thông, thận trọng, biết giữ bí mật, ỷ lại, bình tĩnh, trí tưởng tượng phong phú, tận tâm, và khá truyền thống."];
    sutu = ["Sư Tử","đầy tham vọng, một người yêu ánh đèn sân khấu,thích đầu cơ, hướng ngoại, lạc quan, đáng kính, trang nghiêm, tự tin, cởi mở, rực rỡ, lôi cuốn, kịch tính, cạnh tranh, có bản năng là một nhà lãnh đạo."];
    xunu = ["Xử Nữ","thực tế, có trách nhiệm, hay phân tích, phân biệt đối xử, lập kế hoạch cẩn thận, chính xác và đúng giờ, tận tụy, chủ nghĩa hoàn hảo, hay chỉ trích, có ý thức giữ gìn sức khỏe, và hơi hướng nội."];
    thienbinh = ["Thiên Bình","một sứ giả hòa bình,có tài ngoại giao, duyên dáng, tao nhã, lịch sự, đầu óc công bằng, hòa đồng, yêu nghệ thuật sáng tạo, thân thiện, hướng ngoại, và thường hơi thiếu quyết đoán."];
    thannong = ["Thần Nông","sâu sắc, mạnh mẽ, táo bạo, can đảm, bền vững, cạnh tranh, nhà nghiên cứu xuất sắc, tháo vát, thám tử tài ba, bí ẩn, sắc sảo, tự lực cánh sinh, trầm lặng, hướng nội."];
    nhanma = ["Nhân Mã","lạc quan, yêu tự do, giản dị, thân thiện, sôi động, thích giao du, nhiệt tình, hiếu học, nhìn xa trông rộng, thẳng thắn, trung thực, trung thành, hiếu động và thích du lịch."];
    maket = ["Ma Kết","đầy tham vọng, ý thức tổ chức tốt, kỷ luật, cứng nhắc, tiết kiệm, thận trọng, bảo thủ, có trách nhiệm, thiết thực, kiên trì, luôn xác định mục tiêu rõ ràng, có khả năng lên và sắp xếp kế hoạch tốt, thích hợp chính trị."];
    baobinh1 = ["Bảo Bình","chủ nghĩa cá nhân, không theo quy chuẩn, tư tưởng tiến bộ, độc đáo, độc lập, nhân đạo, vị tha, nhìn xa trông rộng, sâu sắc, trí tuệ, khéo léo, sáng tạo, không thể đoán trước, lúc thân thiện lúc hơi lánh đời."];
    songngu = ["Song Ngư","hay có những cảm giác khác thường, ấn tượng, yêu hoà bình, nghiêm trọng hóa vấn đề, thông cảm, từ bi, yêu nghệ thuật, thích sáng tạo mơ mộng, trí tưởng tượng phong phú, tận tụy, nhút nhát, sống nội tâm, quan trọng tinh thần, không quan trọng vật chất."];

function cunghoangdao(ngay,thang){
    document.getElementById('tinhcachb').innerHTML= "Phẩm chất & Tính cách";
    ngay= Number(ngay);
    thang = Number(thang);
    cung = document.getElementById('cung').innerHTML;
    tinhcach = document.getElementById('tinhcachp').innerHTML;


    if ((thang==3 && ngay >= 21) || (thang==4 && ngay<=19)) {

       return document.getElementById('cung').innerHTML = bachduong[0],document.getElementById('tinhcachp').innerHTML = bachduong[1];
    };
    if ((thang == 4 && ngay >= 20) || (thang==5 && ngay <=20)){
       return document.getElementById('cung').innerHTML = kimnguu[0],document.getElementById('tinhcachp').innerHTML = kimnguu[1];
};
    if ((thang == 5 && ngay >= 21) || (thang==6 && ngay <=21)){
        return document.getElementById('cung').innerHTML = songtu[0],document.getElementById('tinhcachp').innerHTML = songtu[1];
};
    if ((thang == 6 && ngay >= 22) || (thang==7 && ngay <=22)){
        return document.getElementById('cung').innerHTML = cugiai[0],document.getElementById('tinhcachp').innerHTML = cugiai[1];
};
    if ((thang == 7 && ngay >= 23) || (thang==8 && ngay <=22)){
        return document.getElementById('cung').innerHTML = sutu[0],document.getElementById('tinhcachp').innerHTML = sutu[1];
};
    if ((thang == 8 && ngay >= 23) || (thang==9 && ngay <=22)){
        return document.getElementById('cung').innerHTML = xunu[0],document.getElementById('tinhcachp').innerHTML = xunu[1];
};
    if ((thang == 9 && ngay >= 23) || (thang==10 && ngay <=23)){
        return document.getElementById('cung').innerHTML = thienbinh[0],document.getElementById('tinhcachp').innerHTML = thienbinh[1];
};
    if ((thang == 10 && ngay >= 24) || (thang==11 && ngay <=21)){
        return document.getElementById('cung').innerHTML = thannong[0],document.getElementById('tinhcachp').innerHTML = thannong[1];
};
    if ((thang == 11 && ngay >= 22) || (thang==12 && ngay <=21)){
       return document.getElementById('cung').innerHTML = nhanma[0],document.getElementById('tinhcachp').innerHTML = nhanma[1];
};
    if ((thang == 12 && ngay >= 22) || (thang==1 && ngay <=19)){
        return document.getElementById('cung').innerHTML = maket[0],document.getElementById('tinhcachp').innerHTML = maket[1];
};
    if ((thang == 1 && ngay >= 20) || (thang=2 && ngay <=18)){
        return document.getElementById('cung').innerHTML = baobinh1[0],document.getElementById('tinhcachp').innerHTML = baobinh1[1];
};
    if ((thang == 2 && ngay >= 19) || (thang==3 && ngay <=20)) {
       return document.getElementById('cung').innerHTML = songngu[0],document.getElementById('tinhcachp').innerHTML = songngu[1];
    }}

