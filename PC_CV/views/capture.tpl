<html>
<head>
  <title>Pizza Challenge - Computer Vision</title>
</head>

<body>

<h1>Pizza Challenge - Computer Vision</h1>



<input type='file' accept="image/*" onchange="readURL(this);" capture/>
<br/>
<button id="btn_snap">Take webcam photo</button>
<video id="video" autoplay></video>

<hr>
<img id="img_preview" src="#" alt="your image" />
<button id="btn_submit">Send image!</button>

<script type="text/javascript">
// Elements for taking the snapshot
var video = document.getElementById('video');
var preview = document.getElementById('img_preview');


// SHOW PREVIEW OF SELECTED IMAGE
function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
      preview.src = e.target.result;
    };
    reader.readAsDataURL(input.files[0]);
  }
}

// SHOW WEBCAM SHOT

// Get access to the camera!
if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Not adding `{ audio: true }` since we only want video now
    navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
        video.src = window.URL.createObjectURL(stream);
        video.play();
    });
}

// Capture from webcam
function captureImage() {
  var scale = 1;
  var canvas = document.createElement("canvas");
  canvas.width = video.videoWidth * scale;
  canvas.height = video.videoHeight * scale;
  canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
  preview.src = canvas.toDataURL();
};



//BUTTONS
document.getElementById("btn_snap").addEventListener("click", captureImage);
document.getElementById("btn_submit").addEventListener(
  "click",
  function(){
    var form = document.createElement("form");
    form.method = "post";
    form.action = "/image";
    var field = document.createElement("input");
    field.type = "text";
    field.name = "image";
    field.value = preview.src;
    form.appendChild(field);
    document.body.appendChild(form);
    form.submit();
  }
);

</script>

</body>
</html>
