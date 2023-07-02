from conneToDB import connectDB


def get_prof_by_class(class_id):
    # se connecter à la base de données
    conn, cursor = connectDB("student_managment")

    # exécuter une requête SQL pour récupérer les résultats
    sql = "SELECT DISTINCT p.firstname, p.lastname, email_prof FROM prof p, departement d, filier f, class c, student s WHERE f.id_departement = p.id_departement AND c.id_filier = f.id_filier AND p.id_departement = d.id_departement AND s.id_class = c.id_class AND s.id_class = %s"
    val = (class_id,)
    cursor.execute(sql, val)

    # récupérer les résultats de la requête
    resultats = cursor.fetchall()

    # stocker les résultats dans une liste de listes
    liste_resultats = []
    for resultat in resultats:
        liste_resultats.append(list(resultat))

    # fermer la connexion à la base de données
    conn.close()

    # retourner la liste de listes
    return liste_resultats


print(get_prof_by_class(1))
