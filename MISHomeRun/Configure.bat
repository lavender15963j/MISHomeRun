virtualenv ..\Env
call ..\Env\Scripts\activate.bat

pip install -r REQUIREMENTS.txt

python manage.py migrate --noinput

REM http://gnuwin32.sourceforge.net/packages/unzip.htm is required.
REM unzip -u initial_data.zip

python manage.py loaddata superuser.json