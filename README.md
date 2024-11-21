# WebWizards - USV - Backend
Acest proiect reprezintă backend-ul aplicatiei pentru programarea examenelor.

## Tutorial
1. [Descarcă repositoriul de pe pagină și dezarhivați-o](https://github.com/Necromancer20/web-wizards-usv-backend/tree/main) sau foloșeste comanda **git clone https:\/\/github.com\/Necromancer20\/web-wizards-usv-backend.git** [(pentru a folosi comanda trebuie să descarți git)](https://git-scm.com/downloads) în terminal.
2. Deschideți programul într-un IDE (Integrated Development Environment)
3. Deschideți terminalul în directorul unde se află programul.
4. Verificați dacă aveți limbajul de programare **[Python](https://www.python.org/downloads/)** și **pip** instalat și configurat corect.
    * Comanda **pytnon --version** pentru a verifica dacă python e instalat și configurat corect.
    * Comanda **pip --version** pentru a verifica dacă pip e instalat și configurat corect.
5. Introdu comanda **python -m venv env** pentru a creea mediul virtual.
    * **python**: Se referă la versiunea Python instalată.
    * **-m venv**: Modulul Python pentru crearea mediilor virtuale.
    * **env**: Numele folderului care va conține mediul virtual. (poate fi introdus ori ce nume aici)
6. Activare mediul virtual folosind **.\env\Scripts\activate.bat**
7. Instalarea dependențelor folosind comanda **pip install -r requirements.txt** 
8. Introdu comanda **uvicorn main:app -reload** pentru a rula programul.
9. Dacă nu apare nici o eroare și la final scrie **Application startup complete.** intră pe [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
