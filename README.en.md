🌍 *Read this in other languages: [English](README.en.md) | [Español](README.md) | [Русский](README.ru.md) | [tlhIngan](README.tlh.md)*

# 🔍 Smart File Search

A lightweight, fast, dependency-free Python script designed to search for exact words or phrases **inside** the content of multiple text files simultaneously. Ideal for developers, auditors, or anyone who needs to scan large volumes of text.

## ✨ Key Features

* **Deep Internal Search:** Scans the actual content of files, not just their names.
* **🌍 Native Multi-language Interface:** Dynamic menu available in **Spanish, English, Russian, and Klingon (tlhIngan Hol)**. The language can be changed on the fly from the main menu.
* **🎯 Precise Filters:** Limit your search by defining the root folder, specific extensions (e.g., `.txt, .py, .log`), and mandatory words in the filename.
* **📖 Smart Context:** Prints the lines of text immediately before and after the match to understand the context without opening the original file.
* **💾 Profile Manager:** Save your recurring search parameters and load them quickly in future sessions.
* **📤 Results Export:** Save the entire match report and its context in a clean `.txt` file for later review.
* **📦 Zero Dependencies:** Built exclusively with standard Python libraries (`os`, `sys`, `json`, `re`). Works on Windows, Linux, macOS, and Android (via Termux/Pydroid).

## 🚀 Requirements and Installation

All you need is **Python 3.6+** installed on your system. No need to install packages via `pip`.

1. Clone this repository or download the `busca.py` file:
   ```bash
   git clone https://github.com/asesoriaogam-collab/py-interactive-grep.git
   ```
2. Navigate to the project folder:
   ```bash
   cd repo-name
   ```
3. Run the script:
   ```bash
   python busca.py
   ```

## 🛠️ Basic Usage

Upon running the script, you'll be greeted by an interactive console menu:

1. **Configuration:** Here you can define the folder to scan, extensions (default `.txt`), enable context, and manage your profiles.
2. **Start search:** Boots up the search engine asking for the exact word or phrase to locate.
3. **Language Selection:** Allows you to instantly switch the interface between available languages.
4. **Exit:** Safely closes the application.

### 💡 Workflow Example
* Enter Configuration -> Define search in `.log` extensions and enable 2 lines of context.
* Start search -> Search for the word `ERROR`.
* The script will show you exactly in which `.log` files it occurred and print the two lines of code before and after each error so you understand what happened.
* At the end, export the results to `error_report.txt`.

## 🤝 Contributions
Contributions are welcome! If you want to add a new language to the built-in dictionary, improve the search algorithm, or fix a bug, feel free to Fork the project and submit a Pull Request.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
