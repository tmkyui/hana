from flask import Flask,render_template
app = Flask(__name__, static_folder='.', static_url_path='')
@app.route('/',methods=['GET'])
def hello():
    return render_template('hello.html',title="grape",name="yui")


    






if __name__=="__main__":
    app.run(debug=True,port=8888,threaded=True)
