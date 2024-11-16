from app import db

class Cage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(50), nullable=False)
    animaux = db.relationship('Animal', backref='cage', lazy=True, cascade='all, delete-orphan')

    @staticmethod
    def verifier_predation(animal1, animal2):
        RELATIONS_PREDATEUR_PROIE = {
            # Grands félins
            'Lion': [
                'Zèbre', 'Gazelle', 'Antilope', 'Gnou', 'Phacochère', 
                'Autruche', 'Impala', 'Buffle', 'Girafe (jeune)'
            ],
            'Tigre': [
                'Cerf', 'Sanglier', 'Antilope', 'Gazelle', 'Singe', 
                'Phacochère', 'Buffle', 'Zèbre'
            ],
            'Panthère': [
                'Gazelle', 'Antilope', 'Singe', 'Impala', 
                'Phacochère', 'Cerf'
            ],
            'Guépard': [
                'Gazelle', 'Antilope', 'Impala', 'Zèbre (jeune)',
                'Autruche', 'Lièvre'
            ],
            'Jaguar': [
                'Tapir', 'Capybara', 'Pécari', 'Singe', 
                'Tatou', 'Cerf'
            ],

            # Autres carnivores
            'Loup': [
                'Cerf', 'Élan', 'Lièvre', 'Bison (jeune)',
                'Mouflon', 'Chèvre', 'Mouton'
            ],
            'Ours brun': [
                'Cerf', 'Élan', 'Saumon', 'Mouton',
                'Chèvre', 'Lièvre'
            ],
            'Ours polaire': [
                'Phoque', 'Morse (jeune)', 'Poisson',
                'Pingouin', 'Renne'
            ],

            # Reptiles
            'Crocodile': [
                'Zèbre', 'Gazelle', 'Antilope', 'Gnou',
                'Buffle (jeune)', 'Phacochère'
            ],
            'Python': [
                'Souris', 'Rat', 'Lapin', 'Oiseau',
                'Singe (petit)', 'Lièvre'
            ],
            'Anaconda': [
                'Capybara', 'Tapir', 'Pécari', 'Singe',
                'Tatou', 'Oiseau'
            ],

            # Oiseaux de proie
            'Aigle': [
                'Lapin', 'Lièvre', 'Souris', 'Rat',
                'Oiseau', 'Serpent'
            ],
            'Faucon': [
                'Souris', 'Rat', 'Oiseau', 'Lézard',
                'Serpent (petit)'
            ],

            # Petits carnivores
            'Lynx': [
                'Lièvre', 'Lapin', 'Souris', 'Rat',
                'Oiseau', 'Écureuil'
            ],
            'Hyène': [
                'Gazelle', 'Antilope', 'Zèbre (jeune)',
                'Gnou (jeune)', 'Phacochère'
            ],
            'Caracal': [
                'Lièvre', 'Oiseau', 'Gazelle (jeune)',
                'Antilope (jeune)'
            ]
        }

        # Vérifier si animal1 est prédateur de animal2
        if animal1.espece in RELATIONS_PREDATEUR_PROIE:
            for proie in RELATIONS_PREDATEUR_PROIE[animal1.espece]:
                # Vérifie la correspondance exacte ou avec "(jeune)"
                if animal2.espece == proie or animal2.espece == proie.replace(" (jeune)", ""):
                    return animal1, animal2
        
        # Vérifier si animal2 est prédateur de animal1
        if animal2.espece in RELATIONS_PREDATEUR_PROIE:
            for proie in RELATIONS_PREDATEUR_PROIE[animal2.espece]:
                if animal1.espece == proie or animal1.espece == proie.replace(" (jeune)", ""):
                    return animal2, animal1
        
        return None, None