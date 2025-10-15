from pymongo import MongoClient

MONGO_URI = "mongodb://user:password@localhost:27017/admin"

def connect2DB():
    client = MongoClient(MONGO_URI,serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    print("✅ Successfully connected to MongoDB!")
    return client

def show_case_collection_docuements(collection):
    cursor = collection.find()
    for document in cursor:
        print(document)



if __name__ == '__main__':
    client = connect2DB()

    # Exercice 2
    # 1. Créez une nouvelle base de données appelée CinemaDB
    db_CinemaDB = client['CinemaDB']
    # 2. Créez une première collection nommée Films.
    collection_films = db_CinemaDB['Films']
    # 3. Ajoutez un document simple dans Films avec les champs id, titre, annee.
    premier_film_doc = {"id":1,"title":"Inception","annee":2010}

    result = collection_films.insert_one(premier_film_doc)
    print(f"Insertion Acknowledged: {result.acknowledged}")

    #4. Ajoutez un document intermédiaire dans Films avec des champs
    # supplémentaires (genre, duree).
    film_doc2 = {"id":2,"title":"Inception","annee":2010, "genre":"Action", "duree":"1h50"}
    result = collection_films.insert_one(film_doc2)

    #5. Ajoutez un document avancé dans Films contenant :
    # un objet imbriqué pour le réalisateur (nom, nationalite),
    # un tableau d’acteurs principaux.

    collection_films.insert_one({
        "id":3,
        "title":"Inception",
        "anneé":2010,
        "genre":"Action",
        "duree":"1h50",
        "réalisateur" :{
            "nom": "Ahmed",
            "nationalité" : "Maroccaine"
        },
        "acteurs":["Ahmed","Oussama","Anas","Ali"]
    })

    # 6.Montrez la flexibilité de MongoDB en ajoutant un document dans la
    # même collection Films, mais avec des champs différents (langue, budget,
    # noteIMDB).
    collection_films.insert_one({
        "id": 4,
        "title": "Inception",
        "anneé": 2010,
        "genre": "Action",
        "duree": "1h50",
        "réalisateur": {
            "nom": "Ahmed",
            "nationalité": "Maroccaine"
        },
        "acteurs": ["Ahmed", "Oussama", "Anas", "Ali"],
        "langue" : "Anglaise" # ajout du champs langue
    })
    collection_films.insert_one({
        "id": 5,
        "title": "Inception",
        "anneé": 2010,
        "genre": "Action",
        "duree": "1h50",
        "réalisateur": {
            "nom": "Ahmed",
            "nationalité": "Maroccaine"
        },
        "acteurs": ["Ahmed", "Oussama", "Anas", "Ali"],
        "budget" : "Anglaise" # ajout du champs budget
    })
    collection_films.insert_one({
        "id": 6,
        "title": "Inception",
        "anneé": 2010,
        "genre": "Action",
        "duree": "1h50",
        "réalisateur": {
            "nom": "Ahmed",
            "nationalité": "Maroccaine"
        },
        "acteurs": ["Ahmed", "Oussama", "Anas", "Ali"],
        "noteIMDB" : "Anglaise" # ajout du champs noteIMDB
    })
    show_case_collection_docuements(collection_films)
    # 7. Créez une collection Realisateurs et insérez plusieurs documents simples
    # (id, nom, pays)

    collection_realisateurs = db_CinemaDB['Realisateurs']
    collection_realisateurs.insert_many(
        [
            { "id": 1, "nom": "Christopher Nolan", "pays": "UK", "annee_naissance": 1970,"nombre_films": 10 },
            { "id": 2, "nom": "Quentin Tarantino", "pays": "USA", "annee_naissance": 1963,"nombre_films": 9 }
        ]
    )

    # 8.Ajoutez plusieurs documents avancés dans Realisateurs, en utilisant :
    # un champ imbriqué (contact avec email et telephone),
    # un tableau de films réalisés
    collection_realisateurs.insert_many(
        [
            # ajout d un champ imbriqué (contact avec email et telephone)
            { "id": 3, "nom": "Christopher Nolan", "pays": "UK", "annee_naissance": 1970,"nombre_films": 10 , "contact": {"email": "ChristopherNolan@gmail.com", "telephone": "0123456789"}},
            # ajout d un tableau de films réalisés
            { "id": 4, "nom": "Quentin Tarantino", "pays": "USA", "annee_naissance": 1963,"nombre_films": 9 , "films": ["film1", "film2"] },
        ]
    )
    show_case_collection_docuements(collection_realisateurs)
    # 14.Créez une collection Seances et insérez plusieurs documents contenant :
    # 15.un identifiant de film,
    # 16.une date de projection,
    # 17.une salle,
    # 18.un champ optionnel (tickets_vendus).


    collection_seance = db_CinemaDB['Seance']
    collection_seance.insert_many([
        {"film_id": 1, "date": "2025-10-15", "salle": "Salle A", "tickets_vendus": 120 },
        {"film_id": 2, "date": "2025-10-20", "salle": "Salle B"},
        {"film_id": 3, "date": "2025-10-20", "tickets_vendus": 120 }
    ])
    show_case_collection_docuements(collection_seance)








