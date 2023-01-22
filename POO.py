class ReservationCreneau:
   ## date = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
    def __init__(self, id_personne, date, heures, occupe=False):
        self.id_personne = id_personne
        self.date = date
        self.heures = heures
        self.occupe = occupe

    def reserver(self):
        if self.occupe:
            print("Le créneau est déjà réservé à cette date et à ces heures.")
        else:
            self.occupe = True
            print(f"Le créneau a été réservé par {self.id_personne} à cette date et à ces heures.")

    def annuler(self):
        if self.occupe:
            self.occupe = False
            print("La réservation a été annulée.")
        else:
            print("Il n'y a pas de réservation à cette date et à ces heures.")

    def disponibilite(self):
        if self.occupe:
            print("Le créneau n'est pas disponible à cette date et à ces heures.")
        else:
            print("Le créneau est disponible à cette date et à ces heures.")
            
    def disponibilite_globale(self, liste_reservations):
        disponibles = []
        for reservation in liste_reservations:
            if not reservation.occupe:
                disponibles.append((reservation.date, reservation.heures))
        if len(disponibles)==0:
            print("Il n'y a pas de créneaux disponibles.")
        else:
            print("Les créneaux disponibles sont :")
            for dispo in disponibles:
                print(f'Date: {dispo[0]} Heures: {dispo[1]}')

    if __name__ == "__main__":
            # Création de réservations
    reservation1 = ReservationCreneau("12345", "2022-01-01", 9)
    reservation2 = ReservationCreneau("67890", "2022-01-01", 10)
    reservation3 = ReservationCreneau("24680", "2022-01-02", 9)

    # Liste de toutes les réservations
    liste_reservations = [reservation1, reservation2, reservation3]

    # Vérification de la disponibilité d'un créneau spécifique
    reservation1.disponibilite()  # Affiche "Le créneau est disponible à cette date et à ces heures."

    # Réservation d'un créneau
    reservation1.reserver()

    # Vérification de la disponibilité d'un créneau spécifique après réservation
    reservation1.disponibilite()  # Affiche "Le créneau n'est pas disponible à cette date et à ces heures."

    # Annulation d'une réservation
    reservation1.annuler()

    # Vérification de la disponibilité d'un créneau spécifique après annulation
    reservation1.disponibilite()  # Affiche "Le créneau est disponible à cette date et à ces heures."
