# telemedicine-backend

## Initial Installations(For ubuntu)
1. virtualenv
```console
sudo apt-get install virtualenv
```
2. pip3
```console
sudo apt-get install python3-pip
```

## Initial Setup(For ubuntu)
1. Make Projects directory
```console
mkdir Projects/
cd Projects
```
2. Clone the repository
```console
git clone https://github.com/yashrtalele97/telemedicine-backend.git
cd telemedicine-backend/
```
3. Create virtual environment
```console
virtualenv venv
```
4. Activate virtual environment
```console
source venv/bin/activate
```
5. Install requirements.txt
```console
pip3 install -r requirements.txt
```

## Steps to start the backend server(For ubuntu)
1. Make initial migrations
```console
python manage.py makemigrations
```
2. Migraye
```console
python manage.py migrate
```
3. Run the server
  - On the localhost  
    ```console
    python manage.py runserver
    ```
  - On the IP address
  ```console
   ip address
   # copy the inet address from wl01
   # PORT can be any 4 digits number, but make sure that port is not used by any other application
   python manage.py runserver 192.XXX.X.XXX:PORT
  ```
