# Per iniziare da questo progetto

```
python -m venv flask
source flask/bin/activate
pip install -r requirements.txt
```

# Per iniziare ex-novo un progetto Flask

[Sito Flask](https://flask.palletsprojects.com/en/stable/)

```
python -m venv flask
source flask/bin/activate
pip install flask
```

# Creare i folder necessari

Il folder `templates` è il folder predefinito per la funzione `render_template()`. I template flask usano il linguaggio di template [Jinja](https://palletsprojects.com/projects/jinja/) e possono essere gerarchici.

```
mkdir templates
```

# Per salvare tutti i requirements nel file `requirements.txt`

```
pip freeze > requirements.txt
```



