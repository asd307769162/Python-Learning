from flask import Flask
app = Flask(__name__)


# 硬编码
@app.route('/')
def index():
    return 'This is Index.'

@app.route('/hello')
def hello_world():
    return('Hello World!')
    
@app.route('/user/<username>')# 传参数
def show_user_profile(username):
    return('User %s' %username)
           
@app.route('/post/<int:post_id>')# 传参数
def show_post(post_id):
    return('Post %s' %post_id)
    
@app.route('/projects/') # /projects和/projects/两个页面都能够处理
def projects():
    return('The project page')

@app.route('/about')# 访问/about/会404错误
def about():
    return('The about page')
    
    

    
if __name__ == '__main__':
    app.debug = True
    app.run()