import sqlite3

# Conectar o crear la base de datos (será un archivo SQLite)
conn = sqlite3.connect('users.db')  # Esto creará el archivo en la carpeta actual
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

# Insertar algunos datos de ejemplo
cursor.executemany('''
INSERT INTO users (name, email) VALUES (?, ?)
''', [
    ('Juan', 'juan@example.com'),
    ('Maria', 'maria@example.com'),
    ('Carlos', 'carlos@example.com')
])

# Guardar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos y tabla 'users' creadas exitosamente.")
