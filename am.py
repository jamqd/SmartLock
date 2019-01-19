
face_api_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/detect'

image_url = 'https://how-old.net/Images/faces2/main007.jpg'

import requests

headers = { 'Ocp-Apim-Subscription-Key': '64994017348a42009d7484e0fd2f2cf0' }
    
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
}

response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})
faces = response.json()
print(faces)


# creating person group
person_group_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/fus'

headers = { 'Ocp-Apim-Subscription-Key': '64994017348a42009d7484e0fd2f2cf0' }


response = requests.put(person_group_url, headers=headers, json={"name" : "test1"})
if response.status_code == 200 :
    print("added person group")
else:
    print(response.json())
    
create_person_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/fus/persons'
response = requests.post(create_person_url, headers=headers, json={"name": "bob"})
person_id = response.json()
print(person_id)
    

add_face_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/persongroups/fus/persons/'+ str(person_id['personId'])+ '/persistedFaces'
response = requests.post(add_face_url, headers=headers, json={"url": "https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg"})
test = response.json()
print(test)

