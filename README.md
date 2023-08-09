# Time Tracking Tool
## Running application
TBD
## Development setup
On first run:
1. Initiliase **Poetry** with `poetry init`
2. Run `poetry shell` to start venv.
3. Run `poetry install` to fetch all dependencies

To run tests, execute: `poetry run pytest`\
To start application in dev mode, run: `poetry run dev`

## Database setup
For now, you have to connect your own database to make it work. pyproject.toml contains mysqlclient and mysql. Comment out one of them.

1. Install MySQL on your pc, installation is OS dependent
2. Create a user and a database for this project within MySQL
3. Add the credentials for the account and database you made to config/mysql.py
4. Run poetry run pytest
5. Ask Efim if anythong breaks