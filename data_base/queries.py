from sqlalchemy.orm import Session
from sqlalchemy import func

from database import engine
from models import Plat , Client, Commande, CommandePlat


session = Session(engine)

# filter plats with price between 30 and 80
plats = session.query(Plat).filter(
    Plat.prix.between(30, 80)
).all()

# filer clients with name starting with "S" or "F"
clients = session.query(Client).filter(
    Client.nom.like("S%"),
    # Client.nom.like("F%")
).all()


resultats = session.query(
    Commande.id,
    Client.nom,
    Commande.date_commande,
    func.sum(CommandePlat.quantite).label("total_plats")
).join(
    Client,
    Commande.client_id == Client.id
).join(
    CommandePlat,
    Commande.id == CommandePlat.commande_id
).group_by(
    Commande.id,
    Client.nom,
    Commande.date_commande
).all()


# number of commandes per client
resultats = session.query(
    Client.nom,
    func.count(Commande.id).label("nombre_commandes")
).join(
    Commande,
    Client.id == Commande.client_id
).group_by(
    Client.id,
    Client.nom
).order_by(
    func.count(Commande.id).desc()
).all()

# commands between July 1, 2025 and September 30, 2025
commandes = session.query(Commande).filter(
    Commande.date_commande >= "2025-07-01",
    Commande.date_commande < "2025-10-01"
).all()

# clients widh total commandes greater than 150
nombre_total = session.query(
    Client.nom,
    Client.telephone,
    Commande.total
).join(
    Commande,
    Client.id == Commande.client_id
).filter(
    Commande.total > 150
).all()

for client in nombre_total:
    print(
        f"Client: {client.nom} | "
        f"Téléphone: {client.telephone} | "
        f"Montant: {client.total}"
    )


for commande in commandes:
    print(
        f"Commande {commande.id} | "
        f"Date: {commande.date_commande} | "
        f"Total: {commande.total}"
    )

for client in resultats:
    print(
        f"{client.nom} : {client.nombre_commandes} commandes"
    )

# for commande in resultats:
#     print(
#         f"Commande {commande.id} | "
#         f"Client: {commande.nom} | "
#         f"Date: {commande.date_commande} | "
#         f"Total plats: {commande.total_plats}"
#     )


for client in clients:
    print(client.nom)


for plat in plats:
    print(plat.nom, "-", plat.prix)

session.close()