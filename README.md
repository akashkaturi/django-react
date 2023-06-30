# django-react
django-react-app
## Install only this library and it works fine.

```bash
pip install mysql-connector-python

```

```bash
pip install pymysql
```

## Add this line in **init**.py file

```bash
import pymysql
pymysql.install_as_MySQLdb()
```

```bash
git config --global user.name "Akash Katuri"
git config --global user.email "akashkaturi77@gmail.com"
git config --global push.default matching 
git config --global alias.co checkout 
git config --global init.defaultBranch main
git init
```


```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "Akash Katuri", "title": "Matrix","password":"password","description":"Good", "rating":3.5 }' http://localhost:8000/api/movies/ 
```

```bash
curl -X PUT -H "Content-Type: application/json" -d '{"name": "Akash Katuri", "title": "Matrix","password":"password","description":"Good", "rating":3.5 }' http://localhost:8000/api/movies/1/
```

```bash
curl -X DELETE http://localhost:8000/api/movies/1/
```