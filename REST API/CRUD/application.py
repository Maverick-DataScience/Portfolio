from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your-database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Drink(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    desc = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.desc}"

@app.route('/')
def index():
    return 'Hello'

@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    output =[]
    
    for drink in drinks:
        drink_data ={'name' : drink.name, 'description': drink.desc}
        output.append(drink_data)
        
    return {"drinks":output}

@app.route('/drinks/<id>')
def get_drink(id):
    drink = Drink.query.get_or_404(id)
    
    return {"name":drink.name, "description":drink.desc}

@app.route('/drinks', methods=['POST'])
def add_drink():
    drink=Drink(name=request.json['name'],
                desc=request.json['description'])
    db.session.add(drink)
    db.session.commit()
    return {'id':drink.id}


@app.route('/drinks/<id>', methods=['DELETE'])
def delete_drink(id):
    drink=Drink.query.get(id)
    if drink is None:
        return{"error not found 404"}
    
    db.session.delete(drink)
    db.session.commit()
    
    return {'message':'gone'}
    
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)