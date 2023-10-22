$("#name-btn").click(() => {
  let message = {
    name: $("#name-input").val()
  }
  $.post("http://127.0.0.1:5000/hello", JSON.stringify(message), (response) => {
    $("#greeting").text(response.greeting);
    console.log(response);
  });
});