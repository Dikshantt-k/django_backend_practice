pip install setuptools
pip install -r requirements.txt


python manage.py makemigrations
python manage.py migrate    

echo "Current directory before collectstatic:" >&2
pwd >&2
python manage.py collectstatic