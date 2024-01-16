from flask import Flask, request, jsonify
import psycopg2
import api.models as models
from db.db_utils import build_from_record, build_from_records
from flasgger import Swagger

# don't call sql from controller
# use a model level method
# instead of cursor.execute("select * from patients"), do Patients.all()
def create_app(dbname: str, user: str, password: str, host):
    # setup flask app
    app = Flask(__name__)

    # create API documentation from app
    Swagger(app)

    app.config.from_mapping(
        DB_USER=user,
        DB_PASSWORD=password,
        DB_NAME = dbname,
        DB_HOST = host
    )
    # breakpoint()
    # create connection
    conn = psycopg2.connect(user=app.config['DB_USER'],
                            password=app.config['DB_PASSWORD'],
                            dbname=app.config['DB_NAME'],
                            host=app.config['DB_HOST'])
    
    cursor = conn.cursor()

    @app.route('/patients')
    def patients():
        """
        Returns patients
        ---
        responses:
            200:
                description: Patients returned


        """
        records = models.Patient.find_all(conn)
        return jsonify({'patients': [patient.__dict__ for patient in build_from_records(models.Patient, records)]})

    @app.route('/patients/<id>')
    def patient_id(id):
        """
        Returns patients by id
        ---
        parameters:
            - name: id
              in: path
              type: string
              description: The id of the patient.
        responses:
            200:
                description: Patients returned
        """
        record = models.Patient.find_by_id(id, conn)
        return build_from_record(models.Patient, record).__dict__
    
    @app.route('/patients/search')
    def patient_name():
        """
        Search for patients based on specified criteria.
        ---
        parameters:
            - name: name
              in: query
              type: string
              description: The name of the patient
            - name: gender
              in: query
              type: string
              description: The gender of the patient
            - name: race
              in: query
              type: string
              description: The race of the patient
        responses:
            200:
                description: Search successful!
        """
        # name = request.args.get('name')

        # cursor.execute(f'select * from {models.Patient.__table__} where name = %s', (name,))
        # record = cursor.fetchone()
        # return build_from_record(models.Patient, record).__dict__

        name = request.args.get('name')
        gender = request.args.get('gender')
        race = request.args.get('race')
        

        # Build the query based on the provided parameters
        query = "SELECT * FROM patients WHERE 1=1"
        conditions = []

        if name:
            conditions.append(f"name = '{name}'")
        if gender:
            conditions.append(f"gender = '{gender}'")
        if race:
            conditions.append(f"race = '{race}'")
    

        # Combine conditions into the final query
        if conditions:
            query += " AND " + " AND ".join(conditions)

        # Execute the query
        cursor.execute(query)
        records = cursor.fetchall()

        # Build response from records
        patients = [build_from_record(models.Patient, record).__dict__ for record in records]

        return patients
    return app
    

    
