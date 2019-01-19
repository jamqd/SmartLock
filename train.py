from API import API
from upload import upload
import os
from take_photo_function import takePhoto
import switch_button as switch
import lock_unlock 


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

while(True):
    #IF LOCK IS LOCKED
    if(lock_unlock.locked == True):
        if(switch.test_button_was_pressed()==True):
            query_filename = takePhoto()
            query_abspath = os.path.abspath("images/" + query_filename)
            query_url = upload(query_filename, query_abspath)
            response = a.identify(query_url) 
            print(response)
            if(response[0]['candidates'][0]['confidence'] > 0.9):
                #unlock
                lock_unlock.unlock()
     #IF UNLOCKED, PRESS BUTTON TO LOCK     
    if(lock_unlock.locked == False):
        if(switch.test_button_was_pressed()==True):
            lock_unlock.lock()
    

a.delete()