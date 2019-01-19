from API import API


# url of image of face to add to verified list
img_url = ""

a = API("64994017348a42009d7484e0fd2f2cf0", "didy")
a.create_person_group()
id = a.create_person("josh")
a.add_face(id, "https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg")
a.train()
while(a.get_training_status()['status'] != 'succeeded'):
    print(a.get_training_status()['status'])
a.get_training_status()['status']
print(a.identify("https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg"))
a.delete()