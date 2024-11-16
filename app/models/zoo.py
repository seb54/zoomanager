from app import db

class Zoo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    cages = db.relationship('Cage', backref='zoo', lazy=True)
    
    def nombre_cages(self):
        return len(self.cages)
    
    def nombre_animaux(self):
        return sum(len(cage.animaux) for cage in self.cages) 