from flask import Flask,render_template, request
import requests 
app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':
        url="http://ravigitte.pythonanywhere.com/solve"
        exp=str(request.form['eq'])
        PARAMS = {'exp':exp}
        r = requests.get(url = url, params = PARAMS)
        data = r.json()
        lis=[] 
        for i in data:
            u=[]
            for k in i:
                u.append(i[k])
            lis.append(u)
        r=1
        #return str(data)
        return render_template("index.html",r=r,lis=lis)

if __name__ == '__main__':
   app.run(debug=True)