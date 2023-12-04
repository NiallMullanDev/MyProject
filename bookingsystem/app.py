from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data - replace with your own data storage mechanism (database, file, etc.)
bookings = []

@app.route('/')
def index():
    return render_template('index.html', bookings=bookings)

@app.route('/book', methods=['POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        date = request.form['date']
        # Add the booking to the data storage
        bookings.append({'name': name, 'date': date})
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
