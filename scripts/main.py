from subprocess import call
from src.app import main

# Run project in production mode
def prod():
    print ("Hello Prod!")
    main()


# Run project in dev mode
def dev():
    migrate()
    print ("Hello Dev!")
    main()


# Run database migration
def migrate():
    print ("TODO")