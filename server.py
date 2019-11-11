from flask import Flask, render_template, request
app = Flask(__name__)
# app.secret_key = '4\Hf!ek32!;4fdDsAAAD2,.342'

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
	print(request.form)
	import datetime
	logger = datetime.datetime.now()
	strawberryFrom = int(request.form ["strawberry"])
	raspberryFrom = int(request.form ["raspberry"])
	appleFrom = int(request.form ["apple"])
	blackberryFrom = int(request.form ["blackberry"])
	firstNameFrom = (request.form ["first"])
	lastNameFrom = (request.form ["last"])
	stuIDFrom = (request.form) ["stuID"] 

	return render_template("checkout.html", strawberryCnt = strawberryFrom, raspberryCnt = raspberryFrom, appleCnt = appleFrom, blackberryCnt = blackberryFrom, first = firstNameFrom, last = lastNameFrom, stuID = stuIDFrom, loggerCur = logger )


@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    