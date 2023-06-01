import tweepy
from textblob import TextBlob

# Remplacez les valeurs par vos propres clés d'API Twitter
consumer_key = "VOTRE_CONSUMER_KEY"
consumer_secret = "VOTRE_CONSUMER_SECRET"
access_token = "VOTRE_ACCESS_TOKEN"
access_token_secret = "VOTRE_ACCESS_TOKEN_SECRET"

# Authentification avec les clés d'API Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Création d'un objet API Twitter
api = tweepy.API(auth)

# Définition du terme de recherche
search_term = "#Python"

# Récupération des tweets contenant le terme de recherche
tweets = api.search(q=search_term, count=100)

# Analyse des sentiments de chaque tweet
for tweet in tweets:
    # Utilisation de TextBlob pour l'analyse de sentiment
    analysis = TextBlob(tweet.text)
    
    # Affichage du tweet et de son sentiment
    print(tweet.text)
    print("Sentiment: ", analysis.sentiment.polarity)
    print("\n")

    # note :
    #Ce code utilise l'API Twitter et la bibliothèque TextBlob pour analyser les sentiments des tweets contenant le terme de recherche "#Python".
    #Vous devez remplacer les valeurs de vos clés d'API Twitter pour utiliser ce code. Les tweets récupérés sont ensuite analysés en utilisant TextBlob, qui attribue une polarité de sentiment entre -1 (négatif) et 1 (positif) à chaque tweet. 
    #Le code affiche ensuite le texte du tweet et sa polarité de sentiment.
