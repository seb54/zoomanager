from app import db
from datetime import datetime

class Nourriture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    regime_compatible = db.Column(db.String(50), nullable=False)  # carnivore, herbivore, omnivore
    quantite_stock = db.Column(db.Float, default=0)
    unite = db.Column(db.String(20), default='kg')

class Repas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)
    nourriture_id = db.Column(db.Integer, db.ForeignKey('nourriture.id'), nullable=False)
    quantite = db.Column(db.Float, nullable=False)
    date_repas = db.Column(db.DateTime, default=datetime.utcnow)
    succes = db.Column(db.Boolean, default=True) 