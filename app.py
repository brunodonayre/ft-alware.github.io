from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta'  # Clave secreta para las sesiones

# Datos de usuario (almacenados en memoria para este ejemplo)
usuarios = {
    'bdonayred@vitapro.com.pe': 'Lima2022',
    'plataformas@vitapro.com.pe': 'Lima2022',
}

# Ruta para la página de inicio
@app.route('/')
def inicio():
    return 'Bienvenido a la página de inicio'

# Ruta para el formulario de inicio de sesión

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Verificar si las credenciales son válidas
        if usuario in usuarios and usuarios[usuario] == contrasena:
            # Iniciar sesión y redirigir al usuario a una página protegida
            session['usuario'] = usuario
            #return redirect(url_for('index.html'))return redirect('/')
            return redirect('/')
        else:
            # Credenciales incorrectas, mostrar un mensaje de error
            return 'Credenciales incorrectas. <a href="/login">Intenta de nuevo</a>'

    return render_template('login.html')  # Muestra el formulario de inicio de sesión

# Ruta para la página protegida (requiere inicio de sesión)
@app.route('/index.html')
def pagina_protegida():
    if 'usuario' in session:
        return f'Bienvenido, {session["usuario"]}! Esta es una página protegida.'
    else:
        return 'Debes iniciar sesión para acceder a esta página.'

# Ruta para cerrar sesión
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return 'Has cerrado sesión. <a href="/login">Inicia sesión de nuevo</a>'

if __name__ == '__main__':
    app.run(debug=True)