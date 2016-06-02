# DAAC-DB
Downed Allied Air Crew Database Austria. A web application. 

## About
This is the repository of the web application [Downed Allied Air Crew Database Austria](http://flj.eos.arz.oeaw.ac.at/). The application’s purpose is the publication of data about allied air crews whose planes were downed above Austria during WW II. The data running this application was gathered by Georg Hoffmann and Nicole Goll. For more information please refere to [Hoffmann, Fliegerlynchjusitz, 2015](https://www.schoeningh.de/katalog/titel/978-3-506-78137-6.html) or [Goll/Hoffmann, Missing in Action, 2016](http://www.bundesheer.at/download_archiv/pdfs/missing_in_action.pdf). 

## Install
The application was build with Python 3.4.

1. clone the repo
2. create a virtual environment and run install the required packages `pip install > requirements`
3. makemigrations and migrate `python manage.py makemigrations`and `python manage.py migrate`
4. start the dev-server `python manage.py runserver --settings=flj.settings.test`
5. browse to http://127.0.0.1:8000/

## Upload the data
To fetch the last version of the catalogue data, you have to execute the ipython scripts 
* `importBomber.ipynb` and 
* `importCrew.ipynb`

To do so:
1. Start a new iypthon session `python manage.py shell_plus --notebook --settings=flj.settings.test`,
2. open `importBomber.ipynb` and execute the script cell by cell. 
3. Then open `importCrew.ipynb`and execute the script cell by cell.

