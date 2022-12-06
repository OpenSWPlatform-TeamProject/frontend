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
            value = res.val()
            if value['맛집이름'] == name:
                return False
            return True 

    def menu_duplicate_check(self, rest, name):
        menus = self.db.child("menu").get()
        for men in menus.each():
            value = men.val()
            if value['맛집이름'] == rest:
                if value['메뉴이름'] == name:
                    return False
            return True 

    #맛집등록
    def add_restaurant(self, name, data, img_path):
        restaurant_info ={
            "맛집이름":name,
            "음식종류":data.getlist('음식종류'),
            "vegan":data['vegan'],
            "pricerange":data['pricerange'],
            "location":data['location'],
            "address":data['address'],
            "phonenum":data['phonenum'],
            "parking":data['parking'],
            "mondaytime":data['mondaytime'],
            "tuesdaytime":data['tuesdaytime'],
            "wednesdaytime":data['wednesdaytime'],
            "thursdaytime":data['thursdaytime'],
            "fridaytime":data['fridaytime'],
            "saturdaytime":data['saturdaytime'],
            "sundaytime":data['sundaytime'],
            "isBreaktime":data['isBreaktime'],
            "breakday":data.getlist('breakday'),

            "img_path":img_path
        } 
        print(restaurant_info)
        if self.restaurant_duplicate_check(name):
            self.db.child("restaurant").push(restaurant_info)
            print(data,img_path)
            return True
        else : 
            return False

    #리뷰등록
    def add_review(self, name, data, img_path):
        review_info ={
            "맛집이름":name,
            "메뉴이름":data['메뉴이름'],
            # "평점?":data['평점?'],
            "timePeriod":data['timePeriod'],
            "waiting":data['waiting'],
            "리뷰작성내용":data['리뷰작성내용'],
            "img_path":img_path
        }
        print(review_info)
        self.db.child("review").push(review_info)
        print(data,img_path)
        return True

    #대표메뉴등록
    def add_menu(self, name, data, img_path):
        print(name)
        menu_info ={
            "맛집이름":name,
            "메뉴이름":data['메뉴이름'],
            "img_path":img_path,
            "가격":data['가격'],
            "allergyinfo":data['allergyinfo'],
            "vegan":data['vegan'],
            "etcinfo":data['etcinfo'],
            "한줄소개":data['한줄소개'],
        }
        print(menu_info)
        if self.menu_duplicate_check(name, data['메뉴이름']):
            self.db.child("menu").push(menu_info)
            print(data,img_path)
            return True
        else : 
            return False

    #레스토랑 테이블 가져오기
    def get_restaurants(self ):
        restaurants = self.db.child("restaurant").get().val()
        return restaurants

    #맛집이름으로 맛집 정보 가져오기
    def get_restaurant_byname(self, name):
        restaurants = self.db.child("restaurant").get()
        target_value=""
        for res in restaurants.each():
            value = res.val()
            if value['맛집이름'] == name:
                target_value=value
        return target_value

    #리뷰 테이블 가져오기
    def get_reviews(self, name):
        reviews = self.db.child("review").get()
        target_value={}
        for rev in reviews.each():
            value = rev.val()
            if value['맛집이름'] == name:
                writer=value['img_path']
                target_value[writer]=dict((list(value.items())))
        print(target_value)
        return target_value

    #메뉴 테이블 가져오기
    def get_menus(self, name):
        menus = self.db.child("menu").get()
        target_value={}
        for men in menus.each():
            value = men.val()
            if value['맛집이름'] == name:
                menu=value['메뉴이름']
                target_value[menu]=dict((list(value.items())))
        print(target_value)
        return target_value

    #회원가입
    def insert_user(self, data, pw):
        user_info={
            "id":data['id'],
            "pw":pw,
            "nickname":data['nickname']
        }
        if self.user_duplicate_check(str(data['id'])):
            self.db.child("user").push(user_info)
            print(data)
            return True
        else:
            return False
    
    def user_duplicate_check(self, id_string):
        users=self.db.child("user").get()

        print("users###", users.val())
        if str(users.val()) == "None":
            return True
        else:
            for res in users.each():
                value=res.val()
            
            if value['id']==id_string:
                return False
            return True

    #로그인
    def find_user(self, id, pw):
        users = self.db.child("user").get()
        for res in users.each():
            value = res.val()
        if value['id'] == id and value['pw'] == pw:
            return True
        return False

    def get_nickname(self, id, pw):
        users = self.db.child("user").get()
        for res in users.each():
            value = res.val()
        if value['id'] == id and value['pw'] == pw:
            return value['nickname']

    #탈퇴하기
    def withdrawl(self, id, pw):
        users = self.db.child("user").get()
        for res in users.each():
            value = res.val()
        if value['id'] == id and value['pw'] == pw:
            return self.db.child("user").removeValue()
        return False