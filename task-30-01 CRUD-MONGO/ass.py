from flask import Flask,render_template,request,url_for,redirect
from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017")

app=Flask(__name__)




@app.route("/<id>", methods=["POST","GET"])
def show(id):
    client=MongoClient("mongodb://localhost:27017")
    database=client.college
    collect=database.student
    temp=collect.find_one({"id":int(id)})
    print(temp)
    a=[]
    for i in temp:
        a.append(i)
    return render_template("index.html",data=a)

if __name__=="__main__":
    app.run(debug=True)