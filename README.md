🚀 Ecommerce Data Pipeline (ETL)
Este proyecto implementa un pipeline de datos robusto que extrae información de productos desde una API externa, la transforma para su análisis y la almacena en una base de datos relacional para su posterior visualización.
📋 Descripción
El objetivo de este repositorio es demostrar un flujo ETL (Extract, Transform, Load) completo. Automatizamos la obtención de datos de un catálogo de comercio electrónico para generar insights sobre precios, categorías y valoración de productos.
🏗️ Arquitectura del Proyecto
Fuente de Datos: FakeStoreAPI (REST API).
Extracción y Transformación: Script en Python utilizando la librería requests para el consumo de datos y pandas para la limpieza y normalización.
Almacenamiento: Base de datos relacional PostgreSQL para persistencia de datos estructurados.
Visualización: Dashboard interactivo en Power BI conectado directamente a Postgres.
🛠️ Stack Tecnológico
Lenguaje: Python
Librerías principales: requests, pandas, sqlalchemy, psycopg2.
Base de Datos: PostgreSQL.
BI: Power BI Desktop.
