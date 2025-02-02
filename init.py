from os import getenv
from dotenv import load_dotenv
load_dotenv('src/app.env')

version = getenv('VERSION')
author  = getenv('AUTHOR')
build   = getenv('BUILD')

print(f'CTkThemer {version} ({build})')
print(f'made by {author}')