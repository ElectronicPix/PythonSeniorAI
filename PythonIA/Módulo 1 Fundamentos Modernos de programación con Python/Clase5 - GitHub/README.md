# Git y Github

Sitema de control de versiones y colaboración en el desarollo de software

* Registro de cambios
* Colaboración 
* Control de versiones

## ¿Que es Git?

Git es un sistema de control de versiones distribuido, creado por Linus Torvalds en 2005. Permite a los desarrolladores gestionar el historial de cambios de su código, colaborar en equipo y experimentar de forma segura. Git almacena todo el historial de un proyecto y permite crear ramas para desarrollar nuevas funcionalidades sin afectar la versión principal.


## ¿Que es git Hub?
GitHub es una plataforma web que utiliza Git como base para el control de versiones. Permite alojar repositorios en la nube, colaborar con otros desarrolladores, gestionar proyectos y contribuir a proyectos de código abierto. GitHub añade herramientas sociales y de gestión que potencian el trabajo en equipo.


* Repositorio en la nube
* Colaboración
* Gestión de Proyectos
* Integración continua


(render) despliegue de aplicaciones 


## Repositorio

Almacenar la información a travez de github usando comandos.


* push: Es la acción de enviar los commits (cambios) desde tu repositorio local al repositorio remoto. En otras palabras, es cómo subes tus cambios a la nube.

* Publish Branch: (publicar rama) Es la acción de enviar una rama de tu repositorio local al repositorio remoto. Cuando trabajas en una rama nueva, esta solo existe en tu máquina; al publicarla, la pones a disposición de tus colaboradores en el repositorio central.

Repoitorio: Privado - Publico 

* Pull: Es la acción de descargar y fusionar los cambios más recientes del repositorio remoto a tu repositorio local. Es la forma en que obtienes las actualizaciones de tus compañeros y mantienes tu copia al día.


** Comandos:

git config --global user.name "Nombre"
git config --global user.email "tu@ejemplo.com"
git config --global --list


clonar repositorio: git clone   
git clone URL_del_repositorio


Tarea: **Miniproyecto en python Sistema de gestión de inventario**


Un **fork** es una copia de un repositorio que se crea en tu propia cuenta de GitHub, GitLab o Bitbucket. 🍴 Piénsalo como una ramificación de un proyecto. Cuando haces un fork, no estás copiando el proyecto a tu máquina local, sino creando un nuevo repositorio remoto bajo tu control. Esto te permite experimentar, hacer cambios y contribuir al proyecto original sin afectar directamente el código principal. Los forks son esenciales para el desarrollo de código abierto, ya que proporcionan una forma segura de proponer cambios y mejoras.

¿Cuándo usar un Fork?
Para contribuir a un proyecto de código abierto: Si quieres proponer un cambio, una mejora o corregir un error en un proyecto del que no eres colaborador, primero debes hacer un fork. Después de hacer tus cambios en tu repositorio forkeado, puedes enviar una pull request al repositorio original para que tus cambios sean considerados.

Para experimentar con un proyecto: Si solo quieres jugar con el código de un proyecto o usarlo como base para un nuevo proyecto tuyo, un fork es la mejor opción, ya que te da total libertad sin impactar el proyecto original.

A diferencia de un fork, un **clone** es una copia exacta de un repositorio que se descarga de forma local a tu computadora. 💻 Es la acción que usas para obtener una versión funcional de un proyecto en tu máquina para poder trabajar en él. Cuando clonas un repositorio, obtienes todo el historial de commits, todas las ramas y los archivos del proyecto, creando una conexión directa con el repositorio remoto original.

¿Cuándo usar un Clone?
Para comenzar a trabajar en un proyecto: Si eres un colaborador o desarrollador en un proyecto, lo clonas para poder trabajar directamente en él desde tu máquina.

Para obtener una copia local de un repositorio: Ya sea un repositorio que creaste tú, uno forkeado o uno del que eres colaborador, necesitas clonarlo para poder editar archivos, crear ramas y hacer commits.


**Como Inicar el proyecto**

