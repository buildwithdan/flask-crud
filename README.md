# MandalorianBounty

A started Python CRUD app, using Flask, Bootstrap, SQLite

Structure of app   
my_flask_app/   
│   
├── api/   
│ ├── **init**.py #not being used   
│ ├── config.py   
│ ├── models.py   
│ ├── views.py   
│ ├── templates/   
│ │ ├── base.html   
│ │ ├── index.html   
│ │ ├── edit_row.html   
│ ├── static/   
│ │ ├── css/   
│ │ │ ├── main.css   
│   
├── config.ini   
├── requirements.txt   
├── run.py   

Updates

- need to fix the delete button
- need to add a create button for new contracts

To deploy on vercel

- need to delete venv and rebuild as psycopg is causing issues.
