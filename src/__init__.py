from core.app import app
from core.database import create_tables, db

if __name__ == "__main__":
    create_tables(db)
    app.run(debug=True)