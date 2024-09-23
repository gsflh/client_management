from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'client_managmentment_project'

# Initialize database
def init_db():
    with sqlite3.connect('clients.db') as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS clients
                        (id INTEGER PRIMARY KEY,
                        name TEXT,
                        dob TEXT,
                        address TEXT,
                        email TEXT,
                        phone TEXT,
                        service TEXT)''')
init_db()

# Login route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':  # Simple validation logic
            return redirect(url_for('view_clients'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

# Add client route
@app.route('/add_client', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        address = request.form['address']
        email = request.form['email']
        phone = request.form['phone']
        service = request.form['service']
        with sqlite3.connect('clients.db') as conn:
            conn.execute('INSERT INTO clients (name, dob, address, email, phone, service) VALUES (?, ?, ?, ?, ?, ?)',
                         (name, dob, address, email, phone, service))
        flash('Client added successfully!')
        return redirect(url_for('view_clients'))
    return render_template('add_client.html')

# View clients route
@app.route('/view_clients')
def view_clients():
    conn = sqlite3.connect('clients.db')
    clients = conn.execute('SELECT * FROM clients').fetchall()
    conn.close()
    return render_template('view_clients.html', clients=clients)

# Update client route
@app.route('/update_client/<int:id>', methods=['GET', 'POST'])
def update_client(id):
    conn = sqlite3.connect('clients.db')
    client = conn.execute('SELECT * FROM clients WHERE id = ?', (id,)).fetchone()
    conn.close()

    if request.method == 'POST':
        name = request.form['name']
        dob = request.form['dob']
        address = request.form['address']
        email = request.form['email']
        phone = request.form['phone']
        service = request.form['service']
        with sqlite3.connect('clients.db') as conn:
            conn.execute('UPDATE clients SET name = ?, dob = ?, address = ?, email = ?, phone = ?, service = ? WHERE id = ?',
                         (name, dob, address, email, phone, service, id))
        flash('Client updated successfully!')
        return redirect(url_for('view_clients'))

    return render_template('update_client.html', client=client)

# Delete client route
@app.route('/delete_client/<int:id>')
def delete_client(id):
    with sqlite3.connect('clients.db') as conn:
        conn.execute('DELETE FROM clients WHERE id = ?', (id,))
    flash('Client deleted successfully!')
    return redirect(url_for('view_clients'))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=80)


