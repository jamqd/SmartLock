from API import API
from upload import upload
import os
from take_photo_function import takePhoto
import switch_button as s
from lock_unlock import lock_unlock 
from light_up_leds import light_up_leds
import time
from sms import send_sms
def addFace(id, api_object):
    img_filename = takePhoto()

    blinker = light_up_leds()

    blinker.lightYellow()
    #get absolute path of photo
    img_abspath = os.path.abspath("images/" + img_filename)

    # url of image of face to add to verified list
    img_url = str(upload(img_filename, img_abspath))
    added_face = api_object.add_face(id, img_url)
    return added_face

def createPerson(name, api_object):
    id = api_object.create_person(name)
    return id
a = API("", "varsity")

try:
    a.create_person_group()
    id = createPerson("josh",a)
    face_count = 0
    button_press = s.button_pressed()
    blinker = light_up_leds()
    if button_press == 1 or button_press == 2:
        while face_count < 3:
            added_face = addFace(id, a)
            print(added_face)
            if added_face != -1:
                face_count += 1
            else:
                blinker.blink('lightBlue', 2, 0.5)
    a.train()
    while(a.get_training_status()['status'] != 'succeeded'):
        print(a.get_training_status()['status'])
    a.get_training_status()['status']
    b = lock_unlock(7)
    blinker = light_up_leds()
    blinker.lightRed()
except KeyboardInterrupt:
    a.delete()
except Exception as e:
    print(e)
    a.delete()

try:
    while(True):
        #IF LOCK IS LOCKED
        if(b.is_locked == True):
            blinker.lightRed()
            which_button_pressed = s.button_pressed()
            if(which_button_pressed==1):
                time.sleep(3)
                query_filename = takePhoto()
                blinker.lightYellow()
                query_abspath = os.path.abspath("images/" + query_filename)
                query_url = upload(query_filename, query_abspath)
                response = a.identify(query_url) 
                if response != -1 and len(response[0]['candidates']) != 0:
                    if(response[0]['candidates'][0]['confidence'] > 0.8):
                        #unlock
                        b.unlock()
                    else:
                        blinker.blink('red',5,0.5)
                else:
                        blinker.blink('red',5,0.5)
            if (which_button_pressed == 0):
                blinker.blink('purple', 10, 0.25)
                send_sms("Your lock was moved at " + str(int(time.time()))+" Be careful!!! ")
         #IF UNLOCKED, PRESS BUTTON TO LOCK
        
        if(b.is_locked == False):
            blinker.lightGreen()
            which_button_pressed = s.button_pressed()
            if(which_button_pressed==1 or which_button_pressed==2):
                if(which_button_pressed==1):
                    b.lock()
                    blinker.lightRed()
                    time.sleep(3)
                    blinker.blink('red',2,0.35)
                if(which_button_pressed==2):
                    id = createPerson(str(int(time.time())),a)
                    face_count = 0
                    time.sleep(2)
                    while face_count < 3:
                        added_face = addFace(id, a)
                        print(added_face)
                        if added_face != -1:
                            face_count += 1
                        else:
                            blinker.blink('lightBlue', 2, 0.5)
                    a.train()
                    while(a.get_training_status()['status'] != 'succeeded'):
                        print(a.get_training_status()['status'])
                    a.get_training_status()['status']
except KeyboardInterrupt:
    a.delete()
except Exception as e:
    print(e)
    b.destroy()
    a.delete()
    
    
b.destroy()
a.delete()