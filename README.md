Note Untuk Menjalankan

cd kecilin
python -m venv venv
.\venv\Scripts\activate
cd kecilin
pip install -r .\requirements.txt
python .\manage.py migrate
python .\manage.py runserver

url website http://127.0.0.1:8000/
url api http://127.0.0.1:8000/api/mutation-list