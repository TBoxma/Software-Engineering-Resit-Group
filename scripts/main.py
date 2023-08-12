from subprocess import call

# Run project in production mode
def prod():
    print ("Hello Prod!")
    call(["python", "../src/app.py"])


# Run project in dev mode
def dev():
    migrate()
    print ("Hello Dev!")
    call(["python", "../src/app.py"])


# Run database migration
def migrate():
    print ("TODO")