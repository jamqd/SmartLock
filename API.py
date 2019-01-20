import requests

class API:
    """
    Class for API requests for one person group

    self.pg_name: the personGroupId
    self.base_url: the base url for the Azure face API

    """
    
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
        """
        Creates a person with name as name belonging to the person group self.pg_name

        name: the name of the person added
        """
        url = self.base_url + "persongroups/" + self.pg_name + "/persons"
        response = requests.post(url, headers=self.headers, json={"name": name})
        r_json = response.json()
        person_id = r_json['personId']
        return person_id
    
    def add_face(self, person_id, img_url):
        url = self.base_url + "persongroups/" + self.pg_name + "/persons/" + person_id + "/persistedFaces"
        response = requests.post(url, headers=self.headers, json={"url": img_url})
        r_json = response.json()
        print(r_json)
        if 'error' in r_json.keys():
            return -1
        face_id = r_json['persistedFaceId']
        return face_id

    def delete(self):
        url = self.base_url + "persongroups/" + self.pg_name
        response = requests.delete(url, headers=self.headers)
        if response.status_code == 200 :
            print("deleted " + self.pg_name +  " person group")
        else:
            print(response.json())

    def train(self):
        url = self.base_url + "persongroups/" + self.pg_name + "/train"
        response = requests.post(url, headers=self.headers)
        if response.status_code == 202 :
            print("Started training  " + self.pg_name +  " person group")
        else:
            print(response.json())

    def get_training_status(self):
        url = self.base_url + "persongroups/" + self.pg_name + "/training"
        response = requests.get(url, headers=self.headers)
        print(response.json())
        return response.json()

    def identify(self, query_face_url):
        faceId = self.detect(query_face_url)
        if faceId == -1:
            return -1
        url = self.base_url + "identify"
        json = {
            "faceIds": [faceId],
            "personGroupId": self.pg_name
        }
        response = requests.post(url, headers=self.headers, json=json)
        print(response.json())
        return response.json()

    def detect(self, query_face_url):
        url = self.base_url + "detect"
        response = requests.post(url, headers = self.headers, params={"returnFaceId":"true"}, json={"url": query_face_url} )
        print("here" + str(response.json()))
        if len(response.json()) != 0:
            return response.json()[0]['faceId']
        else:
            return -1


    