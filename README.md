# 🔍 Buscador Inteligente de Archivos (Smart File Search)

Un script de Python ligero, rápido y sin dependencias diseñado para buscar palabras o frases exactas **dentro** del contenido de múltiples archivos de texto de forma simultánea. Ideal para desarrolladores, auditores o cualquier usuario que necesite escanear grandes volúmenes de texto.

## ✨ Características Principales

* **Búsqueda Interna Profunda:** Escanea el contenido real de los archivos, no solo sus nombres.
* **🌍 Interfaz Multilenguaje Nativa:** Menú dinámico disponible en **Español, Inglés, Ruso y Klingon (tlhIngan Hol)**. El idioma se puede cambiar en caliente desde el menú principal.
* **🎯 Filtros Precisos:** Limita tu búsqueda definiendo la carpeta raíz, extensiones específicas (ej. `.txt, .py, .log`) y palabras obligatorias en el nombre del archivo.
* **📖 Contexto Inteligente:** Permite imprimir las líneas de texto inmediatamente antes y después de la coincidencia para entender el contexto sin abrir el archivo original.
* **💾 Gestor de Perfiles:** Guarda tus parámetros de búsqueda recurrentes y cárgalos rápidamente en futuras sesiones.
* **📤 Exportación de Resultados:** Guarda todo el reporte de coincidencias y su contexto en un archivo `.txt` limpio para su revisión posterior.
* **📦 Cero Dependencias:** Construido exclusivamente con librerías estándar de Python (`os`, `sys`, `json`, `re`). Funciona en Windows, Linux, macOS y Android (vía Termux/Pydroid).

## 🚀 Requisitos e Instalación

Lo único que necesitas es tener **Python 3.6+** instalado en tu sistema. No hace falta instalar paquetes mediante `pip`.

1. Clona este repositorio o descarga el archivo `busca.py`:
   ```bash
   git clone https://github.com/asesoriaogam-collab/py-interactive-grep.git
   ```
2. Navega hasta la carpeta del proyecto:
   ```bash
   cd nombre-del-repo
   ```
3. Ejecuta el script:
   ```bash
   python busca.py
   ```

## 🛠️ Uso Básico

Al ejecutar el script, te recibirá un menú interactivo en la consola:

1. **Configuración:** Aquí puedes definir la carpeta a escanear, las extensiones (por defecto `.txt`), activar el contexto y gestionar tus perfiles.
2. **Iniciar búsqueda:** Arranca el motor de búsqueda pidiéndote la palabra o frase exacta a localizar.
3. **Selección de Idioma:** Te permite alternar la interfaz entre los idiomas disponibles al instante.
4. **Salir:** Cierra la aplicación de forma segura.

### 💡 Ejemplo de Flujo de Trabajo
* Entras a Configuración -> Defines buscar en extensiones `.log` y activas 2 líneas de contexto.
* Inicias búsqueda -> Buscas la palabra `ERROR`.
* El script te mostrará exactamente en qué archivos `.log` ocurrió y te imprimirá las dos líneas de código antes y después de cada error para que entiendas qué pasó.
* Al final, exportas los resultados a `reporte_errores.txt`.

## 🤝 Contribuciones
¡Las contribuciones son bienvenidas! Si deseas agregar un nuevo idioma al diccionario integrado, mejorar el algoritmo de búsqueda o arreglar un bug, siéntete libre de hacer un *Fork* del proyecto y enviar un *Pull Request*.

## 📄 Licencia
Este proyecto está bajo la Licencia MIT - mira el archivo [LICENSE](LICENSE) para más detalles.
