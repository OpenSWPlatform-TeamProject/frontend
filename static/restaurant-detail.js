function toggleFavoritesImage() {
  const objectPosition = document.getElementsByClassName("favorites")[0].style.objectPosition;
  if(objectPosition === "0px 0px")
    document.getElementsByClassName("favorites")[0].style.objectPosition = "0 -30px";
  else
    document.getElementsByClassName("favorites")[0].style.objectPosition = "0 0";
}

function toggleLikesImage() {
  const objectPosition = document.getElementsByClassName("likes")[0].style.objectPosition;
  if(objectPosition === "0px -60px")
    document.getElementsByClassName("likes")[0].style.objectPosition = "0 -90px";
  else
    document.getElementsByClassName("likes")[0].style.objectPosition = "0px -60px";
}

function copyToClipboard() {
  navigator.clipboard.writeText(window.location.href);
  document.getElementsByClassName("copy-to-clipboard-alert")[0].style.display = "block";
  setTimeout(() => document.getElementsByClassName("copy-to-clipboard-alert")[0].style.display = "none", 2000);
}

function makeReservation() {
  const phoneNumberValue = document.getElementsByClassName("phone-number-value")[0].innerText;
  alert(phoneNumberValue + "로 전화해서 예약 부탁드립니다.");
}