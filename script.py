import os
import sys
import json
import re

# Habilitar soporte para secuencias de color ANSI en la consola de Windows
os.system('')

# Constantes de colores ANSI para la consola
COLOR_AMARILLO = "\033[93m"
COLOR_RESET = "\033[0m"

# Carpetas pesadas que ignoramos para mantener la velocidad
CARPETAS_A_IGNORAR = {'.git', 'node_modules', '__pycache__', '.vscode', 'appdata', 'program files'}

VALORES_POR_DEFECTO = {
    "carpeta_raiz": ".",
    "extensiones": [".txt"],
    "filtro_nombre": "",
    "mostrar_contexto": False,
    "lineas_antes": 0,
    "lineas_despues": 0,
    "nombre_perfil": "Valores por defecto",
    "idioma": "es"
}

# ==========================================
# DICCIONARIO DE TRADUCCIONES
# ==========================================
NOMBRES_IDIOMA = {
    "es": "Idioma",
    "en": "Language",
    "ru": "Язык",
    "tlh": "Hol"
}

TEXTOS = {
    "es": {
        "title_main": "BUSCADOR INTELIGENTE DE ARCHIVOS",
        "opt_config": "Configuración",
        "opt_search": "Iniciar búsqueda",
        "opt_exit": "Salir",
        "val_default": "valores por defecto",
        "val_custom": "Personalizada",
        "select_opt": "> Selecciona una opción",
        "exit_msg": "👋 ¡Gracias por usar el buscador! Saliendo...",
        "title_lang": "SELECCIÓN DE IDIOMA",
        "lang_es": "Español",
        "lang_en": "Inglés (English)",
        "lang_ru": "Ruso (Русский)",
        "lang_tlh": "Klingon (tlhIngan Hol)",
        "back_main": "Volver al Menú Principal",
        "title_config": "SUBMENÚ DE CONFIGURACIÓN",
        "status_curr": "ESTADO ACTUAL",
        "base_folder": "Carpeta base",
        "extensions": "Extensiones",
        "name_filter": "Filtro de nombre",
        "context_lines": "Líneas contexto",
        "activated": "Activado",
        "deactivated": "Desactivado",
        "before": "antes",
        "after": "después",
        "none": "Ninguno",
        "c_opt_1": "Cambiar ruta de la carpeta base",
        "c_opt_2": "Cambiar extensiones de archivo",
        "c_opt_3": "Cambiar filtro por nombre de archivo",
        "c_opt_4": "Configurar líneas de contexto",
        "c_opt_5": "Cargar un perfil guardado",
        "c_opt_6": "Guardar configuración actual como perfil",
        "c_opt_7": "Volver al Menú Principal",
        "in_folder": "Introduce la ruta de la carpeta base:",
        "in_exts": "Introduce las extensiones separadas por comas (ej: .txt, .log):",
        "in_filter": "Introduce la palabra o frase que DEBE contener el nombre del archivo (ENTER para ninguno):",
        "in_context": "¿Deseas activar líneas de contexto? (s/n):",
        "in_before": "↳ Líneas ANTES de la coincidencia (Por defecto: 3):",
        "in_after": "↳ Líneas DESPUÉS de la coincidencia (Por defecto: 3):",
        "title_load": "CARGAR PERFIL GUARDADO",
        "no_profiles": "⚠ No hay perfiles guardados actualmente.",
        "press_enter": "Presiona ENTER para continuar...",
        "cancel": "Cancelar",
        "sel_profile_load": "> Selecciona el número del perfil a cargar:",
        "profile_loaded": "✅ Perfil '{}' cargado con éxito.",
        "title_save": "GUARDAR CONFIGURACIÓN ACTUAL COMO PERFIL",
        "in_prof_name": "Introduce un nombre para este perfil:",
        "err_empty": "⚠ El nombre no puede estar vacío.",
        "warn_exists": "⚠ El perfil '{}' ya existe. ¿Deseas sobrescribirlo? (s/n):",
        "op_cancelled": "Operación cancelada.",
        "profile_saved": "✅ Perfil '{}' guardado con éxito.",
        "title_search": "INICIANDO BÚSQUEDA",
        "s_folder": "Carpeta",
        "s_filters": "Filtros",
        "s_name": "Nombre",
        "s_context": "Contexto",
        "in_term": "Introduce la PALABRA o FRASE a buscar DENTRO del texto (o ENTER para volver al menú):",
        "scanning": "Aplicando filtros y escaneando nombres...",
        "no_files": "⚠ No se encontraron archivos que coincidan con la extensión y el filtro de nombre indicados.",
        "searching": "Buscando... {}% ({}/{} archivos)",
        "summary": "RESUMEN DE LA BÚSQUEDA:",
        "sum_term": "Término buscado por dentro",
        "sum_filter": "Filtro de nombre aplicado",
        "sum_all": "Ninguno (todos)",
        "sum_yes": "Sí",
        "sum_times": "Total de veces encontrado",
        "sum_files": "Encontrado en archivos distintos",
        "sum_scanned": "Total archivos analizados",
        "p_opt_1": "Buscar otra palabra o frase (misma configuración)",
        "p_opt_2": "Exportar resultados a un archivo (.txt)",
        "p_opt_3": "Volver al Menú Principal",
        "no_results_exp": "⚠ No hay resultados para exportar.",
        "in_exp_name": "Introduce el nombre para el archivo (ej: resultados):",
        "exp_success": "✅ Resultados exportados exitosamente en '{}'.",
        "exp_err": "❌ Error al guardar el archivo: {}"
    },
    "en": {
        "title_main": "SMART FILE SEARCH",
        "opt_config": "Configuration",
        "opt_search": "Start search",
        "opt_exit": "Exit",
        "val_default": "default values",
        "val_custom": "Custom",
        "select_opt": "> Select an option",
        "exit_msg": "👋 Thanks for using the search tool! Exiting...",
        "title_lang": "LANGUAGE SELECTION",
        "lang_es": "Spanish (Español)",
        "lang_en": "English",
        "lang_ru": "Russian (Русский)",
        "lang_tlh": "Klingon (tlhIngan Hol)",
        "back_main": "Back to Main Menu",
        "title_config": "CONFIGURATION SUBMENU",
        "status_curr": "CURRENT STATUS",
        "base_folder": "Base folder",
        "extensions": "Extensions",
        "name_filter": "Name filter",
        "context_lines": "Context lines",
        "activated": "Activated",
        "deactivated": "Deactivated",
        "before": "before",
        "after": "after",
        "none": "None",
        "c_opt_1": "Change base folder path",
        "c_opt_2": "Change file extensions",
        "c_opt_3": "Change filename filter",
        "c_opt_4": "Configure context lines",
        "c_opt_5": "Load saved profile",
        "c_opt_6": "Save current configuration as profile",
        "c_opt_7": "Back to Main Menu",
        "in_folder": "Enter base folder path:",
        "in_exts": "Enter extensions separated by commas (e.g., .txt, .log):",
        "in_filter": "Enter word/phrase the filename MUST contain (ENTER for none):",
        "in_context": "Enable context lines? (y/n):",
        "in_before": "↳ Lines BEFORE match (Default: 3):",
        "in_after": "↳ Lines AFTER match (Default: 3):",
        "title_load": "LOAD SAVED PROFILE",
        "no_profiles": "⚠ No saved profiles currently.",
        "press_enter": "Press ENTER to continue...",
        "cancel": "Cancel",
        "sel_profile_load": "> Select profile number to load:",
        "profile_loaded": "✅ Profile '{}' loaded successfully.",
        "title_save": "SAVE CURRENT CONFIGURATION AS PROFILE",
        "in_prof_name": "Enter a name for this profile:",
        "err_empty": "⚠ Name cannot be empty.",
        "warn_exists": "⚠ Profile '{}' already exists. Overwrite? (y/n):",
        "op_cancelled": "Operation cancelled.",
        "profile_saved": "✅ Profile '{}' saved successfully.",
        "title_search": "STARTING SEARCH",
        "s_folder": "Folder",
        "s_filters": "Filters",
        "s_name": "Name",
        "s_context": "Context",
        "in_term": "Enter WORD or PHRASE to search INSIDE the text (or ENTER to return):",
        "scanning": "Applying filters and scanning names...",
        "no_files": "⚠ No files found matching the extension and name filter.",
        "searching": "Searching... {}% ({}/{} files)",
        "summary": "SEARCH SUMMARY:",
        "sum_term": "Search term",
        "sum_filter": "Name filter applied",
        "sum_all": "None (all)",
        "sum_yes": "Yes",
        "sum_times": "Total matches found",
        "sum_files": "Found in distinct files",
        "sum_scanned": "Total files scanned",
        "p_opt_1": "Search another word/phrase (same config)",
        "p_opt_2": "Export results to a file (.txt)",
        "p_opt_3": "Back to Main Menu",
        "no_results_exp": "⚠ No results to export.",
        "in_exp_name": "Enter filename (e.g., results):",
        "exp_success": "✅ Results exported successfully to '{}'.",
        "exp_err": "❌ Error saving file: {}"
    },
    "ru": {
        "title_main": "УМНЫЙ ПОИСК ФАЙЛОВ",
        "opt_config": "Настройки",
        "opt_search": "Начать поиск",
        "opt_exit": "Выход",
        "val_default": "по умолчанию",
        "val_custom": "Пользовательская",
        "select_opt": "> Выберите опцию",
        "exit_msg": "👋 Спасибо за использование! Выход...",
        "title_lang": "ВЫБОР ЯЗЫКА",
        "lang_es": "Испанский (Español)",
        "lang_en": "Английский (English)",
        "lang_ru": "Русский (Русский)",
        "lang_tlh": "Клингонский (tlhIngan Hol)",
        "back_main": "Вернуться в Главное Меню",
        "title_config": "ПОДМЕНЮ НАСТРОЕК",
        "status_curr": "ТЕКУЩЕЕ СОСТОЯНИЕ",
        "base_folder": "Базовая папка",
        "extensions": "Расширения",
        "name_filter": "Фильтр имени",
        "context_lines": "Строки контекста",
        "activated": "Включено",
        "deactivated": "Отключено",
        "before": "до",
        "after": "после",
        "none": "Нет",
        "c_opt_1": "Изменить путь к базовой папке",
        "c_opt_2": "Изменить расширения файлов",
        "c_opt_3": "Изменить фильтр по имени",
        "c_opt_4": "Настроить строки контекста",
        "c_opt_5": "Загрузить сохраненный профиль",
        "c_opt_6": "Сохранить настройки как профиль",
        "c_opt_7": "Вернуться в Главное Меню",
        "in_folder": "Введите путь к базовой папке:",
        "in_exts": "Введите расширения через запятую (напр: .txt, .log):",
        "in_filter": "Слово/фраза в имени файла (ENTER для пропуска):",
        "in_context": "Включить строки контекста? (y/n/д/н):",
        "in_before": "↳ Строки ДО совпадения (По умолчанию: 3):",
        "in_after": "↳ Строки ПОСЛЕ совпадения (По умолчанию: 3):",
        "title_load": "ЗАГРУЗИТЬ ПРОФИЛЬ",
        "no_profiles": "⚠ Нет сохраненных профилей.",
        "press_enter": "Нажмите ENTER для продолжения...",
        "cancel": "Отмена",
        "sel_profile_load": "> Выберите номер профиля для загрузки:",
        "profile_loaded": "✅ Профиль '{}' успешно загружен.",
        "title_save": "СОХРАНИТЬ ПРОФИЛЬ",
        "in_prof_name": "Введите имя для этого профиля:",
        "err_empty": "⚠ Имя не может быть пустым.",
        "warn_exists": "⚠ Профиль '{}' уже существует. Перезаписать? (y/n):",
        "op_cancelled": "Операция отменена.",
        "profile_saved": "✅ Профиль '{}' успешно сохранен.",
        "title_search": "НАЧАЛО ПОИСКА",
        "s_folder": "Папка",
        "s_filters": "Фильтры",
        "s_name": "Имя",
        "s_context": "Контекст",
        "in_term": "Введите СЛОВО или ФРАЗУ для поиска ВНУТРИ текста (или ENTER для возврата):",
        "scanning": "Применение фильтров и сканирование...",
        "no_files": "⚠ Файлы не найдены.",
        "searching": "Поиск... {}% ({}/{} файлов)",
        "summary": "РЕЗУЛЬТАТЫ ПОИСКА:",
        "sum_term": "Искомое слово",
        "sum_filter": "Примененный фильтр",
        "sum_all": "Нет (все)",
        "sum_yes": "Да",
        "sum_times": "Всего совпадений",
        "sum_files": "Найдено в различных файлах",
        "sum_scanned": "Всего файлов",
        "p_opt_1": "Искать другое слово (с теми же настройками)",
        "p_opt_2": "Экспортировать результаты в файл (.txt)",
        "p_opt_3": "Вернуться в Главное Меню",
        "no_results_exp": "⚠ Нет результатов для экспорта.",
        "in_exp_name": "Введите имя файла (напр: результаты):",
        "exp_success": "✅ Результаты успешно экспортированы в '{}'.",
        "exp_err": "❌ Ошибка при сохранении файла: {}"
    },
    "tlh": {
        "title_main": "TEYWI' NEJWI' (FILE SEARCH)",
        "opt_config": "QapmeH wIvmey (Config)",
        "opt_search": "nej (Start search)",
        "opt_exit": "mej (Exit)",
        "val_default": "wIqelchu'ta' (Defaults)",
        "val_custom": "tIgh (Custom)",
        "select_opt": "> wIma' (Select an option)",
        "exit_msg": "👋 Qapla'! mejtaH... (Exiting...)",
        "title_lang": "HOL WIMA' (LANGUAGE)",
        "lang_es": "Spanish (Español)",
        "lang_en": "English (Inglés)",
        "lang_ru": "Russian (Русский)",
        "lang_tlh": "tlhIngan Hol (Klingon)",
        "back_main": "chegh (Back to Main Menu)",
        "title_config": "QAPMEH WIVMEY (CONFIGURATION)",
        "status_curr": "DAH (CURRENT STATUS)",
        "base_folder": "teywi' pa' (Folder)",
        "extensions": "teywi' pong Deghmey Qav (Extensions)",
        "name_filter": "teywi' pong NgaSnISbogh (Name filter)",
        "context_lines": "DungDaq bIngDaq je tu'lu'bogh tlheghmey (Context lines)",
        "activated": "Qaw' (Activated)",
        "deactivated": "Qaw'Ha' (Deactivated)",
        "before": "qaS (before)",
        "after": "pIq (after)",
        "none": "pagh (None)",
        "c_opt_1": "teywi' pa' choH (Change folder)",
        "c_opt_2": "teywi' pong Deghmey Qav choH (Change extensions)",
        "c_opt_3": "teywi' pong NgaSnISbogh choH (Change filter)",
        "c_opt_4": "DungDaq bIngDaq je tu'lu'bogh tlheghmey choH (Context lines)",
        "c_opt_5": "ta'mey lIgh (Load profile)",
        "c_opt_6": "ta'mey pol (Save profile)",
        "c_opt_7": "chegh (Back to Main Menu)",
        "in_folder": "teywi' pa' chaw' yIghItlh (Enter folder path):",
        "in_exts": "teywi' pong Deghmey Qav yIghItlh (Enter extensions):",
        "in_filter": "teywi' pong NgaSnISbogh yIghItlh (Enter name filter):",
        "in_context": "DungDaq bIngDaq je tu'lu'bogh tlheghmey yIQaw'? (HIja'/ghobe') (Context? y/n):",
        "in_before": "↳ qaS (BEFORE match):",
        "in_after": "↳ pIq (AFTER match):",
        "title_load": "TA'MEY LIGH (LOAD PROFILE)",
        "no_profiles": "⚠ ta'mey pagh (No profiles).",
        "press_enter": "ENTER yIqIp (Press ENTER)...",
        "cancel": "qIl (Cancel)",
        "sel_profile_load": "> wIma' (Select profile):",
        "profile_loaded": "✅ '{}' lIghpu'. (Loaded).",
        "title_save": "TA'MEY POL (SAVE PROFILE)",
        "in_prof_name": "pong yIghItlh (Enter profile name):",
        "err_empty": "⚠ pong chIm (Name empty).",
        "warn_exists": "⚠ '{}' tu'lu'. choH? (Overwrite? y/n):",
        "op_cancelled": "qIlpu' (Cancelled).",
        "profile_saved": "✅ '{}' polpu'. (Saved).",
        "title_search": "NEJ (SEARCHING)",
        "s_folder": "teywi' pa' (Folder)",
        "s_filters": "NgaSnISbogh (Filters)",
        "s_name": "pong (Name)",
        "s_context": "DungDaq bIngDaq je... (Context)",
        "in_term": "mu' yIghItlh (Enter SEARCH TERM or ENTER):",
        "scanning": "nejtaH... (Scanning...)",
        "no_files": "⚠ pagh tu'lu' (No files found).",
        "searching": "nej... {}% ({}/{} teywi')",
        "summary": "NEJ POQ (SUMMARY):",
        "sum_term": "mu' (Search term)",
        "sum_filter": "teywi' pong NgaSnISbogh (Filter)",
        "sum_all": "pagh (None)",
        "sum_yes": "HIja' (Yes)",
        "sum_times": "tu'lu' (Matches found)",
        "sum_files": "teywi' (In files)",
        "sum_scanned": "nejpu' (Files scanned)",
        "p_opt_1": "mu' pIm nej (Search another)",
        "p_opt_2": "pol (.txt) (Export)",
        "p_opt_3": "chegh (Back to Main Menu)",
        "no_results_exp": "⚠ pagh pol (No results to export).",
        "in_exp_name": "pong yIghItlh (Enter export name):",
        "exp_success": "✅ '{}' polpu' (Exported).",
        "exp_err": "❌ Qagh: {}"
    }
}

# Configuración activa global en memoria
config_activa = VALORES_POR_DEFECTO.copy()


def t(clave):
    """Obtiene el texto traducido según el idioma actual configurado."""
    idioma = config_activa.get("idioma", "es")
    return TEXTOS.get(idioma, TEXTOS["es"]).get(clave, clave)


def resaltar_coincidencia(texto, termino):
    """Reemplaza el término buscado dentro del texto por la versión en amarillo (case-insensitive)."""
    patron = re.compile(re.escape(termino), re.IGNORECASE)
    return patron.sub(lambda m: f"{COLOR_AMARILLO}{m.group(0)}{COLOR_RESET}", texto)


def es_configuracion_por_defecto(config):
    """Verifica si la configuración activa coincide exactamente con los valores predeterminados, omitiendo el idioma."""
    return (
        os.path.abspath(config["carpeta_raiz"]) == os.path.abspath(VALORES_POR_DEFECTO["carpeta_raiz"]) and
        config["extensiones"] == VALORES_POR_DEFECTO["extensiones"] and
        config["filtro_nombre"] == VALORES_POR_DEFECTO["filtro_nombre"] and
        config["mostrar_contexto"] == VALORES_POR_DEFECTO["mostrar_contexto"] and
        config["lineas_antes"] == VALORES_POR_DEFECTO["lineas_antes"] and
        config["lineas_despues"] == VALORES_POR_DEFECTO["lineas_despues"]
    )


# ==========================================
# GESTIÓN DE PERFILES Y CONFIGURACIÓN (JSON)
# ==========================================

def cargar_perfiles():
    if os.path.exists("perfiles.json"):
        try:
            with open("perfiles.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def guardar_perfiles(perfiles):
    with open("perfiles.json", "w", encoding="utf-8") as f:
        json.dump(perfiles, f, ensure_ascii=False, indent=4)


def menu_cargar_perfil():
    global config_activa
    perfiles = cargar_perfiles()

    if not perfiles:
        print(f"\n{t('no_profiles')}")
        input(t('press_enter'))
        return

    print("\n" + "="*50)
    print(f"      {t('title_load')}")
    print("="*50)
    nombres_perfiles = list(perfiles.keys())
    for idx, nombre in enumerate(nombres_perfiles, 1):
        print(f"{idx}. {nombre}")
    print(f"{len(nombres_perfiles) + 1}. {t('cancel')}")

    opcion = input(f"\n{t('sel_profile_load')} ").strip()
    if opcion.isdigit():
        idx_sel = int(opcion)
        if 1 <= idx_sel <= len(nombres_perfiles):
            nombre_sel = nombres_perfiles[idx_sel - 1]
            # Conservamos el idioma actual antes de cargar el perfil
            idioma_actual = config_activa.get("idioma", "es")
            config_activa = perfiles[nombre_sel].copy()
            config_activa["nombre_perfil"] = nombre_sel
            config_activa["idioma"] = config_activa.get("idioma", idioma_actual)
            print("\n" + t('profile_loaded').format(nombre_sel))
            input(t('press_enter'))


def menu_guardar_perfil():
    perfiles = cargar_perfiles()

    print("\n" + "="*50)
    print(f"   {t('title_save')}")
    print("="*50)
    nombre = input(f"{t('in_prof_name')} ").strip()

    if not nombre:
        print(t('err_empty'))
        input(t('press_enter'))
        return

    if nombre in perfiles:
        confirmar = input(f"{t('warn_exists').format(nombre)} ").strip().lower()
        if confirmar not in ['s', 'si', 'sí', 'y', 'yes', 'д', 'да']:
            print(t('op_cancelled'))
            input(t('press_enter'))
            return

    perfil_guardar = {
        "carpeta_raiz": config_activa["carpeta_raiz"],
        "extensiones": config_activa["extensiones"],
        "filtro_nombre": config_activa["filtro_nombre"],
        "mostrar_contexto": config_activa["mostrar_contexto"],
        "lineas_antes": config_activa["lineas_antes"],
        "lineas_despues": config_activa["lineas_despues"],
        "idioma": config_activa.get("idioma", "es")
    }

    perfiles[nombre] = perfil_guardar
    guardar_perfiles(perfiles)
    config_activa["nombre_perfil"] = nombre

    print("\n" + t('profile_saved').format(nombre))
    input(t('press_enter'))


# ==========================================
# MENÚ DE IDIOMA Y CONFIGURACIÓN
# ==========================================

def menu_idioma():
    global config_activa
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==================================================")
        print(t('title_lang').center(50))
        print("==================================================")
        print("1. " + t('lang_es'))
        print("2. " + t('lang_en'))
        print("3. " + t('lang_ru'))
        print("4. " + t('lang_tlh'))
        print("--------------------------------------------------")
        print("5. " + t('back_main'))
        print("--------------------------------------------------")

        opcion = input(f"{t('select_opt')} (1-5): ").strip()
        
        if opcion == "1":
            config_activa["idioma"] = "es"
            break
        elif opcion == "2":
            config_activa["idioma"] = "en"
            break
        elif opcion == "3":
            config_activa["idioma"] = "ru"
            break
        elif opcion == "4":
            config_activa["idioma"] = "tlh"
            break
        elif opcion == "5":
            break


def menu_configuracion():
    global config_activa

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==================================================")
        print(t('title_config').center(50))
        print("==================================================")
        
        perfil_txt = config_activa.get('nombre_perfil', t('val_custom'))
        print(f" {t('status_curr')}: [{perfil_txt}]")
        print(f" ↳ {t('base_folder')}:      {config_activa['carpeta_raiz']}")
        print(f" ↳ {t('extensions')}:       {', '.join(config_activa['extensiones'])}")
        
        f_nombre = config_activa['filtro_nombre'] if config_activa['filtro_nombre'] else f"({t('none')})"
        print(f" ↳ {t('name_filter')}:  {f_nombre}")
        
        if config_activa['mostrar_contexto']:
            context_txt = f"{t('activated')} ({config_activa['lineas_antes']} {t('before')} / {config_activa['lineas_despues']} {t('after')})"
        else:
            context_txt = f"{t('deactivated')} (0 {t('before')} / 0 {t('after')})"
        print(f" ↳ {t('context_lines')}:   {context_txt}")
            
        print("--------------------------------------------------")
        print(f"1. {t('c_opt_1')}")
        print(f"2. {t('c_opt_2')}")
        print(f"3. {t('c_opt_3')}")
        print(f"4. {t('c_opt_4')}")
        print(f"5. {t('c_opt_5')}")
        print(f"6. {t('c_opt_6')}")
        print(f"7. {t('c_opt_7')}")
        print("--------------------------------------------------")

        opcion = input(f"{t('select_opt')} (1-7): ").strip()

        if opcion == "1":
            nueva_ruta = input(f"\n{t('in_folder')}\n> ").strip().strip('"').strip("'")
            if nueva_ruta:
                config_activa["carpeta_raiz"] = nueva_ruta
                config_activa["nombre_perfil"] = t('val_custom')

        elif opcion == "2":
            print(f"\n{t('in_exts')}")
            ext_in = input("> ").strip()
            if ext_in:
                config_activa["extensiones"] = [ext.strip().lower() for ext in ext_in.split(",") if ext.strip()]
            else:
                config_activa["extensiones"] = [".txt"]
            config_activa["nombre_perfil"] = t('val_custom')

        elif opcion == "3":
            filtro = input(f"\n{t('in_filter')}\n> ").strip().lower()
            config_activa["filtro_nombre"] = filtro
            config_activa["nombre_perfil"] = t('val_custom')

        elif opcion == "4":
            resp = input(f"\n{t('in_context')}\n> ").strip().lower()
            if resp in ['s', 'si', 'sí', 'y', 'yes', 'д', 'да']:
                config_activa["mostrar_contexto"] = True
                cant_a = input(f"{t('in_before')}\n  > ").strip()
                config_activa["lineas_antes"] = int(cant_a) if cant_a.isdigit() else 3
                
                cant_d = input(f"{t('in_after')}\n  > ").strip()
                config_activa["lineas_despues"] = int(cant_d) if cant_d.isdigit() else 3
            else:
                config_activa["mostrar_contexto"] = False
                config_activa["lineas_antes"] = 0
                config_activa["lineas_despues"] = 0
            config_activa["nombre_perfil"] = t('val_custom')

        elif opcion == "5":
            menu_cargar_perfil()

        elif opcion == "6":
            menu_guardar_perfil()

        elif opcion == "7":
            break


# ==========================================
# MOTOR DE BÚSQUEDA Y EXPORTACIÓN
# ==========================================

def ejecutar_busqueda():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==================================================")
        print("🔍 " + t('title_search'))
        print(f"↳ {t('s_folder')}: {config_activa['carpeta_raiz']}")
        
        f_nom = config_activa['filtro_nombre'] if config_activa['filtro_nombre'] else f"({t('none')})"
        print(f"↳ {t('s_filters')}: {', '.join(config_activa['extensiones'])} | {t('s_name')}: {f_nom}")
        
        if config_activa['mostrar_contexto']:
            print(f"↳ {t('s_context')}: {config_activa['lineas_antes']} {t('before')} / {config_activa['lineas_despues']} {t('after')}")
        else:
            print(f"↳ {t('s_context')}: {t('deactivated')}")
        print("==================================================\n")

        texto_buscado = input(f"{t('in_term')}\n> ").strip()

        if not texto_buscado:
            break

        print("\n" + "🔍".center(50, "-"))
        print(t('scanning').center(50))
        print("-" * 50 + "\n")

        archivos_a_procesar = []
        for ruta_actual, subcarpetas, archivos in os.walk(config_activa["carpeta_raiz"]):
            subcarpetas[:] = [d for d in subcarpetas if d.lower() not in CARPETAS_A_IGNORAR]

            for nombre_archivo in archivos:
                nombre_lower = nombre_archivo.lower()
                if any(nombre_lower.endswith(ext) for ext in config_activa["extensiones"]):
                    if not config_activa["filtro_nombre"] or (config_activa["filtro_nombre"] in nombre_lower):
                        archivos_a_procesar.append(os.path.join(ruta_actual, nombre_archivo))

        total_archivos = len(archivos_a_procesar)

        if total_archivos == 0:
            print(t('no_files'))
            input("\n" + t('press_enter'))
            continue

        coincidencias_totales = 0
        archivos_con_coincidencias = 0
        archivos_revisados = 0

        lineas_exportar = []

        for i, ruta_completa in enumerate(archivos_a_procesar, 1):
            archivos_revisados += 1
            nombre_archivo = os.path.basename(ruta_completa)

            porcentaje = int((i / total_archivos) * 100)
            sys.stdout.write("\r" + t('searching').format(porcentaje, i, total_archivos))
            sys.stdout.flush()

            try:
                with open(ruta_completa, 'r', encoding='utf-8', errors='ignore') as archivo:
                    lineas = archivo.readlines()

                nombre_impreso = False
                hubo_coincidencia = False

                for index_linea, linea in enumerate(lineas):
                    if texto_buscado.lower() in linea.lower():

                        if not nombre_impreso:
                            sys.stdout.write("\r" + " " * 60 + "\r")
                            print(f"\n📂 {nombre_archivo}  ({os.path.abspath(ruta_completa)})\n" + "-"*60)
                            nombre_impreso = True
                            hubo_coincidencia = True
                        else:
                            print(f"\n   ...\n")

                        if config_activa["mostrar_contexto"]:
                            inicio = max(0, index_linea - config_activa["lineas_antes"])
                            fin = min(len(lineas), index_linea + config_activa["lineas_despues"] + 1)

                            for j in range(inicio, fin):
                                contenido_linea = lineas[j].rstrip('\n')
                                lineas_exportar.append(contenido_linea + "\n")
                                
                                if j == index_linea:
                                    print(f"    {resaltar_coincidencia(contenido_linea, texto_buscado)}")
                                else:
                                    print(f"    {contenido_linea}")
                        else:
                            contenido_linea = linea.rstrip('\n')
                            lineas_exportar.append(contenido_linea + "\n")
                            print(f"    {resaltar_coincidencia(contenido_linea, texto_buscado)}")

                        coincidencias_totales += 1

                if hubo_coincidencia:
                    archivos_con_coincidencias += 1

            except Exception:
                continue

        sys.stdout.write("\r" + " " * 60 + "\r")

        print("\n" + "="*50)
        print("📊 " + t('summary'))
        print(f"   ↳ {t('sum_term')}: '{texto_buscado}'")
        
        f_nom_res = config_activa['filtro_nombre'] if config_activa['filtro_nombre'] else t('sum_all')
        print(f"   ↳ {t('sum_filter')}:  '{f_nom_res}'")
        
        if config_activa['mostrar_contexto']:
            c_res = f"{t('sum_yes')} ({config_activa['lineas_antes']} {t('before')} / {config_activa['lineas_despues']} {t('after')})"
        else:
            c_res = t('deactivated')
            
        print(f"   ↳ {t('context_lines')}:        {c_res}")
        print(f"   ↳ {t('sum_times')}:  {coincidencias_totales}")
        print(f"   ↳ {t('sum_files')}:             {archivos_con_coincidencias}")
        print(f"   ↳ {t('sum_scanned')}:  {archivos_revisados}")
        print("=" * 50)

        while True:
            print(f"\n1. {t('p_opt_1')}")
            print(f"2. {t('p_opt_2')}")
            print(f"3. {t('p_opt_3')}")
            
            opcion_post = input(f"\n{t('select_opt')} (1-3): ").strip()

            if opcion_post == "1":
                break

            elif opcion_post == "2":
                if not lineas_exportar:
                    print("\n" + t('no_results_exp'))
                    continue

                nombre_out = input(f"\n{t('in_exp_name')} ").strip()
                if not nombre_out:
                    nombre_out = "resultados_busqueda"

                if not nombre_out.lower().endswith(".txt"):
                    nombre_out += ".txt"

                try:
                    with open(nombre_out, "w", encoding="utf-8") as f_out:
                        f_out.writelines(lineas_exportar)
                    print("\n" + t('exp_success').format(nombre_out))
                except Exception as e:
                    print("\n" + t('exp_err').format(e))

            elif opcion_post == "3":
                return


# ==========================================
# MENÚ PRINCIPAL
# ==========================================

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("==================================================")
        print(t('title_main').center(50))
        print("==================================================\n")

        if es_configuracion_por_defecto(config_activa):
            tag_config = f"[{t('val_default')}]"
        else:
            perfil = config_activa.get('nombre_perfil', t('val_custom'))
            tag_config = f"[{perfil}]"

        # Generar texto dinámico de la opción 3 (Idioma actual primero)
        id_actual = config_activa.get("idioma", "es")
        otros_idiomas = [clave for clave in NOMBRES_IDIOMA.keys() if clave != id_actual]
        
        cadena_idioma = f"{NOMBRES_IDIOMA[id_actual]} / {NOMBRES_IDIOMA[otros_idiomas[0]]} / {NOMBRES_IDIOMA[otros_idiomas[1]]} / {NOMBRES_IDIOMA[otros_idiomas[2]]}"

        print(f"1. {t('opt_config')} {tag_config}")
        print(f"2. {t('opt_search')}")
        print(f"3. {cadena_idioma}")
        print(f"4. {t('opt_exit')}")
        print("\n--------------------------------------------------")

        opcion = input(f"{t('select_opt')} (1-4): ").strip()

        if opcion == "1":
            menu_configuracion()
        elif opcion == "2":
            ejecutar_busqueda()
        elif opcion == "3":
            menu_idioma()
        elif opcion == "4":
            print("\n" + t('exit_msg') + "\n")
            break


if __name__ == "__main__":
    main()