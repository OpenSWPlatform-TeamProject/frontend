import sys

from flask import Flask, render_template, request

application = Flask(__name__)

#홈 화면
@application.route('/')
def home():
    return render_template("home.html")

#맛집 화면
@application.route('/restaurant/add',methods=['POST', 'GET'])
def add_restaurant():
    if request.method == 'POST':
        data=request.form
        return render_template("result.html", data=data)
    else :
        return render_template("add-restaurant.html")

@application.route('/restaurant/list')
def restautrant_list():
    return render_template("restaurant-list.html")

@application.route('/restaurant/detail',methods=['POST', 'GET'])
def restautrant_detail():
    if request.method == 'POST':
        data=request.form
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
        data=request.form
        return render_template("result.html", data=data)
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
@application.route('/menu/add',methods=['POST', 'GET'])
def add_menu():
    if request.method == 'POST':
        data=request.form
        return render_template("result.html", data=data)
    else :
        return render_template("add-menu.html")

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