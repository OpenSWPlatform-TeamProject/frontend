
function toggleFavoritesImage1(event) {
  event.stopPropagation();
  const objectPosition = event.target.style.objectPosition;
  console.log('처음이다 이놈아');
  if (objectPosition === "0px 0px")
    event.target.style.objectPosition = "0 -30px";
  else
    event.target.style.objectPosition = "0 0";
}

function toggleFavoritesImage2(event) {
  event.stopPropagation();
  const objectPosition = event.target.style.objectPosition;
  console.log('메롱메롱');
  if (objectPosition === "0px 0px")
    event.target.style.objectPosition = "0 -30px";
  else
    event.target.style.objectPosition = "0 0";
}

