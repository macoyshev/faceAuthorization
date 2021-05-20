function setup() {

  const form = document.getElementById('photoForm')
  const button = document.getElementById('enter')
  const video = createCapture(VIDEO)

  video.size(400,300)

  button.addEventListener('click', ()=>{
    video.loadPixels()
    let data = video.canvas.toDataURL("image/png")
    data = data.replace(/^data:image\/(png|jpg);base64,/, "");
    form.value = data
  })

  noCanvas();
}