import requests, base64, json

with open('car.jpg', 'rb') as f:
    img_bytes = base64.b64encode(f.read()).decode()

files = {'image': (img_bytes)}
print(files)
r = requests.post(url='https://http-forwarder-aarav-dayals-projects.vercel.app/', json=files)
print(r.content)
print(r.json())