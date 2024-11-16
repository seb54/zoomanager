document.addEventListener('alpine:init', () => {
    Alpine.data('nourrissage', () => ({
        showFeedingModal: false,
        selectedFood: '',
        quantity: 0.1,
        availableFood: [],
        
        async init() {
            // Charger les types de nourriture disponibles
            const response = await fetch('/api/nourritures');
            this.availableFood = await response.json();
        },
        
        async nourrir(animalId) {
            if (!this.selectedFood || this.quantity <= 0) {
                this.showError('Veuillez remplir tous les champs');
                return;
            }
            
            try {
                const response = await fetch(`/nourrir/${animalId}`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        nourriture_id: this.selectedFood,
                        quantite: this.quantity
                    })
                });
                
                const data = await response.json();
                
                if (data.success) {
                    this.showSuccess(data.message);
                    this.showFeedingModal = false;
                    // Mettre à jour l'interface
                    this.$dispatch('animal-fed', { animalId });
                } else {
                    this.showError(data.message);
                }
            } catch (error) {
                this.showError('Une erreur est survenue');
            }
        },
        
        showSuccess(message) {
            const toast = document.createElement('div');
            toast.className = 'fixed bottom-4 right-4 bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg transform transition-transform duration-300 ease-in-out';
            toast.textContent = message;
            document.body.appendChild(toast);
            
            setTimeout(() => {
                toast.style.transform = 'translateY(150%)';
                setTimeout(() => toast.remove(), 300);
            }, 3000);
        },
        
        showError(message) {
            const toast = document.createElement('div');
            toast.className = 'fixed bottom-4 right-4 bg-red-500 text-white px-6 py-3 rounded-lg shadow-lg transform transition-transform duration-300 ease-in-out';
            toast.textContent = message;
            document.body.appendChild(toast);
            
            setTimeout(() => {
                toast.style.transform = 'translateY(150%)';
                setTimeout(() => toast.remove(), 300);
            }, 3000);
        }
    }));
}); 