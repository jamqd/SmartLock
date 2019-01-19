import requests

class API:
    
    def __init__(self, api_key, person_group_name):
        self.headers = { 'Ocp-Apim-Subscription-Key': api_key }
        self.pg_name = person_group_name
        self.base_url = "https://westus.api.cognitive.microsoft.com/face/v1.0/"

    def create_person_group(self):
        """
        Creates person group with id as pg_name and name as name
        """
        url = self.base_url + "persongroups/" + self.pg_name
        response = requests.put(url, headers=self.headers, json={"name" : self.pg_name})
        if response.status_code == 200 :
            print("added " + self.pg_name +  " person group")
        else:
            print(response.json())

    def create_person(self, name):
        url = self.base_url + "persongroups/" + self.pg_name + "/persons"
        response = requests.post(url, headers=self.headers, json={"name": name})
        r_json = response.json()
        print(r_json)
        person_id = r_json['personId']
        return person_id
    
    def add_face(self, person_id, img_url):
        url = self.base_url + "persongroups/" + self.pg_name + "/persons/" + person_id + "/persistedFaces"
        response = requests.post(url, headers=self.headers, json={"url": img_url})
        r_json = response.json()
        print(r_json)
        face_id = r_json['persistedFaceId']
        return face_id

    def delete(self):
        url = self.base_url + "persongroups/" + self.pg_name
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 200 :
            print("deleted " + self.pg_name +  " person group")
        else:
            print(response.json())


a = API("64994017348a42009d7484e0fd2f2cf0", "didy")
a.create_person_group()
id = a.create_person("josh")
a.add_face(id, "https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg")
a.delete()

    