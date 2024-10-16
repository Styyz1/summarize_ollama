from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

def get_models():
    # Exécuter la commande pour lister les modèles installés
    command = 'ollama list'
    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    # Extraire les modèles de la sortie
    models = []
    if result.returncode == 0:
        # Ignore la première ligne (les en-têtes) et prend uniquement le premier mot de chaque ligne
        for line in result.stdout.splitlines()[1:]:  # Ignorer la première ligne
            model_name = line.split()[0]  # Prendre uniquement le nom du modèle
            models.append(model_name)  # Ajouter le modèle à la liste
    return models

@app.route('/', methods=['GET', 'POST'])
def index():
    resume = None
    models = get_models()  # Récupérer les modèles installés
    if request.method == 'POST':
        texte = request.form['texte']
        model = request.form['model']  # Récupérer le modèle sélectionné

        # Formuler le prompt pour résumer le texte en français
        prompt = f"Résume ce texte en français : {texte}"

        # Appeler Ollama pour générer le résumé avec le modèle choisi
        command = f'ollama run {model} "{prompt}"'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        resume = result.stdout.strip()  # Récupérer la sortie de la commande

    return render_template('index.html', resume=resume, models=models)

if __name__ == '__main__':
    app.run(debug=True)