import gettext

gettext.install("P4", "/locale")

# Unifier mention R


class Texts:
    main_menu = _("""                            ***
                    ~ MENU PRINCIPAL ~
                            ***\n
Veuillez taper la lettre correspondant au menu désiré :\n
N. Créer un nouveau tournoi ;
C. Continuer un tournoi en cours ;
RA. Consulter les rapports (classements de joueurs, tournois passés...) ;
U. Changer directement les classements des joueurs ;\n
A tout moment, vous pouvez quitter le programme en tapant Q.
    """)

    menu_tournament = """CREATION DE TOURNOI\n
Pour revenir à l'écran d'accueil, tapez R.

Pour créer un tournoi, veuillez taper les informations suivantes :\n"""
    menu_players = """Bienvenue dans le menu d'ajout de joueurs.

1. Sélectionner des joueurs existants
2. Créer un nouveau joueur.\n"""

    ranking_rounds = """\nVeuillez taper le caractère correspondant à l'option souhaitée.
R. Retour au menu principal\n"""

    menu_change_ranks = """
Sélectionnez un joueur en tapant le numéro associé, puis tapez son nouveau rang.
Vous pouvez retourner sur l'écran d'accueil en tapant R.\n"""

    menu_create_player = """CREATION DE JOUEUR\n
Pour retourner au menu Joueurs, tapez R.

Pour créer un joueurs, veuillez taper les informations suivantes :\n"""
    new_gender = """Veuillez entrer un genre : homme ou femme.\n"""
    wrong_date = """Date invalide. Format : jour/mois/année.
Merci d'entrer une date conforme.\n"""
    new_number = """Merci d'entrer un chiffre.\n"""
    wrong_time_control = """Veuillez taper le chiffre correspondant à votre sélection :
1. Bullet
2. Blitz
3. Coup rapide\n"""

    menu_rapport = """Bienvenue dans le menu de rapports.
Veuillez taper le chiffre correspondant à l'action souhaitée :
1. Liste de tous les joueurs
2. Listes de tous les tournois\n
Pour revenir à l'écran d'accueil, tapez R."""

    rapport_players = """Veuillez taper le chiffre correspondant à l'action souhaitée :
1. Ordonner tous les joueurs par ordre alphabétique
2. Ordonner tous les joueurs par classement\n"""

    rapport_tournament = """Veuillez sélectionner un tournoi :\n"""

    menu_rapport_tournament = """Veuillez taper le chiffre correspondant à l'action souhaitée :
1. Afficher tous les participants
2. Afficher tous les tours du tournoi
3. Afficher tous les matches du tournoi\n"""

    select_players = """Veuillez taper le chiffre du joueur souhaité.
Pour retourner au menu précédent, tapez R.\n"""

    rankings_main = """RAPPORTS

1. Liste de tous les joueurs
2. Liste de tous les tournois\n"""

    rankings_players = """RAPPORTS : JOUEURS\n
A. Liste par ordre alphabétique
S. Liste par score total\n
"""

    rankings_players_details = """
A. Liste par ordre alphabétique
S. Liste par score total\n
"""

    rankings_tournaments = """\nVeuillez entrer le chiffre correspondant au tournoi souhaité pour lister ses joueurs et rounds.
Tapez R pour revenir à l'écran Rapport.\n"""

    ranking_tournament = """\nVeuillez entrer le chiffre correspondant à l'option souhaitée.
1. Liste des joueurs par ordre alphabétique
2. Liste des joueurs par classement
3. Liste des tours et matches du tournoi
4. Retour à l'écran rapport\n"""

    ranking_rounds = """\nVeuillez taper le caractère correspondant à l'option souhaitée.
R. Retour à l'écran du tournoi\n"""

    matches_instructions = """Entrer les résultats :
1 si le joueur 1 a gagné, 2 si le joueur 2 a gagné, 3 pour un match nul.\n"""

    end_menu = """\nVeuillez entrer le caractère correspondant à la sélection souhaitée.
1. Retour à l'écran d'accueil
Q. Quitter\n"""
