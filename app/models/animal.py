from app import db
from datetime import datetime

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    espece = db.Column(db.String(100), nullable=False)
    cage_id = db.Column(db.Integer, db.ForeignKey('cage.id'), nullable=False)
    derniere_alimentation = db.Column(db.DateTime)

    @property
    def regime_alimentaire(self):
        REGIMES = {
            'carnivore': [
                'Lion', 'Tigre', 'Panthère', 'Guépard', 'Jaguar', 
                'Loup', 'Lynx', 'Hyène', 'Caracal', 'Aigle', 'Faucon'
            ],
            'herbivore': [
                'Zèbre', 'Girafe', 'Éléphant', 'Antilope', 'Gazelle',
                'Gnou', 'Cerf', 'Élan', 'Bison', 'Lapin', 'Lièvre'
            ],
            'omnivore': [
                'Ours brun', 'Ours polaire', 'Singe', 'Rat', 'Souris',
                'Sanglier', 'Phacochère', 'Capybara'
            ]
        }
        
        for regime, especes in REGIMES.items():
            if self.espece in especes:
                return regime
        return 'inconnu'

    def nourrir(self, nourriture):
        ALIMENTS = {
            'viande': ['carnivore', 'omnivore'],
            'poisson': ['carnivore', 'omnivore'],
            'fruits': ['herbivore', 'omnivore'],
            'légumes': ['herbivore', 'omnivore'],
            'graines': ['herbivore', 'omnivore'],
            'insectes': ['omnivore']
        }
        
        regime = self.regime_alimentaire
        if regime == 'inconnu':
            return False, f"🤔 Le régime alimentaire de {self.espece} est inconnu"
            
        if nourriture not in ALIMENTS:
            return False, f"❌ {nourriture} n'est pas un aliment reconnu"
            
        if regime in ALIMENTS[nourriture]:
            self.derniere_alimentation = datetime.utcnow()
            db.session.commit()
            return True, f"✅ {self.nom} le {self.espece} a mangé {nourriture} avec plaisir !"
        else:
            return False, f"❌ {self.nom} le {self.espece} ne mange pas de {nourriture} ({regime})"

    def __repr__(self):
        return f"<Animal {self.nom} ({self.espece})>" 