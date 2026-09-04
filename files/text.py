# #  Écrivez du code Python ici
import os


# # verifier cest le fichier exist ou pas

# file = os.path.exists("/home/mouad/Desktop/warm_up_python/files/text.py")

# if file:
#     print("Le fichier existe.")
#     with open("/home/mouad/Desktop/warm_up_python/files/config.yml", "r") as f:
#         content = f.read()
#         print("Contenu du fichier :")
#         print(content)
# else:
#     # print("Le fichier n'existe pas.")

#  Écrivez du code Python ici

import os
import shutil

dossier_source = "source"
dossier_destination = "destination"

fichiers = os.listdir(dossier_source)

for fichier in fichiers:
    if fichier.endswith(".csv"):
        chemin_source = dossier_source + "/" + fichier
        chemin_destination = dossier_destination + "/" + fichier

        shutil.copy(chemin_source, chemin_destination)

print("Copie terminée.")