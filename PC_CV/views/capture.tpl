<html>

<head>
	<title>Pizza Challenge - Computer Vision</title>
	<link href="https://fonts.googleapis.com/css?family=Raleway" rel="stylesheet">
	<style>
		* {
			margin: 0;
			padding: 0;
			box-sizing: border-box;
		}

		body {
			font-family: 'Raleway', sans-serif;
			font-size: 16px;
			padding-bottom: 10vh;
		}

		button {
			display: inline-block;
			vertical-align: top;
			width: auto;
			height: auto;
			padding: 2vh 5vw;
			outline: 0;
			background: #ddd;
			color: #555;
			border: 1px solid #ccc;
			font-size: inherit; 
			text-align: center;
			font-family: 'Raleway', sans-serif;
			transition: all .2s ease-in-out;
			cursor: pointer;
		}

		button:hover, 
		button:active { background: #eee; }

		button.secondary {
			background: transparent;
			border-color: #777;
			color: #777;
		}

		button.secondary:hover,
		button.secondary:active {
			border-color: #444;
			color: #444;
		}

		header {
			display: inline-block;
			vertical-align: top;
			width: 100%;
			height: auto;
			padding: 10vh 0;
			text-align: center;
		}

		header h2 { color: #777; }

		#input-selector {
			display: inline-block;
			vertical-align: top;
			width: 90%;
			margin: 0 5%;
			height: auto;

			display: flex;
			flex-wrap: nowrap;
			justify-content: space-around;
			align-items: center;
		}

		#dropdown {
			display: inline-block;
			vertical-align: top;
			position: relative;
			width: 35vw;
			height: 35vw;
			border: 4px dashed #ccc;
			transition: all .2s ease-in-out;
		}

		#dropdown:hover { border-color: #777; }
		#dropdown:hover span { color: #444; }

		#dropdown input {
			position: absolute;
			top: 0; left: 0;
			width: 100%;
			height: 100%;
			opacity: 0;
			z-index: 1;
		}

		#dropdown input:hover,
		#dropdown input:active {
			cursor: pointer;
		}

		#dropdown span {
			position: absolute;
			width: 100%;
			top: 50%; left: 0;
			transform: translateY(-50%);
			color: #888;
			text-align: center;
			z-index: -1;
			transition: all .2s ease-in-out;
		}

		#webcam {
			display: inline-block;
			vertical-align: top;
			position: relative;
			width: 35vw;
			height: 35vw;
		}

		#webcam video {
			display: inline-block;
			vertical-align: top;
			width: 100%;
			height: auto;
		}

		#webcam button {
			position: absolute;
			width: 100%;
			bottom: 0;
			left: 0;
			text-align: center;
		}

		#result {
			display: inline-block;
			vertical-align: top;
			width: 90%;
			height: auto;
			margin: 0 5%;
			text-align: center;
		}

		#result img {
			display: block;
			max-width: 35vw;
			margin: 0 auto 5vh;
		}

		#result button {
			margin: 0 2vw;
		}

		.hide { display: none!important; }
	</style>
</head>

<body>
	<header>
		<h1>Computer Vision</h1>
		<h2>Pizza Challenge</h2>
	</header>

	<section id="input-selector">
		<div id="dropdown">
			<input type='file' accept="image/*" onchange="readURL(this);" capture/>	
			<span>Click or drop your file here</span>
		</div>
		<span>OR</span>
		<section id="webcam">
			<video id="video" autoplay></video>
			<button type="button" onclick="captureImage()">Take a picture!</button>
		</section>
	</section>
	
	<section id="result" class="hide">
		<img id="img_preview" src="#" alt="your image" />
		<button type="button" class="secondary" onclick="showInputs();">Repeat image</button>
		<button type="button" id="btn_submit">Send image!</button>
	</section>
	
	<script type="text/javascript">
		// Elements for taking the snapshot
		var video = document.getElementById('video');
		var preview = document.getElementById('img_preview');

		// SHOW PREVIEW OF SELECTED IMAGE
		function readURL(input) {
			if (input.files && input.files[0]) {
				var reader = new FileReader();
				reader.onload = function(e) {
					preview.src = e.target.result;
				};
				reader.readAsDataURL(input.files[0]);
				showResults();
			}
		}

		// SHOW WEBCAM SHOT

		// Get access to the camera!
		if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
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

			showResults();
		};

		//BUTTONS
		document.getElementById("btn_submit").addEventListener(
			"click",
			function() {
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

		function showInputs() {
			var inputs = document.querySelector("#input-selector");
			inputs.classList.remove("hide");

			var res = document.querySelector("#result");
			res.classList.add("hide");
		}

		function showResults() {
			var res = document.querySelector("#result");
			res.classList.remove("hide");

			var inputs = document.querySelector("#input-selector");
			inputs.classList.add("hide");
		}
	</script>
</body>

</html>