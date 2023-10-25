$("#name-btn").click(() => {
  let message = {
    name: $("#name-input").val()
  }
  $.post("http://localhost:5000/hello", JSON.stringify(message), (response) => {
    $("#greeting").text(response.greeting);
    console.log(response);
  });
});