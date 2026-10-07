import sqlite3
import pandas as pd

# 1. Configuración: Inicialización de la base de datos en memoria
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE ventas_tecnologia (
    id_venta INTEGER PRIMARY KEY,
    producto TEXT,
    categoria TEXT,
    precio_unitario REAL,
    cantidad INTEGER,
    fecha TEXT,
    pais TEXT
)
''')

# Usamos None en Python para que sqlite3 lo inserte como NULL en SQL
datos_prueba = [
    (1, 'Laptop Pro X', 'Laptops', 1200.0, 10, '2026-10-01', 'Colombia'),
    (2, 'Mouse Inalámbrico', 'Accesorios', 25.0, 50, '2026-10-02', 'Argentina'),
    (3, 'Monitor 4K', 'Monitores', 600.0, 20, '2026-10-03', 'Colombia'),
    (4, 'Teclado Mecánico', None, 150.0, 15, '2026-10-04', 'México'),
    (5, 'Smartphone Z', 'Celulares', 800.0, 5, '2026-10-05', 'Colombia'),
    (6, 'Servidor Rack', 'Infraestructura', 5500.0, 3, '2026-10-06', 'Colombia')
]

cursor.executemany('INSERT INTO ventas_tecnologia VALUES (?, ?, ?, ?, ?, ?, ?)', datos_prueba)
conn.commit()

def ejecutar_y_mostrar(query):
    return pd.read_sql_query(query, conn)

# 2. Selección Simple
query_simple = '''
/* ¿Qué productos tenemos en catálogo y cuál es su precio base de venta? */
SELECT 
    producto, 
    precio_unitario
FROM ventas_tecnologia
ORDER BY producto ASC;
'''
print("--- 1. Selección Simple ---")
print(ejecutar_y_mostrar(query_simple), "\n")

# 3. Filtrado Crítico
query_filtro = '''
/* ¿Cuáles son las transacciones de alto valor (superiores a $500) registradas específicamente en Colombia? */
SELECT *
FROM ventas_tecnologia
WHERE pais = 'Colombia' 
  AND precio_unitario > 500;
'''
print("--- 2. Filtrado Crítico ---")
print(ejecutar_y_mostrar(query_filtro), "\n")

# 4. Búsqueda de Nulos
query_nulos = '''
/* ¿Existen registros de ventas que requieran imputación de datos por falta de categorización? */
SELECT *
FROM ventas_tecnologia
WHERE categoria IS NULL;
'''
print("--- 3. Búsqueda de Nulos ---")
print(ejecutar_y_mostrar(query_nulos), "\n")

# 5. Análisis de Rendimiento (Agregación)
query_rendimiento = '''
/* ¿Cuál es el volumen de facturación total aportado por cada categoría de producto? */
SELECT 
    categoria,
    SUM(cantidad * precio_unitario) AS ingresos_totales
FROM ventas_tecnologia
GROUP BY categoria;
'''
print("--- 4. Análisis de Rendimiento ---")
print(ejecutar_y_mostrar(query_rendimiento), "\n")

# 6. Filtro de Élite (HAVING)
query_elite = '''
/* ¿Cuáles son las categorías clave del negocio que superan los $10,000 en ingresos totales? */
SELECT 
    categoria,
    SUM(cantidad * precio_unitario) AS ingresos_totales
FROM ventas_tecnologia
GROUP BY categoria
HAVING SUM(cantidad * precio_unitario) > 10000;
'''
print("--- 5. Filtro de Élite ---")
print(ejecutar_y_mostrar(query_elite), "\n")

conn.close()