##################################################
## Author: {Sayantan Biswas}
## Maintainer: {Sayantan Biswa}
## Email: {sayantanbiswas1002@gmail.com}
##################################################


# Flask Calendar Task with Login Application

The `app.py`

A complete application using Flask factories, click commands and storing
passwords encrypted in a json file `users.json` which you can easily take
as example to replace with your own database appr.

> NOTE: this example is not meant for production use as writing in a json file is suitable only for single access.
> For better performance go with MongoDb, TinyDB or other SGDB.

----------------------------------------------
Run with:

```
bash
python app.py
```
-----------------------------------------------
Create new user:

```
bash
python app.py adduser
```
-----------------------------------------------
Run the server

```bash
python app.py runserver
```
-----------------------------------------------
When you are inside the app, rest is self-explanatory.

The history is only available if you login through admin account.

----------------------------------------------<THANK YOU>------------------------------------------
