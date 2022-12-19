from flask import Flask, render_template, request, flash, redirect, url_for, session
from database import DBhandler
import hashlib
import sys
import math

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
            return redirect(url_for('restaurant_detail', restaurant=data['맛집이름']))
        else :
            return "Restaurant name already exist!"
    else :
        return render_template("add-restaurant.html")

@application.route('/restaurant/addmenu',methods=['POST', 'GET'])
def add_restaurant_menu():
    if request.method == 'POST':
        image_file=request.files["rfile"]
        image_file.save("static/image/{}".format(image_file.filename))
        data=request.form
        print(data)
        if DB.add_restaurant(data['맛집이름'], data, "/static/image/"+image_file.filename):
            return redirect(url_for('add_menu', restaurant=data['맛집이름']))
        else :
            return "Restaurant name already exist!"
    else :
        return render_template("add-restaurant.html")

@application.route('/restaurant/list')
def restaurant_list():
    location = request.args.get("location", "all", type=str)
    foodtype = request.args.get("foodtype", "all", type=str)
    sort = request.args.get("sort", "", type=str)
    search = request.args.get("search", "", type=str)
    page = request.args.get("page", 0, type=int)
    theme = request.args.get("theme", 0, type=int)

    print(location)
    print(foodtype)
    print(sort)
    print(search)
    print(theme)

    data = DB.get_restaurants_bycondition(location, foodtype, search, theme)
    
    total = len(data)
    limit = 9
    if page<0:
        return redirect(url_for('restaurant_list', page=0))
    elif page>(math.ceil(total/limit)-1):
        return redirect(url_for('restaurant_list', page=math.ceil(total/limit)-1))
    start_idx=limit*page
    end_idx=limit*(page+1)

    if total<=limit:
        if sort=="newest" :
            data = dict(sorted(data.items(), key=lambda x: x[1]['timestamp'], reverse=True)[:total])
        elif sort=="best" :
            data = dict(sorted(data.items(), key=lambda x: x[1]['평점'], reverse=True)[:total])
        else : data = dict(sorted(data.items(), key=lambda x: x[1]['맛집이름'], reverse=False)[:total])
    else:
        if sort=="newest" :
            data = dict(sorted(data.items(), key=lambda x: x[1]['timestamp'], reverse=True))
        elif sort=="best" :
            data = dict(sorted(data.items(), key=lambda x: x[1]['평점'], reverse=True))
        else : data = dict(sorted(data.items(), key=lambda x: x[1]['맛집이름'], reverse=False))

    datas=dict(list(data.items())[start_idx:end_idx])
    print(datas)
    if theme>0:
        return render_template("theme-list.html", datas=datas, location=location, foodtype=foodtype, sort=sort, search=search, theme=theme, total=total, limit=limit, page=page, page_count=math.ceil(total/limit))
    return render_template("restaurant-list.html", datas=datas, location=location, foodtype=foodtype, sort=sort, search=search, total=total, limit=limit, page=page, page_count=math.ceil(total/limit))

@application.route('/restaurant/detail/<string:restaurant>',methods=['POST', 'GET'])
def restaurant_detail(restaurant):
    data=DB.get_restaurant_byname(str(restaurant))
    print(data)
    data2=DB.get_menus(restaurant)
    leng=len(data2)
    coms=DB.get_comments(restaurant)
    comtot=len(coms)
    return render_template("restaurant-detail.html", 맛집이름=restaurant, data=data, data2=data2, coms=coms, comtot=comtot, leng=leng, menulist_path="/menu/list/"+restaurant, reviewlist_path="/review/list/"+restaurant, addreview_path="/review/add/"+restaurant)

@application.route('/restaurant/comment/<string:restaurant>',methods=['POST', 'GET'])
def restaurant_comment(restaurant):
    if request.method == 'POST':
        data=request.form
        id=session['id']
        nickname=session['nickname']
        print(data)
        if DB.add_comment(restaurant, data, id, nickname):
            return redirect(url_for('restaurant_detail', restaurant=restaurant))
        else :
            return "Error!"
    else :
        return redirect(url_for('restaurant_detail', restaurant=restaurant))

#@application.route('/restaurant/my')
#def my_fav_list():
#    id=session['id']
#    isFavorite=session['isFavorite']
#    data = DB.get_users(id, isFavorite)
#    print(data)
#    if(data):
#        tot_count=len(data)
#        return render_template("my-fav-list.html", data=data, total=tot_count)
#    else:
#        return "Error!"

#리뷰 화면
@application.route('/review/add/<string:restaurant>',methods=['POST', 'GET'])
def add_review(restaurant):
    if request.method == 'POST':
        image_file=request.files["rvfile"]
        image_file.save("static/image/{}".format(image_file.filename)) 
        data=request.form
        id=session['id']
        nickname=session['nickname']
        print(data)
        if DB.add_review(restaurant, data, id, nickname, "/static/image/"+image_file.filename):
            return redirect(url_for('review_list', restaurant=restaurant))
        else :
            return "Error!"
    else :
        return render_template("add-review.html", 맛집이름=restaurant)

@application.route('/review/list/<string:restaurant>')
def review_list(restaurant):
    page = request.args.get("page", 0, type=int)
    limit = 6
    start_idx=limit*page
    end_idx=limit*(page+1)
    data = DB.get_reviews(restaurant)
    total = len(data)
    datas=dict(list(data.items())[start_idx:end_idx])
    print(data)
    return render_template("review-list.html", datas=datas, 맛집이름=restaurant, total=total, limit=limit, page=page, page_count=int((total/6)+1))   
    
@application.route('/review/detail/<string:restaurant>')
def review_detail(restaurant):
    page = request.args.get("page", 0, type=int)
    limit = 1
    idx=limit*page
    data = DB.get_reviews(restaurant)
    total = len(data)
    review=list(data.items())[idx]
    print(review)
    print(review[1])
    return render_template("review-detail.html", data=review, 맛집이름=restaurant, page=page, total=total)   
    
@application.route('/review/my')
def myreview_list():
    id=session['id']
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

@application.route('/menu/addanother/<string:restaurant>',methods=['POST', 'GET'])
def add_more_menu(restaurant):
    if request.method == 'POST':
        image_file=request.files["mfile"]
        image_file.save("static/image/{}".format(image_file.filename))
        data=request.form
        print(data)
        if DB.add_menu(restaurant, data, "/static/image/"+image_file.filename):
            return redirect(url_for('add_menu', restaurant=restaurant))
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
        id=request.form['id']
        pw=request.form['pw']
        pw_hash=hashlib.sha256(pw.encode('utf-8')).hexdigest()
        print(id)
        print(pw)
        print(pw_hash)
        if DB.find_user(id, pw_hash):
            session['id']=id
            session['nickname']=DB.get_nickname(id, pw_hash)
            return render_template("home.html")
        else :
            flash("아이디 또는 비밀번호가 틀렸습니다")
            return redirect(url_for('login'))
    else :
        return render_template("login.html")
    

#회원가입 화면
@application.route('/signup', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        data=request.form
        pw=request.form['pw']
        pw_hash=hashlib.sha256(pw.encode('utf-8')).hexdigest()
        print(data)
        if DB.insert_user(data, pw_hash):
            return render_template("login.html")
        else:
            flash("중복된 ID 입니다!")
            return render_template("sign-up.html")
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

#로그아웃 
@application.route("/logout") 
def logout_user(): 
    session.clear() 
    return redirect(url_for('home')) 

#탈퇴하기 화면 
@application.route('/withdrawl', methods=['POST', 'GET'])
def withdrawl():
    if request.method == 'POST':
        id=session['id']
        pw=request.form['pw']
        pw_hash=hashlib.sha256(pw.encode('utf-8')).hexdigest()
        print(id)
        print(pw)
        print(pw_hash)
        if DB.withdrawl(id, pw_hash):
            session.clear()
            return redirect(url_for('home'))
        else :
            flash("비밀번호가 틀렸습니다")
            return redirect(url_for('withdrawl'))
    else :
        return render_template("withdrawl.html")

#마이페이지
#좋아요 수 
@application.route('/restaurant/likes/<string:restaurant>', methods=['POST', 'GET'])
def like_num(restaurant):
    if DB.like_num(restaurant):
        return redirect(url_for('restaurant_detail', restaurant=restaurant))
    else :
        return redirect(url_for('restaurant_detail', restaurant=restaurant))

#찜 기능 
@application.route('/restaurant/my', methods=['POST', 'GET'])
def my_favorite_list(restaurant):
    id = session['id']
    if DB.my_fav_list(restaurant):
        return redirect(url_for('my-fav-list'))

#내가 쓴 리뷰 
@application.route('/review/my', methods=['POST', 'GET'])
def my_review():
    id = session['id']
    if DB.get_myreviews():
        return redirect(url_for('myreview-list'))


if __name__ == "__main__":
    application.secret_key = 'super secret key'
    application.config['SESSION_TYPE'] = 'filesystem'
    application.run(host='0.0.0.0') 
