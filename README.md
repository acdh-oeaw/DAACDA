# DAACDA
**D**owned **A**llied **A**ir **C**rew **D**atabase **A**ustria. A web application.

## About
This is the repository of the web application [Downed Allied Air Crew Database Austria](http://daacda.eos.arz.oeaw.ac.at/). The application’s purpose is the publication of data about allied air crews whose planes were downed above Austria during WW II. The data running this application was gathered by Georg Hoffmann and Nicole Goll. For more information please refere to [Hoffmann, Fliegerlynchjustiz, 2015](https://www.schoeningh.de/katalog/titel/978-3-506-78137-6.html) or [Goll/Hoffmann, Missing in Action, 2016](http://www.bundesheer.at/download_archiv/pdfs/missing_in_action.pdf). 

## Install
The application was built with Python 3.4.

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
1. Start a new ipython session `python manage.py shell_plus --notebook --settings=flj.settings.test`,
2. open `importBomber.ipynb` and execute the script cell by cell.
3. Then open `importCrew.ipynb`and execute the script cell by cell.

## Geographic locations

The geographic location of the crash points is determined with recourse to the geographic database [GeoNames](http://www.geonames.org). The coordinates of the crash points result from their assignment to the respective town or city (so-called *PPLA*, seat of an administrative division of certain order), which does not necessarily have to coincide with the administrative unit itself (*ADM*).

## Crash sites
In some cases, the original designations of the crash sites were made more precise. These original names were retained in the data set by using the label function, label type `orig`.

## Aircraft units
The designation of the aircraft units consists of four elements.

e.g.:  `8th USAAF | 67 | 44 | 42-72853`

Element | Meaning
--- | ---
`8th USAAF` | Air Force
`67` | Squadron
`44` | Bomber Group
`42-72853` | Aircraft Identification Number
