### Librerias Utilizadas

    pip install flask
    pip install MySQLdb
    python3 app.py
    pip install mysqlclient
    pip install flask_sqlalchemy
    pip install flask-login
    pip install flask-mysqldb
    pip install csv
    pip install reportlab

### comandos Utilizados

    python3 app.py
    python.exe -m pip install --upgrade pip
    python -m pip install --upgrade pip
    python -m pip install --upgrade python

### MYSQL Linux

    sudo apt-update
    sudo apt-upgrade
    sudo apt install mysql-server
    sudo mysql
    create user 'Gilberto'@'localhost' identified by 'CHICHARITOBLUE4';
    grant all privileges on _._ to 'Gilberto'@'localhost';

    Video --> https://www.youtube.com/watch?v=EYc9DNYyiW4s

### Correción De paquetes dañados

It seems that there is an error in your code related to the MySQL database library. The error message suggests that the Python interpreter could not find the "libmysqlclient.so.21" shared library file, which is required by the MySQLdb module. This could be due to a missing or corrupted installation of the MySQL client library on your system.

To fix this issue, you can try the following steps:

1. Check if the "libmysqlclient.so.21" library file exists on your system. You can use the "locate" command to search for it:

   locate libmysqlclient.so.21

If the file is found, make sure that its path is included in the system's library search path. You can add it to the "LD_LIBRARY_PATH" environment variable:

    export LD_LIBRARY_PATH=/path/to/libmysqlclient.so.21:$LD_LIBRARY_PATH

2.  If the library file is not found, you may need to install the MySQL client library on your system. On Ubuntu or Debian-based systems, you can install it using the following command:

        sudo apt-get install libmysqlclient-dev

On other Linux distributions or macOS, you may need to use a different package manager or download and install the library manually.

Once the MySQL client library is installed, try running your Python code again. If the error persists, you may need to reinstall the MySQLdb module:

    pip uninstall mysqlclient
    pip install mysqlclient

Alternatively, you can try using a different MySQL library for Python, such as PyMySQL or mysql-connector-python.
