import os
from flask import Flask, render_template, request, redirect, url_for
import databasenijisketch  # Your database interaction module

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/submit_reservation', methods=['POST'])
def submit_reservation():
    if request.method == 'POST':
        guest_name = request.form['guest_name']
        guest_phone = request.form['guest_phone']
        guest_email = request.form['guest_email']
        reservation_date = request.form['reservation_date']
        reservation_time = request.form['reservation_time']
        num_guests = request.form['num_guests']
        special_requests = request.form['special_requests']

        reservation_datetime = f"{reservation_date} {reservation_time}"
        databasenijisketch.insert_reservation(guest_name, guest_phone, guest_email, reservation_datetime, num_guests, special_requests)

        return redirect(url_for('booking'))

# if __name__ == '__main__':
#     app.run(debug=True, port=5003)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Default to 5003 if PORT environment variable is not set
    app.run(host='0.0.0.0', port=port, debug=False)
