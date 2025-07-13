# 🌌 Stellar Horizon

**Stellar Horizon** es una aplicación web desarrollada con Django y Django REST Framework que simula un sistema de turismo espacial con planetas, actividades, tours, alojamientos, usuarios, reservas y más.

---

## 🧰 Tecnologías usadas

- Python 3.8+
- Django 4.0
- Django REST Framework 3.13.1
- JWT (djangorestframework-simplejwt)
- drf-spectacular (documentación Swagger)
- Pillow (para el manejo de imágenes)
- django-environ (variables de entorno)
- django-cors-headers (CORS)
- django-filter

---

## ⚙️ Instalación paso a paso

### 1. Clona el repositorio

```bash
git https://github.com/JemPak/intergalactic-travel-management
cd intergalactic-travel-management
# Crear ambiente virtual
python -m venv env/
# Activar ambiente virtual
source env/bin/activate
# Instalar librerias
pip install -r requirements.txt
cd star_wars
# Ejecutar comando para levantar el proyecto
python manage.py runserver
# Acceder al admin para visualizar los modelos
localhost:8000/admin/
email: admin@unal.edu.co
pass: admin1234
# Acceder al swagger para ver la documentación de los endpoints
localhost:8000/swagger/
