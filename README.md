# API de Classification d'Images

## Description

Ce projet fournit une API de classification d'images en utilisant un modèle pré-entraîné ResNet18. L'API est construite avec Flask et permet aux utilisateurs de classer des images en envoyant soit des URLs d'images, soit des fichiers image. Le projet comprend également un client en ligne de commande pour interagir avec l'API et obtenir des résultats de classification.

## Fonctionnalités

- **API Flask** : API RESTful pour la classification d'images.
- **Modèle ResNet18** : Utilise un modèle pré-entraîné ResNet18 pour une classification précise des images.
- **Application Client** : Outil en ligne de commande pour interagir avec l'API et obtenir des prédictions.

## Pour Commencer

### Prérequis

- Python 3.8 ou version ultérieure
- Docker (pour le déploiement en conteneur)
- Docker Compose (pour gérer les applications multi-conteneurs Docker)

### Installation

#### 1. Cloner le Dépôt

```bash
git clone https://github.com/mouridoullah/image-classification-api.git
cd image-classification-api
```

#### 2. Configurer et Exécuter avec Docker
Pour construire et exécuter le projet avec Docker, suivez ces étapes :

##### 2.1 Construire les Images Docker 
```bash
docker-compose build
```
##### 2.2 Démarrer les Conteneurs :

```bash
docker-compose up -d
```

#### 3. Exécuter le Client
Après avoir démarré les conteneurs Docker, vous pouvez utiliser le script client pour envoyer des URLs d'images à l'API pour classification.

##### 3.1 Exécuter le Script Client :

```bash
python client/client.py
```

##### 3.2 Fournir les URLs d'Images : 
Lorsque vous y êtes invité, entrez l'URL de l'image que vous souhaitez classer ou laissez le champ vide pour quitter.

#### Exemple :
```
Entrez l'URL de l'image (ou appuyez sur Entrée pour quitter) : https://example.com/path_to_your_image.jpg
```

Le client affichera l'ID de la classe prédite et le nom de la classe.