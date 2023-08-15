
# Run project in production mode
from src.app import serve_cli


def prod():
    print ("Hello Prod!")
    serve_cli()


# Run project in dev mode
def dev():
    migrate()
    print ("Hello Dev!")
    serve_cli()


# Run database migration
def migrate():
    print ("TODO")