# Exo : ./venv/bin/python3 main.py agario Ex1.py

from datetime import datetime

# Définition des dates
date_debut = datetime.strptime('29/05/2023', '%d/%m/%Y')
date_fin = datetime.strptime('08/09/2023', '%d/%m/%Y')
date_actuelle = datetime.today()

# Calcul du nombre de jours écoulés depuis le 29/05/2023
jours_passes = (date_actuelle - date_debut).days

# Calcul du nombre de jours restants jusqu'au 08/09/2023
jours_restants = (date_fin - date_actuelle).days

# Affichage des résultats
print("Nombre de jours passés depuis le 29/05/2023 : ", jours_passes)
print("Nombre de jours restants jusqu'au 08/09/2023 : ", jours_restants)
