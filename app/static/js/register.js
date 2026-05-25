const video = document.getElementById("video");

navigator.mediaDevices.getUserMedia({
    video: true
})
.then((stream) => {
    video.srcObject = stream;
});

document.getElementById("registerBtn").addEventListener("click", async () => {

    // wait until video fully loads
    if (video.videoWidth === 0) {
        alert("Camera not ready");
        return;
    }

    const canvas = document.createElement("canvas");

    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    const ctx = canvas.getContext("2d");

    ctx.drawImage(video, 0, 0);

    const image = canvas.toDataURL("image/jpeg", 1.0);

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;

    const response = await fetch("/register-face", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name,
            email,
            image
        })
    });

    const data = await response.json();

    document.getElementById("message").innerText = data.message;
});