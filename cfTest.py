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

"""
img_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
result = CF.face.detect(img_url)
print (result)
"""

face_id = result[0].get('faceId')
print (face_id)

CF.person_group.delete('hi')

test = CF.person_group.create('hi')
print("smt here " + str(test))

print(CF.person_group.get('hi'))

person_id = CF.person.create('hi', 'bob')

print(person_id)

#print(CF.person.get('hi', person_id))

CF.person.add_face("Users\icd10\Documents\SmartLock\detection1.jpg", 'hi', person_id)

CF.person_group.delete('hi')
"""

result2 = CF.face.identify([result[0].get('faceId')], person_group_id)

print(result2)
"""