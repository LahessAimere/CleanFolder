# CleanFolder 
<img src="https://www.hebergeur-image.com/upload/91.168.77.68-67aa9a112ff33.png" width="90" />

Un script pour garder les fichiers de l'ordinateur bien organisés en les triant automatiquement selon leur type (par exemple : images, documents, archives, exécutables).

## Fonctionnalités :
- Trie automatiquement les fichiers dans des catégories telles que "Images", "Documents", "Archives", et "Exécutables".
- Déplace les fichiers dans les sous-dossiers correspondants en fonction de leur extension.
- Crée des sous-dossiers s'ils n'existent pas déjà.

## Types de fichiers pris en charge :
- Images : ```.jpg, .jpeg, .png, .gif, .bmp```
- Documents : ```.pdf, .docx, .txt, .md```
- Archives : ```.zip, .rar, .7z, .tar, .gz```
- Exécutables : ```.exe, .msi, .bat, .sh```

## Installation :
Assurez-vous d'avoir Python installé sur votre système. Vous pouvez télécharger Python depuis  - [python.org](https://www.python.org/downloads/).

## Prérequis :
Aucune bibliothèque supplémentaire n'est nécessaire. Le script utilise les modules intégrés de Python : ```os, shutil, et sys```.

## Utilisation :
1. Téléchargez le script sur votre ordinateur.

2. Ouvrez un terminal ou une invite de commande.

3. Accédez au répertoire où se trouve le script en utilisant la commande cd :

```cd chemin/vers/le/script```
Pour exécuter le script, fournissez le chemin du répertoire que vous souhaitez organiser en tant qu'argument. Par exemple :

```python nomDuFichier.py "C:/Users/User/Documents"```
Remplacez "C:/Users/VotreNom/Documents" par le chemin réel du répertoire que vous souhaitez organiser.

- Le script triera les fichiers dans le répertoire spécifié et créera des sous-dossiers pour chaque type de fichier (par exemple, "Images", "Documents", etc.).
- Les fichiers seront déplacés dans leurs sous-dossiers correspondants en fonction de leurs extensions.

## Exemple de sortie :
Si vous exécutez le script sur un répertoire contenant des fichiers image, des documents et des archives, vous pourriez voir une sortie comme celle-ci :

```image1.jpg -> Images/```
```document1.pdf -> Documents/```
```archive1.zip -> Archives/```
Les fichiers seront déplacés dans leurs sous-dossiers respectifs (par exemple, Images, Documents, Archives).

## Notes :
- Le script ignore le fichier lui-même, donc il ne déplacera pas le fichier du script dans un sous-dossier.
- Si le répertoire spécifié n'existe pas, le script affichera un message d'erreur.
- Vous pouvez modifier les types de fichiers pris en charge dans le dictionnaire CATEGORIES si nécessaire.

## Licence :
Ce script est libre à utiliser et à modifier.
