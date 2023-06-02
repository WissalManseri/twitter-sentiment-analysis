# Analyse des sentiments sur Twitter

Ce code en Python utilise l'API Twitter et la bibliothèque TextBlob pour analyser les sentiments des tweets contenant un terme de recherche spécifique.

# Installation
Cloner ce dépôt :

    git clone https://github.com/WISSAL-MN/twitter-sentiment-analysis.git
Installer les dépendances :

        pip install tweepy
        pip install textblob
        
Ajouter vos clés d'API Twitter dans le fichier sentiment_twitter.py :

        consumer_key = "VOTRE_CONSUMER_KEY"
        consumer_secret = "VOTRE_CONSUMER_SECRET"
        access_token = "VOTRE_ACCESS_TOKEN"
        access_token_secret = "VOTRE_ACCESS_TOKEN_SECRET"
        
# Utilisation
Exécuter le script sentiment_twitter.py :

      python sentiment_twitter.py
      
Le script récupère les tweets contenant le terme de recherche "#Python" et affiche leur texte ainsi que leur polarité de sentiment entre -1 et 1.

# Remarque
Ce script est un exemple de base pour l'analyse de sentiment sur Twitter en utilisant Python. Vous pouvez l'adapter à vos besoins en modifiant le terme de recherche ou en ajoutant des fonctionnalités supplémentaires.

# Auteur
Ce code a été écrit par wissalmanseri@gmail.com

# Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, n'hésitez pas à ouvrir une demande d'extraction.

# Licence
Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
