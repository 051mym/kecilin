Note Untuk Menjalankan

cd kecilin
python -m venv venv
.\venv\Scripts\activate
cd kecilin
pip install -r .\requirements.txt
python .\manage.py migrate
python .\manage.py runserver

access server http://127.0.0.1:8000/
