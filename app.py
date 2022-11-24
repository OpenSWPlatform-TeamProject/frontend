from flask import Flask, render_template, request
from database import DBhandler

import sys

application = Flask(__name__)
DB = DBhandler()

#홈 화면
@application.route('/')
def home():
    return render_template("home.html")

#맛집 화면
@application.route('/restaurant/add',methods=['POST', 'GET'])
def add_restaurant():
    if request.method == 'POST':
        image_file=request.files["rfile"]
        image_file.save("static/image/{}".format(image_file.filename))
        data=request.form
        print(data)
        if DB.add_restaurant(data['맛집이름'], data, "/static/image/"+image_file.filename):
            return render_template("result.html", data=data, image_path="/static/image/"+image_file.filename, addmenu_path="/menu/add/"+data['맛집이름'])
        else :
            return "Restaurant name already exist!"
    else :
        return render_template("add-restaurant.html")


@application.route('/restaurant/list')
def restaurant_list():
    return render_template("restaurant-list.html")

@application.route('/restaurant/detail',methods=['POST', 'GET'])
def restaurant_detail():
    if request.method == 'POST':
        data=request.form
        print(data)
        return render_template("result.html", data=data)
    else :
        return render_template("restaurant-detail.html")

@application.route('/restaurant/my')
def my_fav_list():
    return render_template("my-fav-list.html")


#리뷰 화면
@application.route('/review/add',methods=['POST', 'GET'])
def add_review():
    if request.method == 'POST':
        image_file=request.files["rvfile"]
        image_file.save("static/image/{}".format(image_file.filename))
        data=request.form
        print(data)
        if DB.add_review(data['맛집이름'], data, "/static/image/"+image_file.filename):
            return render_template("result.html", data=data, image_path="/static/image/"+image_file.filename, addreview_path="/review/add/"+data['맛집이름'])
        else :
            return "Error!"
    else :
        return render_template("add-review.html")


@application.route('/review/list')
def review_list():
    return render_template("review-list.html")
    
@application.route('/review/detail')
def review_detail():
    return render_template("review-detail.html")

@application.route('/review/my/detail')
def myreveiw_detail():
    return render_template("myreview-detail.html")


#메뉴 화면
@application.route('/menu/add/<string:restaurant>',methods=['POST', 'GET'])
def add_menu(restaurant):
    if request.method == 'POST':
        image_file=request.files["mfile"]
        image_file.save("static/image/{}".format(image_file.filename))
        data=request.form
        print(data)
        if DB.add_menu(data['맛집이름'], data, "/static/image/"+image_file.filename):
            return render_template("result.html", data=data, image_path="/static/image/"+image_file.filename, addmenu_path="/menu/add/"+data['맛집이름'])
        else :
            return "Error!"
    else :
        return render_template("add-menu.html", 맛집이름=restaurant)

@application.route('/menu/list')
def menu_list():
    return render_template("menu-list.html")

#로그인 화면
@application.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data=request.form
        print(data)
        return render_template("home.html")
    else :
        return render_template("login.html")
    

#회원가입 화면
@application.route('/signup', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        data=request.form
        print(data)
        return render_template("home.html")
    else :
        return render_template("sign-up.html")

#마이페이지
@application.route('/mypage')
def mypage():
    return render_template("mypage.html")



if __name__ == "__main__":
    application.run(host='0.0.0.0') 