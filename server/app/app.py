from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
	return render_template('http://35.204.57.81:9090/index.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
	return render_template('index.html', 
		customer_name=request.form['customer_name'], 
		bill_to=request.form['bill_to'],
		email=request.form['email'],
		tel=request.form['tel'],
		city=request.form['city'],
		street_name=request.form['street_name'],
		line2addr=request.form['line2addr'],
		zipcode=request.form['zipcode'],
		fax=request.form['fax'],
		description1=request.form['description'],
		price1=request.form['price'],
		qty1=request.form['qty'],
		amount1=(int(request.form['qty']) * int(request.form['price']))
		)

if __name__ == "__main__":
		app.run(host='0.0.0.0', port=9099)
