import os
os.chdir(os.path.dirname(__file__)) # cette ligne change le répertoire courant pour qu'il devienne celui où ce trouve le fichier actuel.

# Q1  Imprimez le répertoire courant
print(f"Q1{'_'*60}")
print(f"Q1: Répertoire courant {os.getcwd}")


# Q2   Imprimez la variable d'environnement USERPROFILE (utilisez la méthode .get() de l'objet os.environ)
print(f"Q2{'_'*60}")
user_profile = os.environ.get('USERPROFILE')
print(f"Q2:USERPROFILE {user_profile}")


# Q3 Déplacez-vous sur le répertoire 'Documents' et imprimez le répertoire courant
#       Attention : n'utilisez pas un chemin relatif.
print(f"Q3{'_'*60}")
document_path = os.path.join(user_profile, "Documents")
os.chdir(document_path)
print(f"Q3:Nouveau répertoire courant {os.getcwdb()}")

# Q4   Imprimez la liste des répertoires et des fichiers qu'il y a dans 'Document'
print(f"Q4{'_'*60}")
documents_content = os.listdir
print(f"Q4: Contenue de 'Documents' {documents_content}")


# Q5   Créez un répertoire OS-ExercQ5
#       Réimprimez les répertoires et les fichiers dans 'Document'
print(f"Q5{'_'*60}")
os.makedirs("OS-EXERCQ5", exist_ok=True)
documents_content_after = os.listdir()
print(f"Q5: contenue apres création de 'OS-EXercQ5' {documents_content_after}")


# Q6   Créez les répertoires OS-ExercQ6/Subdir1 avec une seule instruction
#       Réimprimez les répertoires et les fichiers dans votre 'Document'
print(f"Q6{'_'*60}")
os.makedirs(os.path.join(document_path, "OS-ExercQ6", "Subdir1"), exist_ok=True)
print(f"Q6: Dossiers créés {os.listdir(document_path)}")


#Q7   Renommez le répertoire Subdir1 pour qu'il s'appelle Sous_repertoire
print(f"Q6{'_'*60}")
#os.rename("OS-ExercQ7/Subdir1", "OS-ExercQ6/Sous-repertoire)


# Q8   suppression du répertoire OS-ExercQ6 et de son contenu
#       Réimprimez les répertoires et les fichiers dans votre 'Document'
print(f"Q6{'_'*60}")





