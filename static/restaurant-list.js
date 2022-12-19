
function toggleFavoritesImage(event) {
  event.stopPropagation();
  const objectPosition = event.target.style.objectPosition;
  if (objectPosition === "0px 0px")
    event.target.style.objectPosition = "0 -30px";
  else
    event.target.style.objectPosition = "0 0";
}

