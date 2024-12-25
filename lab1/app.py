from flask import Flask, render_template, request, redirect, url_for
from models import setup_database, create_session, Customer

app = Flask(__name__)
engine = setup_database("sqlite:///customer.sqlite")
session = create_session(engine)

@app.route('/')
def index():
    customers = session.query(Customer).all()
    return render_template('index.html', customers=customers)

@app.route('/add', methods=['POST'])
def add_customer():
    new_customer = Customer(
        id=request.form['id'],
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        dob=request.form['dob'],
        city=request.form['city'],
        state=request.form['state'],
        zip=request.form['zip']
    )
    session.add(new_customer)
    session.commit()
    return redirect(url_for('index'))

@app.route('/update', methods=['POST'])
def update_customer():
    customer_id = request.form['id2']
    new_name = request.form['new_name']
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        customer.first_name = new_name
        session.commit()
    return redirect(url_for('index'))

@app.route('/delete', methods=['POST'])
def delete_customer():
    customer_id = request.form['id3']
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if customer:
        session.delete(customer)
        session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)