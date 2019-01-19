# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cognitive_face as CF

KEY = '93b2cf4c5c8444da9e124d3d02698bec'  # Replace with a valid Subscription Key here.
CF.Key.set(KEY)

BASE_URL = 'https://westus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
CF.BaseUrl.set(BASE_URL)

img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
result = CF.face.detect(img_url)
print (result)