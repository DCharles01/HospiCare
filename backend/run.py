from api import create_app
from settings import DB_USER, DB_NAME, DB_PASSWORD, DB_HOST

app = create_app(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)

app.run(host='0.0.0.0', debug=True)