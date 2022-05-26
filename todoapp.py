#Se importa la biblioteca de Flask
from flask import Flask, redirect, render_template, request, url_for, flash

#Objeto para inicializar la aplicación
#1. Nombre por defecto
#2. Ruta donde están los templates
app = Flask(__name__, template_folder='plantillaHTML')

#Seguridad de la app
app.secret_key = '0000'

#Almacenamiento de tareas
lista_tareas = []

#Primer controlador: inicial
#Lista actual de tareas pendientes y Formulario HTML para ingresar nuevas tareas
@app.route('/')
def principal():
    return render_template('principal.html', lista_tareas=lista_tareas)


#Segundo controlador: envío de un nuevo elemento
@app.route('/enviar', methods=['POST'])
def enviar():
    if request.method == 'POST':
        
        #Campos a llenar
        tarea = request.form['tarea']
        correo_electronico = request.form['correo_electronico']
        prioridad = request.form['prioridad']

        #Validación para que los campos no sean nulos
        if tarea == '' or correo_electronico == '':
            flash('LLenar todos los campos')
            return redirect(url_for('principal'))
        
        else:
            flash('¡Tarea agregada exitosamente!')
            lista_tareas.append({'tarea': tarea, 'correo_electronico': correo_electronico, 'prioridad': prioridad})
            return redirect(url_for('principal'))
        
#Tercer Controlador: Limpiar la Lista
@app.route('/borrar', methods=['POST'])
def borrar():
    if request.method == 'POST':
        
        #Verificación de la lista de tareas
        if lista_tareas == []:
            flash('Lista de tareas vacía')
            return redirect(url_for('principal'))

        else:
            lista_tareas.clear()
            flash('Lista de tareas borrada')
            return redirect(url_for('principal'))


#Método para correr la aplicación
if __name__ == '__main__':
    app.run(debug=True)