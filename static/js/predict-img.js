let base64Img;

$(".image-selector").change(() => {
  let reader = new FileReader();
  reader.onload = () => {
    let dataURL = reader.result;
    $(".selected-img").attr("src", dataURL);

    base64Img = dataURL.replace("data:image/png;base64,", "");
    console.log(base64Img);
  }

  reader.readAsDataURL($(".image-selector")[0].files[0])
  $(".dog-prediction").text("Dog: ");
  $(".cat-prediction").text("Cat: ");
});

$(".predict-img").click(() => {
  message = {
    image: base64Img
  }
  console.log(message);

  $.post("http://localhost:5000/predict", JSON.stringify(message), (response) => {
    $(".dog-prediction").text(`Dog: ${response.prediction.dog.toFixed(6)}`)
    $(".cat-prediction").text(`Cat: ${response.prediction.cat.toFixed(6)}`)
    console.log(response);
  })
})
