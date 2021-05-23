const video = document.getElementById('value')

let cam

function setup() {

  const form = document.getElementById('photoForm')
  const button = document.getElementById('enter')

  cam = createCapture(VIDEO)

  button.addEventListener('click', ()=>{
    cam.loadPixels()
    let data = cam.canvas.toDataURL("image/png")
    data = data.replace(/^data:image\/(png|jpg);base64,/, "");
    form.value = data
  })

  noCanvas();
}

// function startapp(){
//   navigator.mediaDevices.getUserMedia({
//     video: true,
//     audio: false,
//   }).then(stream => {
//     video.srcObject = stream
//   })
//
// }
//
// window.addEventListener('load', startapp, false)