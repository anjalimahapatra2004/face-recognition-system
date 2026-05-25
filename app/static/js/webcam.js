const video = document.getElementById("video");

navigator.mediaDevices.getUserMedia({
    video: {
        width: 640,
        height: 480
    }
})
.then((stream) => {

    video.srcObject = stream;

})
.catch((err) => {

    console.log("Camera Error:", err);

});


function captureFace() {

    const canvas =
        document.createElement("canvas");

    canvas.width = video.videoWidth;

    canvas.height = video.videoHeight;

    const ctx =
        canvas.getContext("2d");

    ctx.drawImage(
        video,
        0,
        0,
        canvas.width,
        canvas.height
    );

    const imageData =
        canvas.toDataURL(
            "image/jpeg",
            1.0
        );

    localStorage.setItem(
        "face_image",
        imageData
    );

    console.log(imageData);

    alert("Face Scan Successful");
}