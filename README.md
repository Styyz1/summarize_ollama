# Summarize_Ollama
Ce projet fait suite au projet "summarize_py". C'est une version avancé de ce projet, avec des personnes qui ont un matériel plus puissant pour pouvoir exécuter Ollama et ces modèles.
Summarize_Ollama est une application qui vous permet de résumé des textes avec Ollama facilement, il détecte tout seul les modèles installer sur votre système et vous laisse les choisir. 

## Installer Ollama
Pour installer Ollama voici leur [Github](https://github.com/ollama/ollama), vous trouverez un exécutable pour votre OS.

Pour installer un modèle, aller dans votre terminal et tapez : 

```
ollama pull <nom_du_modèle>
```
La liste des modèles est également dispo sur leur Github

## Installation de summarize_ollama
Pour initialiser le projet exécuter cette commande dans le terminal : 
```
git clone https://github.com/Styyz1/summarize_ollama
```
Puis dans le dossier 'summarize_ollama', créer votre environnement virtuel, avec cette commande 
```
python -m venv <nom_de_votre_environnement>
```

Ensuite, exécuter cette commande, pour obtenir les frameworks utiles à ce projet : 

```
pip install -r requirements.txt
```

Enfin, dans le même terminal exécuter la commande suivante pour lancer l'application : 

```
python app.py
```
Vous pourrez alors copier votre texte et choisir le modèle utiliser pour générer un résumé.



