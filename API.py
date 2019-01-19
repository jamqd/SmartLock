import requests

class API:
    face_api_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/detect'
    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise'
    }
    
    def __init__(self, api_key, person_group_name):
        self.headers = { 'Ocp-Apim-Subscription-Key': api_key }
        self.pg_name = person_group_name
    