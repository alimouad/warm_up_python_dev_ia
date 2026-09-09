from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from database import Base


# =========================
# Categories
# =========================

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)

    plats = relationship("Plat", back_populates="categorie")


# =========================
# Plats
# =========================

class Plat(Base):
    __tablename__ = "plats"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    prix = Column(Float, nullable=False)
    description = Column(String(255))

    categorie_id = Column(
        Integer,
        ForeignKey("categories.id")
    )

    categorie = relationship(
        "Category",
        back_populates="plats"
    )


# =========================
# Clients
# =========================

class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    telephone = Column(String(20), nullable=True)

    commandes = relationship(
        "Commande",
        back_populates="client"
    )

    avis = relationship(
        "Avis",
        back_populates="client"
    )


# =========================
# Commandes
# =========================

class Commande(Base):
    __tablename__ = "commandes"

    id = Column(Integer, primary_key=True)

    client_id = Column(
        Integer,
        ForeignKey("clients.id")
    )

    date_commande = Column(
        DateTime,
        default=datetime.now
    )

    total = Column(Float, nullable=False)

    client = relationship(
        "Client",
        back_populates="commandes"
    )


# =========================
# Commande_Plat
# =========================

class CommandePlat(Base):
    __tablename__ = "commande_plats"

    commande_id = Column(
        Integer,
        ForeignKey("commandes.id"),
        primary_key=True
    )

    plat_id = Column(
        Integer,
        ForeignKey("plats.id"),
        primary_key=True
    )

    quantite = Column(
        Integer,
        nullable=False
    )


# =========================
# Fournisseurs
# =========================

class Fournisseur(Base):
    __tablename__ = "fournisseurs"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    contact = Column(String(100))

    ingredients = relationship(
        "Ingredient",
        back_populates="fournisseur"
    )


# =========================
# Ingredients
# =========================

class Ingredient(Base):
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True)
    nom = Column(String(100), nullable=False)
    cout_unitaire = Column(Float, nullable=False)
    stock = Column(Float, nullable=False)

    fournisseur_id = Column(
        Integer,
        ForeignKey("fournisseurs.id")
    )

    fournisseur = relationship(
        "Fournisseur",
        back_populates="ingredients"
    )


# =========================
# Plat_Ingredient
# =========================

class PlatIngredient(Base):
    __tablename__ = "plat_ingredients"

    plat_id = Column(
        Integer,
        ForeignKey("plats.id"),
        primary_key=True
    )

    ingredient_id = Column(
        Integer,
        ForeignKey("ingredients.id"),
        primary_key=True
    )

    quantite_necessaire = Column(
        Float,
        nullable=False
    )


# =========================
# Avis
# =========================

class Avis(Base):
    __tablename__ = "avis"

    id = Column(Integer, primary_key=True)

    client_id = Column(
        Integer,
        ForeignKey("clients.id")
    )

    plat_id = Column(
        Integer,
        ForeignKey("plats.id")
    )

    note = Column(
        Integer,
        nullable=False
    )

    commentaire = Column(Text)

    date_avis = Column(
        DateTime,
        default=datetime.now
    )

    client = relationship(
        "Client",
        back_populates="avis"
    )

    plat = relationship("Plat")