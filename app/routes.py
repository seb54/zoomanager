from flask import Blueprint, render_template, request, flash, redirect, url_for
from app import db
from app.models.animal import Animal
from app.models.cage import Cage

main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    cages = Cage.query.all()
    total_animaux = sum(len(cage.animaux) for cage in cages)
    return render_template('dashboard.html', 
                         cages=cages,
                         total_animaux=total_animaux)

@main.route('/ajouter-cage', methods=['POST'])
def ajouter_cage():
    numero = request.form.get('numero')
    if not numero:
        flash('Le numéro de la cage est requis', 'error')
        return redirect(url_for('main.dashboard'))
        
    nouvelle_cage = Cage(numero=numero)
    db.session.add(nouvelle_cage)
    
    try:
        db.session.commit()
        flash('Cage ajoutée avec succès !', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Erreur lors de l\'ajout de la cage', 'error')
        
    return redirect(url_for('main.dashboard'))

@main.route('/ajouter-animal', methods=['POST'])
def ajouter_animal():
    espece = request.form.get('espece')
    nom = request.form.get('nom')
    cage_id = request.form.get('cage_id')
    
    if not all([espece, nom, cage_id]):
        flash('Tous les champs sont requis', 'error')
        return redirect(url_for('main.dashboard'))
        
    cage = Cage.query.get(cage_id)
    if not cage:
        flash('Cage invalide', 'error')
        return redirect(url_for('main.dashboard'))
        
    nouvel_animal = Animal(
        espece=espece,
        nom=nom,
        cage_id=cage_id
    )
    db.session.add(nouvel_animal)
    
    try:
        db.session.commit()
        flash(f'{nom} a été ajouté avec succès !', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Erreur lors de l\'ajout de l\'animal', 'error')
        
    return redirect(url_for('main.dashboard'))

@main.route('/supprimer-cage/<int:cage_id>', methods=['POST'])
def supprimer_cage(cage_id):
    cage = Cage.query.get_or_404(cage_id)
    nb_animaux = len(cage.animaux)
    db.session.delete(cage)
    db.session.commit()
    if nb_animaux > 0:
        flash(f'Cage et {nb_animaux} animal(aux) supprimés avec succès', 'success')
    else:
        flash('Cage supprimée avec succès', 'success')
    return redirect(url_for('main.dashboard'))

@main.route('/nourrir-animal/<int:animal_id>', methods=['POST'])
def nourrir_animal(animal_id):
    animal = Animal.query.get_or_404(animal_id)
    nourriture = request.form.get('nourriture')
    
    if not nourriture:
        flash('Veuillez sélectionner une nourriture', 'error')
        return redirect(url_for('main.dashboard'))
        
    succes, message = animal.nourrir(nourriture)
    flash(message, 'success' if succes else 'error')
    return redirect(url_for('main.dashboard')) 