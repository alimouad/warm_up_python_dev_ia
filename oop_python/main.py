from abc import ABC, abstractmethod
from datetime import date

class Employee(ABC):
    def __init__(self, nom, matricule, prénom, année_de_naissance):
        self.nom = nom
        self.matricule = matricule
        self.prénom = prénom
        self.année_de_naissance = année_de_naissance


    def __str__(self):
        return f"Nom: {self.nom}, Matricule: {self.matricule}, Prénom: {self.prénom}, Année de naissance: {self.année_de_naissance}"

    @abstractmethod
    def get_salaire(self):
        pass

 


class Ouvrier(Employee):
    def __init__(self, nom, matricule, prénom, année_de_naissance, année_dentrée):
        super().__init__(nom, matricule, prénom, année_de_naissance)
        self.année_dentrée = année_dentrée
        self.SMIG = 2500
        
    def get_salaire(self):
        annee_actuelle = date.today().year
        anciennete = annee_actuelle - self.année_dentrée

        salaire = self.SMIG + (anciennete * 100)

        salaire_max = self.SMIG * 2

        if salaire > salaire_max:
            salaire = salaire_max

        return salaire
    
    def __str__(self):
        return (
            super().__str__()
            + f", Année d'entrée : {self.année_dentrée}"
        )

class Manager(Employee):
    def __init__(self, nom, matricule, prénom, année_de_naissance, chiffre_d_affaire, indice):
        super().__init__(nom, matricule, prénom, année_de_naissance)
        self.chiffre_d_affaire = chiffre_d_affaire
        self.indice = indice


    def get_salaire(self):
        salaires = {
            1: 13000,
            2: 15000,
            3: 17000
        }

        return salaires.get(self.indice, 0)

    def __str__(self):
        return (
            super().__str__()
            + f", Indice : {self.indice}"
        )


class Cadre(Employee):
    chiffre_affaire = 0
    def __init__(self, nom, matricule, prenom, annee_naissance):
        super().__init__(
            nom,
            matricule,
            prenom,
            annee_naissance
        )

    def get_salaire(self):
        return self.chiffre_affaire * 0.1

    def __str__(self):
        return super().__str__()


ouvrier = Ouvrier("John", "123", "Doe", 1990, 2015)   
patron = Manager("Alice", "456", "Smith", 1985, 100000, 2)
cadre = Cadre("Bob", "789", "Johnson", 1980)

employees = [ouvrier, patron, cadre]
for employee in employees:
    print(employee)
    print(f"Salaire: {employee.get_salaire()} DH")
    print()
    
    
    
# 2. Créer l'interface (classe abstraite) IEmploye avec les méthodes suivantes :
# a. Une méthode age() qui retournera l'âge d'un employé (entier).
# b. Une méthode anciennete() qui retournera l'ancienneté d'un employé (le nombre d'années travaillées).
# c. Une méthode date_retraite(age_retraite) qui renvoie la date de retraite : date de retraite = date de naissance + âge de retraite.
# Un employé est caractérisé par : Matricule (mtle), Nom (nom), Date de naissance (date_naissance), Date d'embauche (date_embauche), Salaire de base (salaire_base).


class IEmploye(ABC):
    @abstractmethod
    def age(self):
        pass

    @abstractmethod
    def anciennete(self):
        pass

    @abstractmethod
    def date_retraite(self, age_retraite):
        pass

class Employe(IEmploye):
    def __init__(self, mtle, nom, date_naissance, date_embauche, salaire_base):
        self.mtle = mtle
        self.nom = nom
        self.date_naissance = date_naissance
        self.date_embauche = date_embauche
        self.salaire_base = salaire_base

    def age(self):
        today = date.today()
        return today.year - self.date_naissance.year - ((today.month, today.day) < (self.date_naissance.month, self.date_naissance.day))

    def anciennete(self):
        today = date.today()
        return today.year - self.date_embauche.year - ((today.month, today.day) < (self.date_embauche.month, self.date_embauche.day))

    def date_retraite(self, age_retraite):
        return self.date_naissance.replace(year=self.date_naissance.year + age_retraite)
    
    def __str__(self):
        return (
            f"Matricule : {self.mtle}\n"
            f"Nom : {self.nom}\n"
            f"Date de naissance : {self.date_naissance}\n"
            f"Date d'embauche : {self.date_embauche}\n"
            f"Salaire de base : {self.salaire_base} DH"
        )
        
        
employe1 = Employe("001", "Alice", date(1980, 5, 15), date(2010, 6, 1), 50000) 
print(employe1)      
print(employe1.date_retraite(65)) 


# 3. Créer la classe abstraite Employe avec :
# a. Les attributs (accessibles dans les classes filles de Employe).
# b. Les deux accesseurs (properties) date_embauche et date_naissance.
# c. Un constructeur par défaut et un autre d'initialisation.
# d. Une méthode abstraite salaire_a_payer() pour retourner le salaire net d'un employé.
# e. L'implémentation de l'interface IEmploye avec ces trois méthodes.
# f. La redéfinition de la méthode __str__() qui renvoie toutes les propriétés.
# Un formateur est un employé avec en plus : le nombre d'heures supplémentaires par mois (heure_sup) et la rémunération par heure supplémentaire, dont la valeur est partagée par tous les formateurs et par défaut égale à 70,00 DH (remuneration_hsup).


class Employe(IEmploye, ABC):

    def __init__(
        self,
        mtle=None,
        nom=None,
        date_naissance=None,
        date_embauche=None,
        salaire_base=0
    ):
        self._mtle = mtle
        self._nom = nom
        self._date_naissance = date_naissance
        self._date_embauche = date_embauche
        self._salaire_base = salaire_base

    # =========================
    # Properties
    # =========================

    @property
    def date_naissance(self):
        return self._date_naissance

    @date_naissance.setter
    def date_naissance(self, value):
        self._date_naissance = value

    @property
    def date_embauche(self):
        return self._date_embauche

    @date_embauche.setter
    def date_embauche(self, value):
        self._date_embauche = value

    # =========================
    # Implémentation IEmploye
    # =========================

    def age(self) -> int:
        aujourd_hui = date.today()

        age = (
            aujourd_hui.year
            - self._date_naissance.year
        )

        if (
            aujourd_hui.month,
            aujourd_hui.day
        ) < (
            self._date_naissance.month,
            self._date_naissance.day
        ):
            age -= 1

        return age

    def anciennete(self) -> int:
        aujourd_hui = date.today()

        anciennete = (
            aujourd_hui.year
            - self._date_embauche.year
        )

        if (
            aujourd_hui.month,
            aujourd_hui.day
        ) < (
            self._date_embauche.month,
            self._date_embauche.day
        ):
            anciennete -= 1

        return anciennete

    def date_retraite(self, age_retraite: int) -> date:
        return date(
            self._date_naissance.year + age_retraite,
            self._date_naissance.month,
            self._date_naissance.day
        )

    # =========================
    # Méthode abstraite
    # =========================

    @abstractmethod
    def salaire_a_payer(self) -> float:
        pass

    # =========================
    # __str__
    # =========================

    def __str__(self):
        return (
            f"Matricule : {self._mtle}\n"
            f"Nom : {self._nom}\n"
            f"Date de naissance : {self.date_naissance}\n"
            f"Date d'embauche : {self.date_embauche}\n"
            f"Salaire de base : {self._salaire_base} DH"
        )
        
class Formateur(Employe):
    remuneration_hsup = 70.0

    def __init__(
        self,
        mtle=None,
        nom=None,
        date_naissance=None,
        date_embauche=None,
        salaire_base=0,
        heure_sup=0
    ):
        super().__init__(
            mtle,
            nom,
            date_naissance,
            date_embauche,
            salaire_base
        )
        self.heure_sup = heure_sup

    def salaire_a_payer(self) -> float:
        return (
            self._salaire_base
            + (self.heure_sup * Formateur.remuneration_hsup)
        )

    def __str__(self):
        return (
            super().__str__()
            + f"\nHeures supplémentaires : {self.heure_sup}\n"
            f"Rémunération par heure supplémentaire : {Formateur.remuneration_hsup} DH"
        )        
        
form = Formateur(
    mtle="002",
    nom="Bob",
    date_naissance=date(1985, 3, 20),
    date_embauche=date(2012, 4, 15),
    salaire_base=60000,
    heure_sup=10
)
print(form)
print(f"Salaire à payer : {form.salaire_a_payer()} DH")        