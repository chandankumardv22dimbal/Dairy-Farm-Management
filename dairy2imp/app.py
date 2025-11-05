from flask import Flask, render_template, request, redirect, url_for, flash
from config import get_db
import mysql.connector

app = Flask(__name__)
app.secret_key = 'replace-this-with-a-secure-random-key'

# -------------------
# HOME
# -------------------
@app.route('/')
def home():
    return redirect(url_for('animals'))

# -------------------
# ANIMALS
# -------------------
@app.route('/animals')
def animals():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM animals ORDER BY id DESC")
    animals = cursor.fetchall()
    cursor.close()
    return render_template('animals.html', animals=animals)

@app.route('/animals/add', methods=['POST'])
def add_animal():
    name = request.form.get('name')
    species = request.form.get('species')
    breed = request.form.get('breed')
    age = request.form.get('age') or None
    gender = request.form.get('gender')

    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO animals (name, species, breed, age, gender) VALUES (%s, %s, %s, %s, %s)",
        (name, species, breed, age, gender)
    )
    db.commit()
    cursor.close()
    flash('Animal added successfully.')
    return redirect(url_for('animals'))

@app.route('/animals/delete/<int:id>')
def delete_animal(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM animals WHERE id = %s", (id,))
    db.commit()
    cursor.close()
    flash('Animal deleted.')
    return redirect(url_for('animals'))

@app.route('/animals/edit/<int:id>', methods=['GET', 'POST'])
def edit_animal(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        name = request.form.get('name')
        species = request.form.get('species')
        breed = request.form.get('breed')
        age = request.form.get('age')
        gender = request.form.get('gender')
        cursor.execute(
            "UPDATE animals SET name=%s, species=%s, breed=%s, age=%s, gender=%s WHERE id=%s",
            (name, species, breed, age, gender, id)
        )
        db.commit()
        cursor.close()
        flash('Animal updated.')
        return redirect(url_for('animals'))
    cursor.execute("SELECT * FROM animals WHERE id=%s", (id,))
    animal = cursor.fetchone()
    cursor.close()
    return render_template('edit_animal.html', animal=animal)

# -------------------
# MILK PRODUCTION
# -------------------
@app.route('/milk')
def milk():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT m.*, a.name AS animal_name 
        FROM milk_production m
        JOIN animals a ON m.animal_id = a.id
        ORDER BY m.date DESC
    """)
    milk = cursor.fetchall()
    cursor.close()
    return render_template('milk.html', milk=milk)

@app.route('/milk/add', methods=['POST'])
def add_milk():
    animal_id = request.form.get('animal_id')
    date = request.form.get('date')
    quantity = request.form.get('quantity_liters')
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO milk_production (animal_id, date, quantity_liters) VALUES (%s, %s, %s)",
        (animal_id, date, quantity)
    )
    db.commit()
    cursor.close()
    flash('Milk record added.')
    return redirect(url_for('milk'))

@app.route('/milk/delete/<int:id>')
def delete_milk(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM milk_production WHERE id=%s", (id,))
    db.commit()
    cursor.close()
    flash('Milk record deleted.')
    return redirect(url_for('milk'))

@app.route('/milk/edit/<int:id>', methods=['GET', 'POST'])
def edit_milk(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        animal_id = request.form.get('animal_id')
        date = request.form.get('date')
        quantity = request.form.get('quantity_liters')
        cursor.execute(
            "UPDATE milk_production SET animal_id=%s, date=%s, quantity_liters=%s WHERE id=%s",
            (animal_id, date, quantity, id)
        )
        db.commit()
        cursor.close()
        flash('Milk record updated.')
        return redirect(url_for('milk'))
    cursor.execute("SELECT * FROM milk_production WHERE id=%s", (id,))
    milk = cursor.fetchone()
    cursor.close()
    return render_template('edit_milk.html', milk=milk)

# -------------------
# FEED RECORDS
# -------------------
@app.route('/feed')
def feed():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT f.*, a.name AS animal_name 
        FROM feed_records f
        JOIN animals a ON f.animal_id = a.id
        ORDER BY f.date DESC
    """)
    feed = cursor.fetchall()
    cursor.close()
    return render_template('feed.html', feed=feed)

@app.route('/feed/add', methods=['POST'])
def add_feed():
    animal_id = request.form.get('animal_id')
    feed_type = request.form.get('feed_type')
    quantity_kg = request.form.get('quantity_kg')
    date = request.form.get('date')
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO feed_records (animal_id, feed_type, quantity_kg, date) VALUES (%s, %s, %s, %s)",
        (animal_id, feed_type, quantity_kg, date)
    )
    db.commit()
    cursor.close()
    flash('Feed record added.')
    return redirect(url_for('feed'))

@app.route('/feed/delete/<int:id>')
def delete_feed(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM feed_records WHERE id=%s", (id,))
    db.commit()
    cursor.close()
    flash('Feed record deleted.')
    return redirect(url_for('feed'))

@app.route('/feed/edit/<int:id>', methods=['GET', 'POST'])
def edit_feed(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        animal_id = request.form.get('animal_id')
        feed_type = request.form.get('feed_type')
        quantity_kg = request.form.get('quantity_kg')
        date = request.form.get('date')
        cursor.execute(
            "UPDATE feed_records SET animal_id=%s, feed_type=%s, quantity_kg=%s, date=%s WHERE id=%s",
            (animal_id, feed_type, quantity_kg, date, id)
        )
        db.commit()
        cursor.close()
        flash('Feed record updated.')
        return redirect(url_for('feed'))
    cursor.execute("SELECT * FROM feed_records WHERE id=%s", (id,))
    feed = cursor.fetchone()
    cursor.close()
    return render_template('edit_feed.html', feed=feed)

# -------------------
# HEALTH RECORDS
# -------------------
@app.route('/health')
def health():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT h.*, a.name AS animal_name 
        FROM health_records h
        JOIN animals a ON h.animal_id = a.id
        ORDER BY h.date DESC
    """)
    health = cursor.fetchall()
    cursor.close()
    return render_template('health.html', health=health)

@app.route('/health/add', methods=['POST'])
def add_health():
    animal_id = request.form.get('animal_id')
    date = request.form.get('date')
    issue = request.form.get('issue')
    treatment = request.form.get('treatment')
    vet_name = request.form.get('vet_name')
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO health_records (animal_id, date, issue, treatment, vet_name) VALUES (%s, %s, %s, %s, %s)",
        (animal_id, date, issue, treatment, vet_name)
    )
    db.commit()
    cursor.close()
    flash('Health record added.')
    return redirect(url_for('health'))

@app.route('/health/delete/<int:id>')
def delete_health(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM health_records WHERE id=%s", (id,))
    db.commit()
    cursor.close()
    flash('Health record deleted.')
    return redirect(url_for('health'))

@app.route('/health/edit/<int:id>', methods=['GET', 'POST'])
def edit_health(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        animal_id = request.form.get('animal_id')
        date = request.form.get('date')
        issue = request.form.get('issue')
        treatment = request.form.get('treatment')
        vet_name = request.form.get('vet_name')
        cursor.execute(
            "UPDATE health_records SET animal_id=%s, date=%s, issue=%s, treatment=%s, vet_name=%s WHERE id=%s",
            (animal_id, date, issue, treatment, vet_name, id)
        )
        db.commit()
        cursor.close()
        flash('Health record updated.')
        return redirect(url_for('health'))
    cursor.execute("SELECT * FROM health_records WHERE id=%s", (id,))
    health = cursor.fetchone()
    cursor.close()
    return render_template('edit_health.html', health=health)

# -------------------
# EMPLOYEES
# -------------------
@app.route('/employees')
def employees():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees ORDER BY id DESC")
    employees = cursor.fetchall()
    cursor.close()
    return render_template('employees.html', employees=employees)

@app.route('/employees/add', methods=['POST'])
def add_employee():
    name = request.form.get('name')
    role = request.form.get('role')
    contact = request.form.get('contact')
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO employees (name, role, contact) VALUES (%s, %s, %s)",
        (name, role, contact)
    )
    db.commit()
    cursor.close()
    flash('Employee added.')
    return redirect(url_for('employees'))

@app.route('/employees/delete/<int:id>')
def delete_employee(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM employees WHERE id=%s", (id,))
    db.commit()
    cursor.close()
    flash('Employee deleted.')
    return redirect(url_for('employees'))

@app.route('/employees/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        name = request.form.get('name')
        role = request.form.get('role')
        contact = request.form.get('contact')
        cursor.execute(
            "UPDATE employees SET name=%s, role=%s, contact=%s WHERE id=%s",
            (name, role, contact, id)
        )
        db.commit()
        cursor.close()
        flash('Employee updated.')
        return redirect(url_for('employees'))
    cursor.execute("SELECT * FROM employees WHERE id=%s", (id,))
    employee = cursor.fetchone()
    cursor.close()
    return render_template('edit_employee.html', employee=employee)

# -------------------
# ASSIGNMENTS
# -------------------
@app.route('/assignments')
def assignments():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT asn.*, e.name AS employee_name, a.name AS animal_name
        FROM assignments asn
        JOIN employees e ON asn.employee_id = e.id
        JOIN animals a ON asn.animal_id = a.id
        ORDER BY asn.date DESC
    """)
    assignments = cursor.fetchall()
    cursor.close()
    return render_template('assignments.html', assignments=assignments)

@app.route('/assignments/add', methods=['POST'])
def add_assignment():
    employee_id = request.form.get('employee_id')
    animal_id = request.form.get('animal_id')
    task = request.form.get('task')
    date = request.form.get('date')
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO assignments (employee_id, animal_id, task, date) VALUES (%s, %s, %s, %s)",
        (employee_id, animal_id, task, date)
    )
    db.commit()
    cursor.close()
    flash('Assignment added.')
    return redirect(url_for('assignments'))

@app.route('/assignments/delete/<int:id>')
def delete_assignment(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM assignments WHERE id=%s", (id,))
    db.commit()
    cursor.close()
    flash('Assignment deleted.')
    return redirect(url_for('assignments'))

@app.route('/assignments/edit/<int:id>', methods=['GET', 'POST'])
def edit_assignment(id):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    if request.method == 'POST':
        employee_id = request.form.get('employee_id')
        animal_id = request.form.get('animal_id')
        task = request.form.get('task')
        date = request.form.get('date')
        cursor.execute(
            "UPDATE assignments SET employee_id=%s, animal_id=%s, task=%s, date=%s WHERE id=%s",
            (employee_id, animal_id, task, date, id)
        )
        db.commit()
        cursor.close()
        flash('Assignment updated.')
        return redirect(url_for('assignments'))
    cursor.execute("SELECT * FROM assignments WHERE id=%s", (id,))
    assignment = cursor.fetchone()
    cursor.close()
    return render_template('edit_assignment.html', assignment=assignment)

# -------------------
# MAIN
# -------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
