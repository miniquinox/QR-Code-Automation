import requests

url = "https://qrcode-monkey.p.rapidapi.com/qr/custom"
data = "https://linktr.ee/Optimiz3D"
for i in range(501):
    number = "{:03d}".format(i)
    new_data = f'{data}{number}'
    payload = {
		"data": new_data,
		"config": {
			"body": "circular",
			"eye": "frame12",
			"eyeBall": "ball14",
			# "bodyColor": "#5C8B29",
			"bgColor": "#000000",
			"gradientColor1": "#FF00F7",
			"gradientColor2": "#00F7FF",
			"gradientType": "linear",
			"gradientOnEyes": True,
			"logo": ""
		},
		"size": 2000,
		"download": True,
		"file": "png"
	}
    headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": "a0df49e7d4mshd45616054150c64p11f3a7jsnaf2661610c0f",
		"X-RapidAPI-Host": "qrcode-monkey.p.rapidapi.com"
	}
    response = requests.request("POST", url, json=payload, headers=headers)
    image_url = response.json().get("imageUrl")
    image_url = f"https:{image_url}"
    print(image_url)
    
	# Download image
    download = requests.get(image_url)
    file = f'{number}.png'
    with open(file, "wb") as f:
        f.write(download.content)
    