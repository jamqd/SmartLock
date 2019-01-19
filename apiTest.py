# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 00:24:28 2019

@author: icd10
"""

import requests

headers = { 'Ocp-Acm-Subscription-Key' : '93b2cf4c5c8444da9e124d3d02698bec' }

params = {
        'returnFaceId' : 'true',
        'returnFaceLandmarks' : 'false'
}

face_api_url = 'https://westus.api.cognitive.microsoft.com/face/v1.0/detect?returnFaceId'

response = requests.post(face_api_url, params=params, headers=headers, json={"url": 'https://ideahacksstorage.blob.core.windows.net/pics/bob.jpeg'})
faces = response.json()
print("Hello")
print(faces)