from flask import Flask,request,render_template


app=Flask(__name__)


@app.route('/')
def welcome():
    return "Welcome to Flask"
@app.route('/cal',methods=["GET"])
def math_operator():
    operation=request.json["operation"]
    num1=request.json["num1"]
    num2=request.json["num2"]

    if operation == "add":
        result = int(num1)+int(num2) 
    elif operation == "mul":
        result = int(num1)*int(num2) 
    elif operation == "div":
          result = int(num1)/int(num2)  
    else :          
           result = int(num1)-int(num2)
    return  "the operation is {} and the result is {}".format(operation,result)

print(__name__)

if __name__ == '__main__':
    app.run()

