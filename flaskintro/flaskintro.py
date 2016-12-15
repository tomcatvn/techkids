from flask import Flask,render_template,url_for

app = Flask(__name__)


@app.route('/nostarch')
def nostarch():
    return render_template("nostarch.html")

@app.route('/intro')
def intro():
    return render_template('intro.html')

@app.route('/fordemo')
def fordemo():
    return render_template('for.html',names=["phuc","Trang","minh","thanh"])


food_list = [
        {
            "name":"bundau" ,
            "desc":"15k"   ,
            "img" :'http://7monngonmoingay.com/wp-content/uploads/2014/11/cach-lam-bun-dau-mam-tom-ha-noi-ngon-tuyet-cu-meo-9.jpg'
        }                 ,
    {
        "name":"cut cho",
        "desc":"30k",
        "img":'http://kinhdoanhnhahang.vn/wp-content/uploads/2014/12/lap-ke-hoach-kinh-doanh-quan-bun-dau-mam-tom.jpg'
    }                   ,
        {
            "name":        "thanh",
            "desc":"60k"              ,
            "img":'http://2monngonmoingay.net/wp-content/uploads/2015/01/cach-lam-bun-dau-mam-tom.jpg'

         }
    ]

@app.route('/food_blog')
def food_blog():
    return render_template('food_blog.html',foodlist=food_list)
if __name__ == '__main__':

    app.run()
