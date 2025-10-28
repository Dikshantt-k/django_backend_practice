pip install setuptools
pip install -r requirements.txt


python manage.py makemigrations
python manage.py migrate    

echo "Current directory before collectstatic:"
pwd
python manage.py collectstatic