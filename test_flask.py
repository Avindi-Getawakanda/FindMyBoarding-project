from flask import Flask,request

app = Flask(__name__)


@app.route("/test",methods=["GET","POST"])
def test():
    if request.method=="GET":
        return "ruveenata pissu"
    else:
        return "error"


if __name__=="__main__":
    app.run(host = "0.0.0.0" ,  port = 5000, debug=True)