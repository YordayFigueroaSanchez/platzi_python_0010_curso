- [Control de Versiones con Git y GitHub: De Básico a Avanzado](https://platzi.com/cursos/gitgithub/que-son-git-y-github/)

- [Control de Versiones con Git: Comandos Básicos y Flujo de Trabajo](https://platzi.com/cursos/gitgithub/comandos-basicos-de-git-add-commit-log/)

![alt text](image.png)

- [Gestión de ramas en Git: creación, fusión y eliminación eficiente](https://platzi.com/cursos/gitgithub/ramas-y-fusion-de-cambios-branch-merge-checkout/)
    git branch
    git branch test
    git checkout test
    git switch main
    git merge test
    git branch -D test

- [Git Reset vs Git Revert: Manejo de Historial y Corrección de Errores](https://platzi.com/cursos/gitgithub/volviendo-en-el-tiempo-en-git-reset-revert/)
    git reset --soft HEAD~1
    git reset --mixed HEAD~1
    git reset --hard HEAD~1
    git revert HEAD

- [Uso de Git Tag y Git Checkout para Gestión de Versiones y Revisión](https://platzi.com/cursos/gitgithub/gestion-de-versiones-con-tag-y-checkout/)
    - crear tag local
    git tag -a v1.0.0 -m "version 1.0.0"
    - listar tags
    git tag
    - mostrar tag
    git show v1.0.0
    - borrar tag local
    git tag -d v1.0.0
    - checkout a un commit
    git checkout 5c0e62ec0941286d223f7b998533a73f411608a5

- [Resolución de Conflictos de Ramas en Git paso a paso](https://platzi.com/cursos/gitgithub/resolucion-de-conflictos-en-git/)
    - resolver conflictos
    crear archivo `conflicto.txt`
    git checkout -b conflicto
    git add conflicto.txt
    git commit -m "agregar conflicto.txt"
    git checkout main
    git merge conflicto
    git status
    git diff
    git add conflicto.txt
    git commit -m "resolver conflictos"

- [Uso de Git en Visual Studio Code](https://platzi.com/cursos/gitgithub/usando-git-desde-vs-code/)
    - probar conflictos desde VSCode

- [Configuración de SSH en GitHub para Windows, Linux y Mac](https://platzi.com/cursos/gitgithub/configuracion-de-llaves-ssh/)
    - generar llave ssh
    ssh-keygen -t ed25519 -C "mail@example.com"
    - agregar llave ssh a github
    ssh-add ~/.ssh/id_ed25519
    - clonar repositorio
    git clone git@github.com:username/repository.git

- [Configuración de Proyectos de Software con Git y GitHub](https://platzi.com/cursos/gitgithub/importancia-de-los-pull-requests-y-ramas-en-github/)
```
uv pip install -r .\0030-api\requirements.txt
uvicorn app:app --reload
```

- Pendiente la clase de release y paquetes

- [Certificación - Curso de Git y GitHub](https://platzi.com/clases/examen/e1907be5-f4a2-4d34-a5d4-adba8083da13/examen_usuario/)
1. ¿Qué comando usarías para clonar un repositorio desde GitHub a tu máquina local?
    - `git clone `
2. ¿Qué comando permite añadir todos los cambios en el área de preparación en un solo paso?
    - `git add .`
3. Si deseas deshacer el último commit pero mantener los cambios en el área de preparación, ¿qué comando usarías?
    - `git reset --soft HEAD~1`
4. ¿Para qué se usa `git stash` en Git?
    - Guardar temporalmente los cambios sin hacer commit
5. ¿Cuál comando fusionaría todos los commits en uno solo antes de enviarlos al remoto?
    - `git rebase -i HEAD~`
6. ¿Qué diferencia hay entre `git reset --hard` y `git reset --soft`?
    - `git reset --hard` elimina los cambios, mientras que `git reset --soft` los mantiene en staging
7. ¿Qué sucede si intentas hacer `push` sin permisos en el repositorio remoto?
    - La operación es rechazada con un mensaje de error
8. Si deseas ver los archivos modificados desde el último commit, ¿qué comando utilizarías?
    - `git status`
9. ¿Qué significa el mensaje de error 'merge conflict' en Git?
    - Dos ramas tienen cambios en la misma línea de un archivo
10. Si deseas eliminar una rama local que ya no necesitas, ¿qué comando utilizas?
    - `git branch -d `
11. ¿Qué archivo se suele usar en GitHub Pages para configurar el sitio?
    - `_config.yml`
12. Si quieres habilitar GitHub Pages en un repositorio, ¿dónde configuras el origen del contenido?
    - En la configuración de GitHub Pages del repositorio
13. ¿Cuál es el propósito de una Wiki en GitHub?
    - Documentar el proyecto para que los colaboradores tengan información detallada
14. Si deseas ver los archivos modificados desde el último commit, ¿qué comando utilizas?
    - `git status`
15. En GitHub Actions, ¿cómo se llama el archivo YAML que define un 'job' para ejecutar pruebas?
    - `.github/workflows/.yml`
