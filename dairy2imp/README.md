# Dairy Management System - Flask + MySQL

This application provides a simple CRUD for `animals` as an example and serves static files in `static/` and templates in `templates/`.

## Quick start (local MySQL)
1. Install Python 3.8+ and pip.
2. (Optional but recommended) Create a virtualenv:
   ```
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```
3. Install requirements:
   ```
   pip install -r requirements.txt
   ```
4. Create the database and tables:
   - Edit `import_db.sql` if you want to change names.
   - Run:
   ```
   mysql -u root -p < import_db.sql
   ```
   or login to mysql and paste the SQL.
5. Edit `config.py` to set DB credentials or set environment variables `DB_HOST`, `DB_USER`, `DB_PASS`, `DB_NAME`.
6. Run the app:
   ```
   python app.py
   ```
7. Open http://localhost:8000

## Notes
- This is a starter conversion. Replace the templates and static files with your original project's frontend files (HTML/CSS/JS).
- For production, use a proper WSGI server (gunicorn/uwsgi) and connection pooling.
