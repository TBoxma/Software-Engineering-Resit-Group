# Time Tracking Tool
## Running application
To run the application, either download latest release from the releases page of this repository. \
Or, download the source code and see next section for instructions. 
## Development setup
On first run:
1. Initiliase **Poetry** with `poetry init`
2. Run `poetry shell` to start venv.
3. Run `poetry install` to fetch all dependencies

To run tests, execute: `poetry run pytest`\
To start application in dev mode, run: `poetry run dev`

## Database setup

### SQLite

1. Run `alembic init`
2. Rollback both alembic/env.py and alembic.ini changes if there are some.
    - if second env.py or alembic.ini files are created, delete them
    - !!! Make sure, that there are some files in alembic/versions directory !!!, see 4. if there are none
3. Run `alembic upgrade head`. This command should create new file /data/ttt.db, with all needed columns.
4. Ask Efim if anything breaks

### Developing with Alembic
After any changes to existing models or creation of new ones:
1. Make sure new model is imported in `alembic/env.py`
2. Run `alembic revision --autogenerate -m <your_message_here>`
3. To sync local database, run: `alembic upgrade head`

Optionally: check if new version in `alembic/versions` reflects changes you made.

### Releasing executable files
1. Make sure you have [PyInstaller](https://pyinstaller.org/en/stable/) installed on your system.
2. Execute: `poetry run pyinstaller main.py --collect-submodules application --onefile --paths [path_to_spec]"`. \
Here, replace [path_to_spec] with an **absolute** path to .venv/Lib/site-packages.
    - Example of [path_to_spec] on Windows: "C:\Users\john\Software-Engineering-Resit-Group\\.venv\Lib\site-packages" 
3. After that, there should be a "dist" folder with an executable inside. Run this executable file from **command line** to make sure it works correctly. 
4. If you need to rebuild the executable, run `poetry run pyinstaller main.spec`.
5. Folders /build, /dist and /data are a part of executable program. Create a zip archive where you include all of them. After that this zip archive can be released on GitHub. \ 

WARNING: releases are platform specific. If you ran above commands on Linux, it will create Linux executable, which will not work on Windows/MacOS. 
    
