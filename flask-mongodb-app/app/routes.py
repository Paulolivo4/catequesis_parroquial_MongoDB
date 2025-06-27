from flask import Blueprint, render_template, request, redirect, url_for, current_app, flash

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    catequizados = list(current_app.mongo.db.catequizados.find())
    return render_template('index.html', catequizados=catequizados)

@bp.route('/add', methods=['POST'])
def add_item():
    nombre = request.form['Nombre_Catequizado']
    apellido = request.form['Apellido_Catequizado']
    current_app.mongo.db.catequizados.insert_one({
        'Nombre_Catequizado': nombre,
        'Apellido_Catequizado': apellido
    })
    return redirect(url_for('main.index'))

@bp.route('/delete/<id>', methods=['POST'])
def delete_item(id):
    current_app.mongo.db.Catequizado.delete_one({'_id': id})  # Replace with your actual model
    return redirect(url_for('main.index'))

@bp.route('/registro_catequizado', methods=['GET', 'POST'])
def registro_catequizado():
    if request.method == 'POST':
        # Validación básica
        campos = [
            'IdCatequizado', 'Nombre_Catequizado', 'Apellido_Catequizado',
            'FechaNacimiento_Catequizado', 'Cedula_Catequizado', 'Direccion_Catequizado',
            'Telefono_Catequizado', 'Email_Catequizado', 'Parroquia_IdParroquia',
            'GrupoCatequizado_IdGrupoCatequizado'
        ]
        for campo in campos:
            if not request.form.get(campo):
                flash(f'El campo {campo} es obligatorio.', 'error')
                return render_template('registro_catequizado.html')

        # Si pasa la validación, guarda el catequizado
        catequizado = {
            'IdCatequizado': int(request.form['IdCatequizado']),
            'Nombre_Catequizado': request.form['Nombre_Catequizado'],
            'Apellido_Catequizado': request.form['Apellido_Catequizado'],
            'FechaNacimiento_Catequizado': request.form['FechaNacimiento_Catequizado'],
            'Cedula_Catequizado': request.form['Cedula_Catequizado'],
            'Direccion_Catequizado': request.form['Direccion_Catequizado'],
            'Telefono_Catequizado': request.form['Telefono_Catequizado'],
            'Email_Catequizado': request.form['Email_Catequizado'],
            'Parroquia_IdParroquia': int(request.form['Parroquia_IdParroquia']),
            'GrupoCatequizado_IdGrupoCatequizado': int(request.form['GrupoCatequizado_IdGrupoCatequizado'])
        }
        current_app.mongo.db.catequizados.insert_one(catequizado)
        flash('Catequizado registrado exitosamente.', 'success')
        return redirect(url_for('main.index'))
    return render_template('registro_catequizado.html')

@bp.route('/eliminar_catequizado', methods=['GET', 'POST'])
def eliminar_catequizado():
    catequizados = list(current_app.mongo.db.catequizados.find())
    if request.method == 'POST':
        try:
            id_catequizado = int(request.form['IdCatequizado'])
            result = current_app.mongo.db.catequizados.delete_one({'IdCatequizado': id_catequizado})
            if result.deleted_count == 1:
                flash('Catequizado eliminado exitosamente.', 'success')
            else:
                flash('No se encontró un catequizado con ese ID.', 'error')
        except Exception as e:
            flash('Error al eliminar: ' + str(e), 'error')
    return render_template('eliminar_catequizado.html', catequizados=catequizados)

@bp.route('/editar_catequizado', methods=['GET', 'POST'])
def editar_catequizado():
    catequizados = list(current_app.mongo.db.catequizados.find())
    if request.method == 'POST':
        id_catequizado = int(request.form['IdCatequizado'])
        catequizado = current_app.mongo.db.catequizados.find_one({'IdCatequizado': id_catequizado})
        if catequizado:
            return render_template('editar_catequizado_form.html', catequizado=catequizado)
        else:
            flash('No se encontró un catequizado con ese ID.', 'error')
    return render_template('editar_catequizado.html', catequizados=catequizados)

@bp.route('/actualizar_catequizado', methods=['POST'])
def actualizar_catequizado():
    try:
        id_catequizado = int(request.form['IdCatequizado'])
        update_fields = {
            'Nombre_Catequizado': request.form['Nombre_Catequizado'],
            'Apellido_Catequizado': request.form['Apellido_Catequizado'],
            'FechaNacimiento_Catequizado': request.form['FechaNacimiento_Catequizado'],
            'Cedula_Catequizado': request.form['Cedula_Catequizado'],
            'Direccion_Catequizado': request.form['Direccion_Catequizado'],
            'Telefono_Catequizado': request.form['Telefono_Catequizado'],
            'Email_Catequizado': request.form['Email_Catequizado'],
            'Parroquia_IdParroquia': int(request.form['Parroquia_IdParroquia']),
            'GrupoCatequizado_IdGrupoCatequizado': int(request.form['GrupoCatequizado_IdGrupoCatequizado'])
        }
        result = current_app.mongo.db.catequizados.update_one(
            {'IdCatequizado': id_catequizado},
            {'$set': update_fields}
        )
        if result.modified_count == 1:
            flash('Catequizado actualizado exitosamente.', 'success')
        else:
            flash('No se realizaron cambios o no se encontró el catequizado.', 'error')
    except Exception as e:
        flash('Error al actualizar: ' + str(e), 'error')
    return redirect(url_for('main.index'))

@bp.route('/buscar_catequizado', methods=['GET', 'POST'])
def buscar_catequizado():
    resultados = []
    if request.method == 'POST':
        criterio = request.form['criterio']
        valor = request.form['valor']
        query = {}
        if criterio == 'nombre':
            query = {'Nombre_Catequizado': {'$regex': valor, '$options': 'i'}}
        elif criterio == 'apellido':
            query = {'Apellido_Catequizado': {'$regex': valor, '$options': 'i'}}
        elif criterio == 'cedula':
            query = {'Cedula_Catequizado': {'$regex': valor, '$options': 'i'}}
        resultados = list(current_app.mongo.db.catequizados.find(query))
    return render_template('buscar_catequizado.html', resultados=resultados)