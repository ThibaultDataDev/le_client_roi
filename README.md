# Pour utiliser ce programme il vous faudra
- Un navigateur internet
- Python 3

## Installation sur votre machine

- Copier/coller le dossier sur votre ordinateur
- Ouvrez un terminal et utilisez la commande ```cd <folder_path>/le_client_est_roi``` afin de pouvoir acceder au dossier
- Créez un environnement virtuel et lancez le (recommandé):
    -https://docs.python.org/fr/3/library/venv.html si vous utilisez un terminal windows
    -https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html si vous utilisez anaconda
- Utilisez les commande ```pip install Flask``` puis ```pip install pymongo``` sur vous utilisez le terminal python ou ```conda install Flask``` puis ```conda install pymongo``` si vous utilisez Anaconda, l'environnement est prêt à être utilisé.

### - Utilisation

- Dans ce même terminal, utilisez la commande ```python api.py``` pour lancer le serveur
- L'url http://localhost:5000/country renvoie la liste de tous les pays 
- L'url http://localhost:5000/country/France renvoie une recherche du pays demandé (France dans cet exemple)
- L'url http://localhost:5000/addcountry/<name> ajoute un pays à la base de donnée, les valeurs de densité et population sont aléatoires
- L'url http://localhost:5000/category/<1/2/3 ou 4> renvoie une tranche des pays présents dans la base, classés selon leur densité
