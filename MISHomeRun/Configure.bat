virtualenv ..\Env
call ..\Env\Scripts\activate.bat
python -m pip install --upgrade pip

pip install -r REQUIREMENTS.txt

REM python manage.py migrate --noinput

REM http://gnuwin32.sourceforge.net/packages/unzip.htm is required.
REM unzip -u initial_data.zip

REM python manage.py loaddata superuser.json