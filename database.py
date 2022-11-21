import pyrebase
import json

class DBhandler:
    def __init__(self) :
        with open('./authentication/firebase_auth.json') as f:
            config=json.load(f)

        firebase = pyrebase.initialize_app(config)
        self.db = firebase.database()

    def restaurant_duplicate_check(self, name):
        restaurants = self.db.child("restaurant").get()
        for res in restaurants.each():
            if res.key() == name:
                return False
            return True 

    def add_restaurant(self, name, data, img_path):
        restaurant_info ={
            "음식종류":data['음식종류'],
            "vegan":data['vegan'],
            "pricerange":data['pricerange'],
            "location":data['location'],
            "address":data['address'],
            "phonenum":data['phonenum'],
            "parking":data['parking'],
            #월
            "mondaytime":data['mondaytime'],
            "mondaybreak":data['mondaybreak'],
            #화
            "tuesdaytime":data['tuesdaytime'],
            "tuesdaybreak":data['tuesdaybreak'],
            #수
            "wednesdaytime":data['wednesdaytime'],
            "wednesdaybreak":data['wednesdaybreak'],
            #목
            "thursdaytime":data['thursdaytime'],
            "thursdaybreak":data['thursdaybreak'],
            #금
            "fridaytime":data['fridaytime'],
            "fridaybreak":data['fridaybreak'],
            #토
            "saturdaytime":data['saturdaytime'],
            "saturdaybreak":data['saturdaybreak'],
            #일
            "sundaytime":data['sundaytime'],
            "sundaybreak":data['sundaybreak'],

            "isBreaktime":data['isBreaktime'],

            "img_path":img_path
        }
        if self.restaurant_duplicate_check(name):
            self.db.child("restaurant").child(name).set(restaurant_info)
            print(data,img_path)
            return True
        else : 
            return False
