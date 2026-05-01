# Plan de Migración a Django + Vue.js

Este plan detalla los pasos necesarios para transformar nuestro MVP estático actual en una aplicación Full-Stack moderna. Al hacer esto, **Django** actuará como el cerebro (Backend) manejando la base de datos y la seguridad (incluyendo la conexión con NewsAPI), mientras que **Vue.js** se encargará de crear una interfaz interactiva y dinámica (Frontend).

## > [!IMPORTANT] User Review Required

Antes de comenzar a programar, necesito que apruebes este enfoque arquitectónico. Existen dos formas comunes de unir Django y Vue:
1. **Arquitectura Desacoplada (Recomendada):** El backend (Django) y el frontend (Vue) son proyectos separados. Django funciona puramente como una API (JSON), y Vue consume esa API. Es el estándar de la industria y la mejor opción para escalar.
2. **Arquitectura Híbrida:** Vue se incrusta dentro de las plantillas HTML (Templates) tradicionales de Django.

**El plan a continuación asume la Arquitectura Desacoplada (Opción 1)** por ser la más robusta y moderna. Por favor, confirma si estás de acuerdo con esta ruta en tu respuesta.

## Open Questions

> [!WARNING] Prerrequisitos del Sistema
> Para ejecutar la migración, tu computadora (Windows) debe tener instalados:
> 1. **Python** (Para Django)
> 2. **Node.js y npm** (Para instalar y compilar Vue.js)
> ¿Tienes instaladas estas herramientas actualmente? Si no es así, el primer paso será instalarlas.

## Proposed Changes

La estructura del proyecto cambiará radicalmente. En la carpeta `c:\workspace\sitio-web-curumani` tendremos dos carpetas principales: `/backend` (Django) y `/frontend` (Vue).

---

### Backend (Django)

Se creará el proyecto base y una API para exponer los datos y solucionar el problema de NewsAPI.

#### [NEW] `backend/manage.py` y configuración base
- Creación del proyecto Django.
- Configuración de `Django REST Framework` y `django-cors-headers`.

#### [NEW] `backend/api/models.py`
- Modelos de base de datos reales para reemplazar `negocios.js` y `eventos.js`:
  - `Negocio` (Nombre, Categoría, Dirección, Teléfono, Horario, Lat, Lng)
  - `Evento` (Título, Fecha de inicio, Fecha de fin, Color)

#### [NEW] `backend/api/views.py`
- Endpoints (URLs) para exponer los negocios y eventos a Vue.
- **Solución NewsAPI:** Un endpoint propio (ej. `/api/news/`) que utilizará tu llave de NewsAPI (`e9707b96692d4e51b5340afdb151c8c4`) para hacer la petición desde el servidor. Como el servidor no tiene restricciones CORS, la petición siempre será exitosa.

---

### Frontend (Vue 3 + Vite)

Migraremos tu actual HTML y Javascript puro a componentes reutilizables de Vue.js.

#### [NEW] `frontend/package.json`
- Inicialización de Vue 3.
- Instalación de dependencias formales: `tailwindcss`, `three`, `leaflet`, `fullcalendar`, y `axios`.

#### [NEW] `frontend/src/App.vue`
- El componente raíz que orquestará la página, reemplazando el esqueleto general de tu actual `index.html`.

#### [NEW] Componentes de Vue (`frontend/src/components/`)
- `HeroHeader.vue`: Contendrá la animación Three.js y el botón principal.
- `NewsSection.vue`: Hará la petición al backend de Django para obtener las noticias.
- `DirectoryMap.vue`: Inicializará Leaflet.js y consumirá los negocios de la base de datos de Django.
- `CommunityCalendar.vue`: Inicializará FullCalendar.js con los eventos de la base de datos de Django.

#### [DELETE] Archivos Antiguos
- Una vez la migración esté completada y probada, eliminaremos la estructura estática antigua (`index.html`, `/js`, `/css`, `/data`) para mantener el repositorio limpio.

## Verification Plan

### Automated Tests
- Se verificarán que los endpoints de Django devuelvan código HTTP `200 OK` con datos JSON estructurados correctamente.
- Se verificará que el servidor de Vite compile Vue sin errores de dependencias.

### Manual Verification
- Te pediré que ejecutes ambos servidores localmente (te daré los comandos precisos) para visualizar la página en tu navegador.
- Validaremos que el mapa (Leaflet), la animación 3D (Three.js) y el calendario interactivo se rendericen correctamente en su versión de componentes Vue.
- Validaremos la carga exitosa de las noticias a través del puente (Proxy seguro) creado en el backend de Django, confirmando que el error de CORS ha desaparecido permanentemente.
