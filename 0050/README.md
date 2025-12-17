# Solicitudes HTTP con Requests (12/20)
[Solicitudes HTTP con Requests](https://platzi.com/cursos/python-pip/solicitudes-http-con-requests/)
# Entorno virtual con uv
## Crear entorno virtual para web-server
**Verificar version de uv**
```:bash
uv --version
```
**Inicializar proyecto**
```:bash
uv init
```
**Crear entorno virtual**
```:bash
uv venv
```
**Activar entorno virtual**
```:bash
.venv\Scripts\activate
```
**Instalar requests**
```:bash
uv add requests
```
**Generar el requirements.txt**
```:bash
uv lock
```
## Usar api fakeplatzi
[store.py](web-server/store.py)

# Pandas (13/20)
[Pandas](https://platzi.com/cursos/python-pip/pandas/)

# Python para Backend: web server con FastAPI
[Python para Backend: web server con FastAPI](https://platzi.com/cursos/python-pip/python-para-backend-web-server-con-fastapi/)
**Instalar fastapi y uvicorn**
```:bash
uv add fastapi
```
```:bash
uv add uvicorn
```
**Iniciar servidor con uvicorn**
```:bash
uvicorn main:app --reload
```
**Documentación FastAPI**
[FastAPI](https://fastapi.tiangolo.com/)
**Documentación Uvicorn**
[Uvicorn](https://www.uvicorn.org/)

**Responder HTML**

# ¿Qué es Docker?
[¿Qué es Docker?](https://platzi.com/cursos/python-pip/que-es-docker/)

# Dockerizando web services
[Dockerizando web services](https://platzi.com/cursos/python-pip/dockerizando-web-services/)

```
docker-compose build
docker-compose up -d
docker-compose ps
docker-compose down
```