from flask import Flask, render_template, request
app=Flask(__name__)
RECETAS=[
{"id":1,"nombre":"Rosca de Color","produccion":65,"costo":45.40},
{"id":2,"nombre":"Empanada Salpor","produccion":20,"costo":55.92},
{"id":3,"nombre":"Frances","produccion":318,"costo":53.24},
{"id":4,"nombre":"Donas","produccion":288,"costo":56.52},
]
@app.route('/')
def home():
    q=request.args.get('q','').lower()
    datos=[r for r in RECETAS if q in r['nombre'].lower()]
    return render_template('index.html',recetas=datos)
@app.route('/receta/<int:id>')
def receta(id):
    receta=next((r for r in RECETAS if r['id']==id),None)
    return render_template('receta.html',receta=receta)
if __name__=='__main__':
    app.run(debug=True)
