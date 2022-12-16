function handleCardClick() {
  console.log("화면 이동 했어요!");
}

function toggleFavoritesImage(event) {
  event.stopPropagation();
  const objectPosition = event.target.style.objectPosition;
  if (objectPosition === "0px 0px")
    event.target.style.objectPosition = "0 -30px";
  else
    event.target.style.objectPosition = "0 0";
}




/*
  const objectPosition12 = document.getElementsByClassName("favorites")[i].style.objectPosition;
  if(objectPosition === "0px 0px")
    document.getElementsByClassName("favorites")[i].style.objectPosition = "0 -30px";
  else
    document.getElementsByClassName("favorites")[i].style.objectPosition = "0 0";
*/