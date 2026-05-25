const video = document.getElementById("video");

navigator.mediaDevices.getUserMedia({
    video: true
})
.then((stream) => {
    video.srcObject = stream;
});

document.getElementById("loginBtn").addEventListener("click", async () => {

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

    const response = await fetch("/login-face", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            image
        })
    });

    const data = await response.json();

    document.getElementById("message").innerText = data.message;
});