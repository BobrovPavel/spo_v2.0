### The project uses
1. Python 3.8
2. PyQt5 5.13.2 
3. WMI 1.4.9
4. psutil 5.6.4
5. and other...

### To install and run
```bash
$ git clone https://github.com/BobrovPavel/spo_v2.0.git
$ cd spo_v2.0
$ pip install -r requirements.txt
```
Run "wdiget.py" file

### For create .exe file
```bash
$ pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz
$ pyinstaller --onefile --windowed widget.py
```