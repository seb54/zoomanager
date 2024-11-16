from app import create_app, db
from app.models.zoo import Zoo

def reset_db():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()
        
        # Créer un zoo par défaut
        zoo_default = Zoo(nom="Mon Zoo")
        db.session.add(zoo_default)
        db.session.commit()
        
        print("Base de données réinitialisée avec succès!")

if __name__ == "__main__":
    reset_db() 