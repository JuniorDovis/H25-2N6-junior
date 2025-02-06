import os
os.chdir(os.path.dirname(__file__)) # cette ligne change le répertoire courant 
# # allez dans le dossier Ex3 Videos
# # avec la boucle for, passez à travers chacun des dossiers de os.listdir()
# #     utilisez os.path.splitext pour obtenir le filename et l'extension
# #     utilisez split sur le filename pour obtenir le titre, le cours et le numéro du cours
# #     utilisez strip pour enlever les espaces qui pourraient rester pour le titre et le numéro
# #     en plus utilisez zfill pour remplir le numéro de sorte que 1 deviendra 01
# #     recréez le nouveau nom de fichier#   utliser os.rename pour renommer le fichier

directory = "Ex3 Videos.zip"
for filename in os.listdir(directory):
    name, ext = os.path.splitext(filename)
    parts = name.split("_")
    if len(parts) == 3:
        title = parts[0].strip()
        course = parts[1].strip()
        num = parts[2].strip().zfill(2)
        new_filname = f"{title}_{course}_{num}`{ext}"
        os.rename(filename, new_filname)
        print(f"Renommé :{filename} {new_filname}")
