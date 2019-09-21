from flask import Flask, request, render_template, session

from service.user_service import UserService

app = Flask(__name__)

# 设置app密钥
app.config['SECRET_KEY'] = '123123123'

# 修改渲染脚本模板
app.jinja_env.variable_start_string = '[['
app.jinja_env.variable_end_string = ']]'

@app.route("/", methods= ['GET'])
def index():
    user_info = UserService.get_user_info_by_id(1)
    session[user_info['username']] = user_info
    return render_template('index.html', user_info=user_info)

@app.route("/login", methods= ['GET'])
def login():
    return render_template('login.html')

@app.route("/welcome", methods= ['GET'])
def welcome():
    return render_template('welcome.html')

@app.route("/welcome1", methods= ['GET'])
def welcome1():
    return render_template('welcome1.html')

@app.route("/member-list/<string:username>", methods= ['GET', 'POST'])
def member_list(username):
    user_info = session.get(username)
    user_list = UserService.get_user_list(user_info)
    return render_template('member-list.html', user_list=user_list, user_info=user_info)

@app.route("/member-add", methods= ['GET'])
def member_add():
    return render_template('member-add.html')

@app.route("/member-edit", methods= ['GET'])
def member_edit():
    return render_template('member-edit.html')

@app.route("/member-password/<string:username>", methods= ['GET'])
def member_password(username):
    user_info = session.get(username)
    return render_template('member-password.html', user_info=user_info, update=True)

@app.route("/member-reset-password/<int:id>", methods= ['GET'])
def member_reset_password(id):
    user_info =UserService.get_user_info_by_id(id)
    return render_template('member-password.html', user_info=user_info)

@app.route("/member-update-status/<int:id>", methods= ['GET', 'POST'])
def update_user_status(id):
    UserService.update_stat_by_id(id)
    return "success"

@app.route("/member-list1", methods= ['GET'])
def member_list1():
    return render_template('member-list1.html')

@app.route("/member-del", methods= ['GET'])
def member_del():
    return render_template('member-del.html')

@app.route("/order-list", methods= ['GET'])
def order_list():
    return render_template('order-list.html')

@app.route("/order-list1", methods= ['GET'])
def order_list1():
    return render_template('order-list1.html')

@app.route("/cate", methods= ['GET'])
def cate():
    return render_template('cate.html')

@app.route("/city", methods= ['GET'])
def city():
    return render_template('city.html')

@app.route("/admin-list", methods= ['GET'])
def admin_list():
    return render_template('admin-list.html')

@app.route("/admin-role", methods= ['GET'])
def admin_role():
    return render_template('admin-role.html')

@app.route("/admin-cate", methods= ['GET'])
def admin_cate():
    return render_template('admin-cate.html')

@app.route("/admin-rule", methods= ['GET'])
def admin_rule():
    return render_template('admin-rule.html')

@app.route("/echarts1", methods= ['GET'])
def echarts1():
    return render_template('echarts1.html')

@app.route("/echarts2", methods= ['GET'])
def echarts2():
    return render_template('echarts2.html')

@app.route("/echarts3", methods= ['GET'])
def echarts3():
    return render_template('echarts3.html')

@app.route("/echarts4", methods= ['GET'])
def echarts4():
    return render_template('echarts4.html')

@app.route("/echarts5", methods= ['GET'])
def echarts5():
    return render_template('echarts5.html')

@app.route("/echarts6", methods= ['GET'])
def echarts6():
    return render_template('echarts6.html')

@app.route("/echarts7", methods= ['GET'])
def echarts7():
    return render_template('echarts7.html')

@app.route("/echarts8", methods= ['GET'])
def echarts8():
    return render_template('echarts8.html')

@app.route("/unicode", methods= ['GET'])
def unicode():
    return render_template('unicode.html')

@app.route("/error", methods= ['GET'])
def error():
    return render_template('error.html')

@app.route("/demo", methods= ['GET'])
def demo():
    return render_template('demo.html')

@app.route("/log", methods= ['GET'])
def log():
    return render_template('log.html')

if __name__ == '__main__':
    app.run(debug=True)