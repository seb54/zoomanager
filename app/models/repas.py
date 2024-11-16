from app import db
from datetime import datetime

class Repas(db.Model):
    __table_args__ = {'extend_existing': True}
    
    id = db.Column(db.Integer, primary_key=True)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)
    nourriture_id = db.Column(db.Integer, db.ForeignKey('nourriture.id'), nullable=False)
    quantite = db.Column(db.Float, nullable=False)
    date_repas = db.Column(db.DateTime, default=datetime.utcnow)
    succes = db.Column(db.Boolean, default=True)

    animal = db.relationship('Animal', backref='repas')
    nourriture = db.relationship('Nourriture', backref='repas') 