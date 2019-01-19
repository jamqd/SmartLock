from API import API
from upload import upload
import os
from take_photo_function import takePhoto



img_filename = takePhoto()


#get absolute path of photo
img_abspath = os.path.abspath("images/" + img_filename)

# url of image of face to add to verified list
img_url = str(upload(img_filename, img_abspath))

a = API("64994017348a42009d7484e0fd2f2cf0", "verified")
a.create_person_group()
id = a.create_person("josh")
a.add_face(id, img_url)
a.train()
while(a.get_training_status()['status'] != 'succeeded'):
    print(a.get_training_status()['status'])
a.get_training_status()['status']

query_filename = takePhoto()
query_abspath = os.path.abspath("images/" + query_filename)
query_url = upload(query_filename, query_abspath)
print(a.identify(query_url))
a.delete()