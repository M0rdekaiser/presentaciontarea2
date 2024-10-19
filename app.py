from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>Menú de Formularios</h1>
        <ul>
            <li><a href="/inscripcion">Inscripción en curso</a></li>
            <li><a href="/registro_usuarios">Registro de usuarios</a></li>
            <li><a href="/registro_productos">Registro de productos</a></li>
            <li><a href="/registro_libros">Registro de libros</a></li>
        </ul>
    '''

# Inscripción en curso
@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        curso = request.form['curso']
        return f"Inscripción exitosa: {nombre} {apellidos} en el curso {curso}"
    return '''
        <h2>Inscripción en curso</h2>
        <form method="post">
            <label>Nombre:</label><br>
            <input type="text" name="nombre"><br>
            <label>Apellidos:</label><br>
            <input type="text" name="apellidos"><br>
            <label>Curso:</label><br>
            <select name="curso">
                <option>Curso 1</option>
                <option>Curso 2</option>
                <option>Curso 3</option>
            </select><br><br>
            <input type="submit" value="Enviar">
        </form>
    '''

# Registro de usuarios
@app.route('/registro_usuarios', methods=['GET', 'POST'])
def registro_usuarios():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        correo = request.form['correo']
        contraseña = request.form['contraseña']
        return f"Usuario registrado: {nombre} {apellidos}, correo: {correo}"
    return '''
        <h2>Registro de usuarios</h2>
        <form method="post">
            <label>Nombre:</label><br>
            <input type="text" name="nombre"><br>
            <label>Apellidos:</label><br>
            <input type="text" name="apellidos"><br>
            <label>Correo electrónico:</label><br>
            <input type="email" name="correo"><br>
            <label>Contraseña:</label><br>
            <input type="password" name="contraseña"><br><br>
            <input type="submit" value="Enviar">
        </form>
    '''

# Registro de productos
@app.route('/registro_productos', methods=['GET', 'POST'])
def registro_productos():
    if request.method == 'POST':
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        return f"Producto registrado: {producto}, Categoría: {categoria}, Existencia: {existencia}, Precio: {precio}"
    return '''
        <h2>Registro de productos</h2>
        <form method="post">
            <label>Producto:</label><br>
            <input type="text" name="producto"><br>
            <label>Categoría:</label><br>
            <select name="categoria">
                <option>Categoría 1</option>
                <option>Categoría 2</option>
                <option>Categoría 3</option>
            </select><br>
            <label>Existencia:</label><br>
            <input type="number" name="existencia"><br>
            <label>Precio:</label><br>
            <input type="text" name="precio"><br><br>
            <input type="submit" value="Enviar">
        </form>
    '''

# Registro de libros
@app.route('/registro_libros', methods=['GET', 'POST'])
def registro_libros():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        return f"Libro registrado: {titulo} por {autor}, Medio: {medio}"
    return '''
        <h2>Registro de libros</h2>
        <form method="post">
            <label>Título:</label><br>
            <input type="text" name="titulo"><br>
            <label>Autor:</label><br>
            <input type="text" name="autor"><br>
            <label>Resumen:</label><br>
            <textarea name="resumen"></textarea><br>
            <label>Medio:</label><br>
            <input type="radio" name="medio" value="Físico"> Físico<br>
            <input type="radio" name="medio" value="Magnético"> Magnético<br><br>
            <input type="submit" value="Enviar">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
