# Flask Calendar Task with Login Application

The `manage.py`

A complete application using Flask factories, click commands and storing
passwords encrypted in a json file `users.json` which you can easily take
as example to replace with your own database manager.

> NOTE: this example is not meant for production use as writing in a json file is suitable only for single access. 
> For better performance go with MongoDb, TinyDB or other SGDB.

Run with:

```bash
python manage.py
```

Create new user:

```bash
python manage.py adduser
```

Run the server

```bash
python manage.py runserver
```


