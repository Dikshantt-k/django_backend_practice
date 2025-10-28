set -x  # show commands
echo ">>> Inside setup.sh" >&2

echo ">>> Python version:" >&2
python3 --version >&2

echo ">>> Current directory before collectstatic:" >&2
pwd >&2
ls >&2


pip install setuptools
pip install -r requirements.txt


python manage.py makemigrations
python manage.py migrate    


python manage.py collectstatic