if(document.getElementById("input-check-mon").checked) {
    document.getElementById("input-check-hidden-mon").disabled = true;
}

if(document.getElementById("input-check-tues").checked) {
    document.getElementById("input-check-hidden-tues").disabled = true;
}

if(document.getElementById("input-check-wed").checked) {
    document.getElementById("input-check-hidden-wed").disabled = true;
}

if(document.getElementById("input-check-thur").checked) {
    document.getElementById("input-check-hidden-thur").disabled = true;
}

if(document.getElementById("input-check-fri").checked) {
    document.getElementById("input-check-hidden-fri").disabled = true;
}

if(document.getElementById("input-check-sat").checked) {
    document.getElementById("input-check-hidden-sat").disabled = true;
}

if(document.getElementById("input-check-sun").checked) {
    document.getElementById("input-check-hidden-sun").disabled = true;
}



if(document.getElementById("food-type-check-korean").checked) {
    document.getElementById("food-type-check-korean").disabled = true;
}


if(document.getElementById("food-type-check-chinese").checked) {
    document.getElementById("food-type-check-chinese").disabled = true;
}

if(document.getElementById("food-type-check-western").checked) {
    document.getElementById("food-type-check-western").disabled = true;
}

if(document.getElementById("food-type-check-japanese").checked) {
    document.getElementById("food-type-check-japanese").disabled = true;
}

if(document.getElementById("food-type-check-cafe").checked) {
    document.getElementById("food-type-check-cafe").disabled = true;
}

if(document.getElementById("food-type-check-alcohol").checked) {
    document.getElementById("food-type-check-alcohol").disabled = true;
}


//이미지 파일 첨부 미리보기
function setRfile(event) {
    var reader = new FileReader();

    reader.onload = function(event) {
      var img = document.createElement("img");
      img.setAttribute("src", event.target.result);
      document.querySelector("div#image-preview").appendChild(img);
    };

    reader.readAsDataURL(event.target.files[0]);
  }