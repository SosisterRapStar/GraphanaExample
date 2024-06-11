import psycopg2
from dotenv import load_dotenv
from psycopg2.errors import DuplicateTable
import os
import random
import time


load_dotenv()

conn = psycopg2.connect(
    database=os.getenv("POSTGRES_DB"), user=os.getenv("POSTGRES_USER"),
  password=os.getenv("POSTGRES_PASSWORD"), host="localhost", port='5432'
)

conn.autocommit = True

cursor = conn.cursor()

create_table = '''
CREATE TABLE metrics (
    id SERIAL PRIMARY KEY,
    request_url VARCHAR(255) NOT NULL,
    execution_time DOUBLE PRECISION NOT NULL,
    time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
'''

try:
    cursor.execute(create_table)
except DuplicateTable:
    pass


api_endpoints = [
    "users/home",
    "users/me",
    "users/login",
    "shop/getproducts",
    "shop/getproducts",
    "shop/getproducts",
    "shop/createorder",
    "shop/updateorder",
    "shop/deleteorder",
    "shop/checkout",
    "shop/searchproducts",
    "shop/addtocart",
    "shop/removefromcart",
    "shop/viewcart",
    "shop/checkoutprocess",
]

prepared_sql = """ INSERT INTO metrics (request_url, execution_time) VALUES (%s,%s)"""


while True:
    random_api = api_endpoints[random.randint(0, 14)]
    response_time = random.choices(
            population=[random.uniform(0.05, 0.5), random.uniform(0.8, 2)],
            weights=[0.8, 0.2],
            k=1,
        )[0]
    print(random_api, response_time)

    data = (random_api, response_time)
    cursor.execute(prepared_sql, data)
    time.sleep(5)
    

