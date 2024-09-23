source ~/venv/bin/activate
python3 -m pip install django
python3 -m pip install django-bootstrap_modal_forms
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR
python3 manage.py runserver
