virtualenv ..\Env
call ..\Env\Scripts\activate.bat
python -m pip install --upgrade pip==8.1.1
pip install -r REQUIREMENTS.txt

python manage.py migrate --noinput

REM http://gnuwin32.sourceforge.net/packages/unzip.htm is required.
REM unzip -u initial_data.zip

python manage.py loaddata superuser.json