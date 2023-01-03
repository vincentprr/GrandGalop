from .core.app import app
from .core.database import create_tables, db

create_tables(db)
app.run(debug=True)
    