from flask import Flask, render_template, request
from var import INV

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
	return render_template('http://35.204.57.81:9090/index.html')

@app.route('/invoice_pdf', methods=['GET', 'POST'])
def invoice_pdf():

	customer_name = request.form['customer_name'] 
	bill_to = request.form['bill_to']
	email = request.form['email']
	tel = request.form['tel']
	line1addr = request.form['line1addr']
	street_name = request.form['street_name']
	line2addr = request.form['line2addr']
	zipcode = request.form['zipcode']
	fax = request.form['fax']
	description = request.form['description']
	price = int(request.form['price'])
	qty = int(request.form['qty'])
	amount = qty * price
	sub_tot = amount
	tax = (sub_tot) * 0.15
	total = sub_tot + tax
	balance = total

	ls = request.form
	count_items = 0
	amtdict = {}
	for itm in ls:
		if "price" in str(itm) and "price" != str(itm):
			count_items += 1
			amtdict["amt" + str(count_items)] = [
				float(request.form["price" + str(count_items)]) * 
				float(request.form["qty" + str(count_items)]), 
				str(request.form["description" + str(count_items)]), 
				float(request.form["price" + str(count_items)]),
				int(request.form["qty" + str(count_items)])]
			sub_tot = sub_tot + amtdict["amt" + str(count_items)][0]

	tax = sub_tot * 0.15
	total = sub_tot + tax
	balance = total
	invoiceno = 1000
	print("\n------")
	return render_template('index.html', customer_name=customer_name,
	 bill_to=bill_to, email=email, tel=tel, line1addr=line1addr, street_name=street_name, 
	 line2addr=line2addr, zipcode=zipcode, fax=fax, description=description, 
	 price=price, qty=qty, amount=amount, sub_tot=sub_tot, tax=tax,
	 total=total, balance=balance,amtdict=amtdict, invoiceno=invoiceno)

if __name__ == "__main__":
		app.run(host='0.0.0.0', port=9099)
