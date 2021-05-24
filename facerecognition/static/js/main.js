const video = document.getElementById('video')

let cam
let width = 350
let height = 350

function setup() {

    const form = document.getElementById('photoForm')
    const button = document.getElementById('enter')

    cam = createCapture(VIDEO)
    cam.size(width, height)
    cam.hide()

    createCanvas(width, height)

    button.addEventListener('click', () => {
        cam.loadPixels()
        let data = cam.canvas.toDataURL("image/png")
        data = data.replace(/^data:image\/(png|jpg);base64,/, "");
        form.value = data
    })
}


function draw(){
    image(cam, 0 ,0, width, height)
}
