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

class Ninja:
    def __init__(self,name,atk,def_,hp):
        self.name = name
        self.atk = atk
        self.def_ = def_
        self.hp = hp

    def print(self):
        print("{0}, {1}, {2}, {3}".format(self.name,self.atk,self.def_,self.hp))

    def attack(self,other):
        print("thang {0} danh thang {1}".format(self.name,other.name))
        if self.atk > other.def_:
            matmau = int(self.atk - other.def_)
            other.hp =- matmau
            print(self.name + ' danh ' + other.name +' mat ' + str(matmau) + ' mau')
        if other.def_ > self.atk:
            matmau = int(abs(self.atk - other.def_))
            self.hp =- matmau
            print(self.name + ' mat '+str(matmau) +' mau boi vi giap '+other.name +' qua to')

ninja1 = Ninja("naruto",30,6,10)
ninja2 = Ninja(name="sasuke",atk=5,hp=10,def_=6)
ninja1.attack(ninja2)
ninja2.attack(ninja1)
if __name__ == '__main__':

    app.run()
