function toggleFavoritesImage(event) {
  const objectPosition = event.target.style.objectPosition;
  const form = document.form;

  if (objectPosition === "0px 0px") {
    event.target.style.objectPosition = "0 -30px";
    event.currentTarget.value = true;
  }
  else {
    event.target.style.objectPosition = "0 0";
    event.currentTarget.value = false;
  }

  form.action = "/restaurant/my"
  form.submit();
}

function toggleLikesImage(event) {
  const objectPosition = event.target.style.objectPosition;
  const numberOfLikes = parseInt(document.getElementsByClassName("number-of-likes").innerText);
  const form = document.form;

  if (objectPosition === "0px -60px") {
    event.target.style.objectPosition = "0 -90px";
    event.currentTarget.value = true;
    const newLikes = toString(numberOfLikes + 1);
    document.getElementsByClassName("number-of-likes").innerText = newLikes;
    document.getElementsByClassName("number-of-likes").value = newLikes;
  }

  else {
    event.target.style.objectPosition = "0px -60px";
    event.currentTarget.value = false;
    const newLikes = toString(numberOfLikes - 1);
    document.getElementsByClassName("number-of-likes").innerText = newLikes;
    document.getElementsByClassName("number-of-likes").value = newLikes;
  }

  form.action = "/restaurant/likes"
  form.submit();
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