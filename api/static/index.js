document.addEventListener("DOMContentLoaded", function () {
  var flashMessage = document.getElementById("flash-message");
  if (flashMessage.innerHTML.trim() !== "") {
    setTimeout(function () {
      flashMessage.style.display = "none";
    }, 2000);
  }
});
