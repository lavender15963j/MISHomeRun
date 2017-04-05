virtualenv ..\Env
call ..\Env\Scripts\activate.bat
python -m pip install --upgrade pip

pip install ./lib/lxml-3.5.0-cp27-none-win_amd64.whl
pip install ./lib/Scrapy-1.3.1-py2.py3-none-any.whl
pip install -r REQUIREMENTS.txt
