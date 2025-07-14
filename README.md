# 🌍 Proyecto: Mapa del Ecuador con Flask, MySQL, Docker y NGINX

Este proyecto despliega un sistema distribuido compuesto por:

- 2 servidores **Flask** que muestran un mapa interactivo del Ecuador.
- Una base de datos **MySQL** que almacena información de las provincias.
- Un **balanceador de carga NGINX** que distribuye el tráfico entre los servidores.
- Todo ejecutado con **Docker Compose**, usando **volúmenes** y **redes personalizadas**.

---

## 🚀 Tecnologías usadas

- 🐍 Flask (Python)
- 🐬 MySQL 5.7
- 🌐 Leaflet.js (mapas interactivos)
- 🐳 Docker + Docker Compose
- ⚖️ NGINX (balanceador de carga)
- 💾 Volúmenes de Docker

---

## 🗺️ ¿Qué muestra la app?

- Un mapa del Ecuador centrado con Leaflet y OpenStreetMap.
- Una lista de provincias con:
  - Nombre
  - Capital
  - Área (km²)
  - Población estimada

Los datos son consultados desde una base MySQL que se inicializa automáticamente al arrancar.

---
