import os  # Interagit avec le système de fichiers
import shutil  # Déplace les fichiers
import sys

CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".md"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Exécutables": [".exe", ".msi", ".bat", ".sh"]
}

def get_category(extension):
    """
    Cette fonction prend une extension de fichier (comme '.jpg') 

    Retourne la catégorie à laquelle elle appartient, par exemple: si c'est un fichier '.jpg', elle retournera "Images".
    """
    for category, extensions in CATEGORIES.items():  # On parcourt chaque catégorie et ses extensions
        if extension.lower() in extensions:  # Si l'extension du fichier est dans la catégorie
            return category  # Retourne le nom de la catégorie
    return "Autres"  # Si l'extension ne correspond à rien, on la classe dans "Autres"

def sort_files(directory):
    """
    Cette fonction prend un dossier en entrée et trie les fichiers qui s'y trouvent dans les sous-dossiers
    selon leur type (image, document, archive, etc.).
    """
    if not os.path.exists(directory):  # Vérifie si le dossier existe
        print(f"Le dossier '{directory}' n'existe pas.")
        exit(1)
    
    if not os.path.isdir(directory):
        print(f"Erreur: '{directory}' n'est pas un dossier valide.")
        exit(1)
    
    TestTrie = os.path.basename(__file__)  # Récupère le nom du script
    # On parcourt tous les fichiers dans le dossier
    for file in os.listdir(directory):  # Liste tous les fichiers dans le dossier
        file_path = os.path.join(directory, file)  # Crée le chemin complet du fichier
        
        if os.path.isfile(file_path) and file != TestTrie:  # Si c'est bien un fichier
            _, ext = os.path.splitext(file)  # Sépare le nom du fichier de son extension
            category = get_category(ext)  # On trouve la catégorie du fichier selon son extension
            category_path = os.path.join(directory, category)  # Crée le chemin du sous-dossier pour cette catégorie
            
            # Si le sous-dossier n'existe pas encore, on le crée
            if not os.path.exists(category_path):
                os.makedirs(category_path)
            
            # Déplace le fichier dans le sous-dossier approprié
            try:
                shutil.move(file_path, os.path.join(category_path, file))
                print(f"{file} -> {category}/")  # Affiche un message pour dire où le fichier a été déplacé
            except:
                print(f"Erreur lors du déplacement de {file}")

# Exécutée lorsque le script est lancé
if __name__ == "__main__":
    if len(sys.argv) == 2:
        sort_files(sys.argv[1])