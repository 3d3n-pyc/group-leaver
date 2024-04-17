# Programme Python : Readme

Le programme lit les fichiers à rechercher dans le répertoire `data` et ses sous-dossiers. Vous devez placer les fichiers à rechercher dans ce répertoire (et ses sous-dossiers) avant d'exécuter le programme. Il utilise la librairie `pystyle` pour afficher des messages colorés dans la console.

## Supression des modules

Les modules pouvant créer des conflits doivent être désintallés à l'aide de `pip`.

```bash
python -m pip uninstall -r interferances.txt
```

## Installation des modules

Les modules requis peuvent être installés à l'aide de `pip`.

```bash
python -m pip install -r requirements.txt
```

## Utilisation du programme

### Configuration

Configurez le script à partir du fichier [config.yml](/config.yml)

### Lancement du programme

Vous pouvez lancer le programme en exécutant le fichier [main.py](/main.py).

Le programme supprimera les groupes inactifs selon votre configuration.

## Licence
Ce programme est sous licence MIT. Veuillez consulter le fichier [LICENSE](/LICENSE) pour plus d'informations.

## Attention
Le script est uniquement à but éducatif. Je ne suis responsable d'aucun problème engendré par ce projet. (Il a néanmoins été fait de façon à ce que vous en ayez le moins possible)