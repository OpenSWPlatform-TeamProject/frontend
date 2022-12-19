function toggleFavoritesImage(event) {
  const objectPosition = event.target.style.objectPosition;
  if (objectPosition === "0px 0px") {
    event.target.style.objectPosition = "0 -30px";
  }
  else {
    event.target.style.objectPosition = "0 0";
  }
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