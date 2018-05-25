<html>

<head>
  <title>Pizza Challenge - Computer Vision</title>
</head>

<body>
<h1>Pizza Challenge - Computer Vision</h1>

<!-- Tell me what you see!! -->
% if topic=="nothing":
<h2>I can't see anything. I'm blind!</h2>
% end
% if topic!="nothing":
<h2>I see a {{ topic }}</h2>
% end

<!-- Can you read anything? -->
% if ocr_lines:
<h2>I can read:</h2>
<ul>
  % for line in ocr_lines:
  <li>{{ line }}</li>
  % end
</ul>
% end

<!-- Show me the modified image -->
<h3>This is your processed image</h3>
<img src="{{ image }}" />
<button id="btn_submit" onclick="window.location.href='/'">Back home</button>
</body>
</html>
