# Exploración SQL - Ventas Tecnología

Simulación de exploración inicial de datos (EDA) sobre la tabla `ventas_tecnologia` utilizando Python (`sqlite3` y `pandas`).

## Consultas resueltas
1. **Selección Simple:** Catálogo de productos y precios ordenados alfabéticamente (`ORDER BY`).
2. **Filtrado Crítico:** Ventas en Colombia con precio unitario superior a 500 (`WHERE`).
3. **Búsqueda de Nulos:** Detección de registros sin categoría asignada (`IS NULL`).
4. **Análisis de Rendimiento:** Facturación total agrupada por categoría (`SUM` + `GROUP BY`).
5. **Filtro de Élite:** Categorías que superan los 10,000 en ingresos totales (`HAVING`).

## Instalación y Configuración

1. Clonar el repositorio y entrar a la carpeta:
   git clone [https://github.com/santiagoflorin/sql_practica.git](https://github.com/santiagoflorin/sql_practica.git)
   cd sql_practica

2. Crear y activar el entorno virtual:
   python3 -m venv .venv
   source .venv/bin/activate

3. Instalar las dependencias:
   pip install -r requirements.txt

## Cómo ejecutar el proyecto

Para correr el script que crea la tabla en memoria y ejecuta las 5 consultas SQL, usar el siguiente comando en la terminal:

   python exploracion_ventas.py