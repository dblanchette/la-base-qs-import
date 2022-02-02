# la-base-qs-import
Outil pour extraire des données de La Base


# Requis

- Python 3
- Package `requests`

# Authentification

- Accéder à https://labase.quebecsolidaire.net/
- Ouvrez le mode développeur (F12), puis l'onglet réseau (network)
- Naviguer vers [la page des contacts](https://labase.quebecsolidaire.net/contacts) en gardant le mode développeur ouvert
- Une fois la page chargée, dans l'onglet réseau du mode développeur, vous devriez trouver une requête débutant par `GET https://labase.quebecsolidaire.net/api/v2/instances/00/contacts` (où `00` est votre numéro d'instance)
- Appuyez pour voir les détails de le requête et naviguez vers la section "En-têtes de la requête" (Request Headers)
- Identifiz l'en-tête (header) `Authorization`. Il devrait débuter par `Bearer ey` et être assez long
- Copier cette valeur
- Créer un fichier nommé exactement "bearer.txt" dans le même dossier que ce README
- Coller la valeur du bearer dans ce fichier et sauvegarder le.

# Exécution

- Assurer vous d'avoir Python 3 et le package requests
- Cloner ou télécharger et extraire le contenu de ce dossier localement
- Ouvrir une console et exécuter `python main.py` (Sur Mac et Linux, la commande est souvent `python3` au lieu de `python`)
- Si tout se passe bien, le programme aura créer un fichier `contacts_export_AAAA_MM_JJ.json` dans le répertoire `QS` sous votre répertoire d'utilisateur. Le chemin vers le fichier est affiché à la fin.

# À venir

Je ne fais aucune garantie, mais si intérêt, voici des fonctionnalités qui pourraient s'ajouter:

- Export en CSV (pour tableur Excel)
- Instructions pour débutants
- Filtres (présentement, le filtre est "membres en règle")
- Ouvert aux suggestions!