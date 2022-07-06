# Script for Syntetic Data Generation for Relational Database
Script that can generate random tuples given the database's types and the number of samples (n)
The purpose of these script was to test the performance of default and user created index in PostgreSQL, the structure of the project is as follows: 
 1. Create the dataase, Schemas and tables.
 2. Generate the data  ("creating_csvs.py").
 3. Insert the data  ("final.py").

In the 3rd step, a stopwatch measures the time needed to insert the data, from 3k rows to a million. This scripts where tested with 20M rows for the table Order, and 1M rows for "Person"

---

## Format:
The Schema used to test the script has the following tables:

  - Person
  - CLient
  - Ingredient
  - Pizza
  - Local
  - User
  - Role
  - Worker
  - Order
  - PizzaIngredient
  - Soda
  - CL_User
  - Role_User
  - Shift
  - Recipe
  - Order_Soda
  - Order_Pizza
 
_For the sake of the presentation all tables were written in spanish._


## Methodology

Each table is described in the respective function, and each column of each table has his data generator:

For the "Client" table 
```python
    #cliente
    print("Cliente")
    n_clientes = 0
    with open('csv_files/cliente' + file, 'w', newline='') as csvfile:
        esc = csv.writer(csvfile, delimiter=',', quotechar = "\t", quoting=csv.QUOTE_MINIMAL)
        for i in tqdm(range(0, n_per - n_workers)):
            linea = ["('" + clientes_data[i][0] + "'"]
            linea.append(clientes_data[i][1])
            linea.append("'calle:" + chr(random.randrange(100,115))*20 + "')")
            n_clientes += 1
            esc.writerow(linea)
    csvfile.close()
```

As some tables have fields from others, some generated data will stay in memory for future use. For example, "Client" and "Worker" tables get data from the table "Person"
That's why some arrays persist in the program after they exit their respective table function.

The generated data is saved in csv files with the name of its respective table.

---

## Inserting data into the Database
**final.py** uses psycopg2 to insert the generated data into the PostgreSQL databasee. Each table has its own function that returns a string (cur) that contains the data to be inserted into the database. 
The data is read from the respective .csv file, previously generated by **creating_csvs.py**.