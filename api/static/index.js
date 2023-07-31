document.addEventListener("DOMContentLoaded", function () {
  var flashMessage = document.getElementById("flash-message");
  if (flashMessage && flashMessage.innerHTML.trim() !== "") {
    setTimeout(function () {
      flashMessage.style.display = "none";
    }, 2000);
  }
});

// fake data to add
$(document).ready(function () {
  $("#generate-fake-data").click(function (e) {
    e.preventDefault();
    $.ajax({
      url: "/add_fake_data",
      type: "POST",
      success: function (response) {
        alert(response.message);
        // You can refresh the page to see the new data
        location.reload();
      },
      error: function (error) {
        console.log(error);
      },
    });
  });
});
