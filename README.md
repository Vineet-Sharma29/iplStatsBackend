# iplStatsBackend

This web app analyses IPL data from 2008 to 2016 to know various trivia and stats about IPL. Frontend for this app can be found [here](https://github.com/Vineet-Sharma29/ipl-stats)

# Tech Stack
> frontend
* VueJS
* ChartJS

> Backend
* Django
* Postgres

# Challenges Faced

* Data was difficult to handle with. 
  * There were some entries which looked blank but had white spaces.
  * Some integer fields had string NULL values.
  * There were also some fields which were foreign key but had blank value
  * Data was large(approx ~150K) rows due to which database addition through Django ORM was time taking process
* Choosing right type of graph
* Analysis involved using complex queries using Django ORM

# Code Structure

* `ipl` has complete logic of backend
* `uploadData.py` is used to add csv file data to database through Django ORM
* `util.py` has all the queries used to results 
* `models.py` has db-schema design. All necessary constraints arising due to available data is considered
* `ipl/data` contains data used in get analysis


# Screenshot

![screenshot](https://github.com/Vineet-Sharma29/ipl-stats/blob/master/screenshot.png)

## Project setup
```
virtualenv env-ipl
source ./env-ipl/bin/activate
cd iplStatsBackend
pip install -r requirements.txt
```

## Add data to DB
```
python manage.py shell
from ipl import uploadData
uploadData.run()
```

### Run backend
```
python manage.py runserver
```
