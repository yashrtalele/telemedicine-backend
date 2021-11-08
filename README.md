# telemedicine-backend

### Initial Installations
#### For ubuntu
1. virtualenv
```console
yash97@yash:~$ sudo apt-get install virtualenv
```
2. pip3
```console
yash97@yash:~$ sudo apt-get install python3-pip
```
#### For windows
1. virtualenv
```powershell
PS C:\Users\yasht> python -m pip install --upgrade pip
PS C:\Users\yasht> python -m pip install --user virtualenv
```

### Initial Setup
#### For ubuntu
1. Make Projects directory
```console
yash97@yash:~$ mkdir Projects/
yash97@yash:~$ cd Projects
```
2. Clone the repository
```console
yash97@yash:~/Projects$ git clone https://github.com/yashrtalele97/telemedicine-backend.git
yash97@yash:~/Projects$ cd telemedicine-backend/
```
3. Create virtual environment
```console
yash97@yash:~/Projects/telemedicine-backend$ virtualenv venv
```
4. Activate virtual environment
```console
yash97@yash:~/Projects/telemedicine-backend$ source venv/bin/activate
```
5. Install requirements.txt
```console
yash97@yash:~/Projects/telemedicine-backend$ pip3 install -r requirements.txt
```
#### For windows
1. Clone the repository
```powershell
PS C:\Users\yasht> git clone https://github.com/yashrtalele97/telemedicine-backend.git
PS C:\Users\yasht> cd telemedicine-backend/
```
2. Create virtual environment
```powershell
PS C:\Users\yasht> python -m venv env
```
3. Activate virtual environment
```powershell
PS C:\Users\yasht> .\env\Scripts\activate
```
4. Install requirements.txt
```powershell
PS C:\Users\yasht> pip install -r requirements.txt
```

### Steps to start the backend server
#### For ubuntu
1. Make initial migrations
```console
yash97@yash:~/Projects/telemedicine-backend$ python manage.py makemigrations
```
2. Migrate
```console
yash97@yash:~/Projects/telemedicine-backend$ python manage.py migrate
```
3. Run the server
  - On the localhost  
    ```console
    yash97@yash:~/Projects/telemedicine-backend$ python manage.py runserver
    ```
  - On the IP address
    ```console
    yash97@yash:~/Projects/telemedicine-backend$ ip address
    ```
   
    > copy the inet address from wl01 <br />
    > PORT can be any 4 digits number, but make sure that port is not used by any other application
    ```console
    yash97@yash:~/Projects/telemedicine-backend$ python manage.py runserver 192.XXX.X.XXX:PORT
    ```
#### For windows
1. Make initial migrations
```powershell
PS C:\Users\yasht> python manage.py makemigrations
```
2. Migrate
```powershell
PS C:\Users\yasht> python manage.py migrate
```
3. Run the server
  - On the localhost  
    ```powershell
    PS C:\Users\yasht> python manage.py runserver
    ```
  - On the IP address (for the following the powershell or windows terminal need to be run as administrator)
    ```powershell
    PS C:\WINDOWS\system32> Get-NetIPAddress -AddressFamily IPV4
    ```
   
    > copy the ip address <br />
    > PORT can be any 4 digits number, but make sure that port is not used by any other application
    ```powershell
    PS C:\Users\yasht> python manage.py runserver 192.XXX.X.XXX:PORT
    ```
