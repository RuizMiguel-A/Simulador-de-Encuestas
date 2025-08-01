---
# 📝 Simulador de Encuestas

## 📌 Descripción del Proyecto

El módulo **Simulador de Encuestas** permite a los usuarios crear encuestas simples, responderlas y visualizar los resultados en tiempo real. Esta aplicación está diseñada para facilitar la recolección de opiniones de manera eficiente y organizada, almacenando las respuestas en formato **JSON** o base de datos.

El sistema proporciona una interfaz intuitiva para gestionar preguntas y opciones, así como una visualización clara de los resultados mediante **porcentajes**.

---

### 🔧 Funcionalidades Principales:

* Crear encuestas con múltiples preguntas y opciones de respuesta.
* Responder encuestas de forma dinámica.
* Almacenar las respuestas en formato JSON o en base de datos.
* Mostrar resultados de las encuestas en forma de porcentajes visuales.
* Interfaz moderna y adaptable a distintos dispositivos.

📸 *(Imagen de referencia del formulario + resultados con porcentajes)*

---

## 👥 Integrantes y Roles del Equipo

| Rol                 | Nombre            |
| ------------------- | ------------------|
| Scrum Master        | Cesar Martel      |
| Product Owner       | Felix Torre       |
| Developer Front-end | Sebastian Rosas   |
| Developer Apoyo     | Nicolaz Meza      |
| Developer Back-end  | Miguel Ruiz       |

---

## 🛠️ Instalación del Proyecto

### Requisitos:

* Python 3.10 o superior
* Django 4.x
* Git

### Pasos de Instalación:

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/RuizMiguel-A/Simulador-de-Encuestas
   ```

2. **Crea y activa un entorno virtual:**

   ```bash
   python -m venv .env
   source .env/bin/activate    # En Linux/Mac
   .env\Scripts\activate       # En Windows
   ```

3. **Instala las dependencias:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Aplica las migraciones:**

   ```bash
   python manage.py migrate
   ```

5. **Ejecuta el servidor:**

   ```bash
   python manage.py runserver
   ```

---

## 📋 Historias de Usuario

Aquí se detallan las funcionalidades principales del simulador desde la perspectiva del usuario.

### 🧩 **H1: Crear Encuestas**

**Como administrador**, quiero crear encuestas con preguntas y múltiples opciones, para poder recolectar información de forma estructurada.

#### Criterios de Aceptación:

* Permite ingresar título, preguntas y opciones.
* Mínimo una pregunta por encuesta.
* Cada pregunta debe tener al menos dos opciones válidas.
* Guarda la encuesta en JSON o base de datos.
* Muestra mensaje de confirmación al guardar.

⏳ *Estado:* `Completo`

---

### 🧩 **H2: Responder Encuestas**

**Como usuario**, quiero poder seleccionar una opción por pregunta y enviar mis respuestas, para participar activamente en las encuestas.

#### Criterios de Aceptación:

* Las respuestas se guardan correctamente.
* Se impide el envío si no se responde a todas las preguntas.
* Al finalizar, se muestra mensaje de agradecimiento.

⏳ *Estado:* `Completo`

---

### 🧩 **H3: Visualizar Resultados**

**Como usuario**, quiero ver los resultados en porcentajes luego de responder, para interpretar de manera rápida las tendencias de cada encuesta.

#### Criterios de Aceptación:

* Resultados por opción mostrados con barra de progreso o gráfico.
* El total de votos y porcentaje por opción se actualiza dinámicamente.
* No se permite votar nuevamente en la misma sesión.

⏳ *Estado:* `Completo`

---

## 🔧 Prácticas de Desarrollo y Metodología (XP & CI)

Este proyecto implementa las siguientes prácticas de desarrollo, esenciales para nuestra metodología ágil:

* **Test-Driven Development (TDD):** Al menos una funcionalidad clave ha sido desarrollada utilizando TDD, escribiendo los tests *antes* de la implementación del código.
* **Pair Programming:** Se ha realizado Pair Programming en al menos una tarea significativa, con roles claros de Driver y Navigator, fomentando la colaboración y la calidad del código.
* **Refactorización:** Se ha identificado y refactorizado al menos un módulo del código, mejorando su estructura y mantenibilidad sin alterar su comportamiento funcional. Se documenta el "antes" y el "después" de la refactorización.
* **Gestión de Código con Git/GitHub:**
    * Utilizamos ramas `main` y al menos una rama de *feature* para gestionar el desarrollo.
    * Todos los `commits` incluyen autores claros.
    * Se realizan **Pull Requests (PRs)** reales, que son revisadas por al menos un compañero antes de la fusión.

---

## 🗂️ Estructura del Tablero Trello

El equipo utiliza **Trello** como tablero ágil para organizar el flujo de trabajo de acuerdo con la metodología Scrum. Nuestro tablero incluye las siguientes columnas principales para seguir el progreso de las tareas:

* **Product Backlog / Historias de Usuario:** Contiene todas las ideas y funcionalidades deseadas para el proyecto, priorizadas.
* **Sprint Goal:** Una tarjeta dedicada al objetivo claro y conciso del sprint actual.
* **Sprint Planning:** Actividades y decisiones tomadas durante la planificación del sprint.
* **Sprint Backlog / To Do:** Tareas y Historias de Usuario seleccionadas para el sprint actual, listas para ser iniciadas.
* **In Progress / Haciendo:** Tareas en las que el equipo está trabajando activamente.
* **Review / Revisión:** Tareas completadas y listas para ser inspeccionadas por otros miembros del equipo.
* **Done / Hecho:** Tareas y Historias de Usuario completamente terminadas y validadas.

El tablero también incluye:
* Etiquetas por prioridad.
* Asignación de tareas por rol.
* Documentación y checklists dentro de cada tarea.
* Se evidencian las reuniones Scrum (capturas o enlaces).

---

## 🔗 Accesos Directos

* 🧾 **Tablero Trello:**
    👉 [https://trello.com/invite/b/688abe36c4f85d147492dc61/ATTIc084b1bc30aefa12a0625c8594445b682262AC39/simuladordeencuesta]([https://trello.com/invite/b/688abe36c4f85d147492dc61/ATTIc084b1bc30aefa12a0625c8594445b682262AC39/simuladordeencuesta](https://trello.com/b/himkcePB/simuladordeencuesta))

* 💻 **Repositorio GitHub:**
    🔗 [https://github.com/RuizMiguel-A/Simulador-de-Encuestas](https://github.com/RuizMiguel-A/Simulador-de-Encuestas)

---
