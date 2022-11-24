from flask import Flask, render_template, request, redirect, url_for
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
    page = request.args.get("page", 0, type=int)
    limit = 9
    start_idx=limit*page
    end_idx=limit*(page+1)
    data = DB.get_restaurants()
    total = len(data)
    datas=dict(list(data.items())[start_idx:end_idx])
    print(datas)
    return render_template("restaurant-list.html", datas=datas, total=total, limit=limit, page=page, page_count=int((total/9)+1))

@application.route('/restaurant/themelist')
def restaurant_themelist():
    page = request.args.get("page", 0, type=int)
    limit = 9
    start_idx=limit*page
    end_idx=limit*(page+1)
    data = DB.get_restaurants()
    total = len(data)
    datas=dict(list(data.items())[start_idx:end_idx])
    print(datas)
    return render_template("theme-list.html", datas=datas, total=total, limit=limit, page=page, page_count=int((total/9)+1))
    
@application.route('/restaurant/detail/<string:restaurant>',methods=['POST', 'GET'])
def restaurant_detail(restaurant):
    data=DB.get_restaurant_byname(str(restaurant))
    print(data)
    if request.method == 'POST':
        comment=request.form
        print(comment)
        return render_template("restaurant-detail.html", 맛집이름=restaurant, data=data, menulist_path="/menu/list/"+restaurant, reviewlist_path="/review/list/"+restaurant, addreview_path="/review/add/"+restaurant)
    else :
        return render_template("restaurant-detail.html", 맛집이름=restaurant, data=data, menulist_path="/menu/list/"+restaurant, reviewlist_path="/review/list/"+restaurant, addreview_path="/review/add/"+restaurant)

@application.route('/restaurant/my')
def my_fav_list():
    return render_template("my-fav-list.html")


#리뷰 화면
@application.route('/review/add/<string:restaurant>',methods=['POST', 'GET'])
def add_review(restaurant):
    if request.method == 'POST':
        image_file=request.files["rvfile"]
        image_file.save("static/image/{}".format(image_file.filename)) 
        data=request.form
        print(data)
        if DB.add_review(restaurant, data, "/static/image/"+image_file.filename):
            return redirect(url_for('review_list', restaurant=restaurant))
        else :
            return "Error!"
    else :
        return render_template("add-review.html", 맛집이름=restaurant)

@application.route('/review/list/<string:restaurant>')
def review_list(restaurant):
    page = request.args.get("page", 0, type=int)
    limit = 9
    start_idx=limit*page
    end_idx=limit*(page+1)
    data = DB.get_reviews(restaurant)
    total = len(data)
    datas=dict(list(data.items())[start_idx:end_idx])
    print(data)
    return render_template("review-list.html", datas=datas, 맛집이름=restaurant, total=total, limit=limit, page=page, page_count=int((total/9)+1))   
    
@application.route('/review/detail')
def review_detail():
    return render_template("review-detail.html")

@application.route('/review/my')
def myreview_list():
    return render_template("review-list.html")

@application.route('/review/my/detail')
def myreview_detail():
    return render_template("myreview-detail.html")


#메뉴 화면
@application.route('/menu/add/<string:restaurant>',methods=['POST', 'GET'])
def add_menu(restaurant):
    if request.method == 'POST':
        image_file=request.files["mfile"]
        image_file.save("static/image/{}".format(image_file.filename))
        data=request.form
        print(data)
        if DB.add_menu(restaurant, data, "/static/image/"+image_file.filename):
            return redirect(url_for('restaurant_detail', restaurant=restaurant))
        else :
            return "Error!"
    else :
        return render_template("add-menu.html", 맛집이름=restaurant)

@application.route('/menu/list/<string:restaurant>')
def menu_list(restaurant):
    datas = DB.get_menus(restaurant)
    print(datas)
    if(datas) :
        tot_count = len(datas)
        return render_template("menu-list.html", datas=datas, 맛집이름=restaurant, total=tot_count)
    else :
        return "Error!"

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
    page = request.args.get("page", 0, type=int)
    limit = 9
    start_idx=limit*page
    end_idx=limit*(page+1)
    data = DB.get_restaurants()
    total = len(data)
    datas=dict(list(data.items())[start_idx:end_idx])
    print(datas)
    return render_template("mypage.html", datas=datas, total=total, limit=limit, page=page, page_count=int((total/9)+1))




if __name__ == "__main__":
    application.run(host='0.0.0.0') 