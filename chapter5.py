# ETL PROCESS IN PYTHON 
# Extract data from CSV, SQL tables, MongoDB collections or Json Files 
# Transform 
# data transformation 
# column transformations, sorting, grouping data, concatenating data, removing duplicates 
# load => csv files, sql tables, nosql tables, json files 

# extract file python 
class extract: 
    def fromCSV(self):
        pass 
    def fromSQL(self):
        pass 
    def fromMYSQL(self):
        pass 
    def fromMongoDB(self):
        pass 


class extract:
    def fromCSV(self, file_path, delimiter=", ", quotechar="|"): 
        # if the file is not there 
        if not file_path:
            raise Exception("You must provide a valid file path")
        # now import the csv 
        import csv 
        # put csv into a list 
        dataset = list() 
        # open this file 
        with open(file_path) as f:
            # list of dictionaries where each dictionary contains data 
            # for a single row in the csv file 
            csv_file = csv.DictReader(f, delimiter=delimiter, quotechar=quotechar) 
            # for loop 
            # for each row in the csv file 
            # add row in the dataset 
            # return dataset 
            for row in csv_file:
                dataset.append(row) 
        return dataset 

    def fromJson(self, file_path):
        if not file_path:
            raise Exception("You must provide a valid file path")
        import json 
        dataset = list() 
        with open(file_path) as json_file: 
            dataset = json.load(json_file) 
        return dataset 
    
    # INSTALL PYMYSQL PACKAGE - python3 -m pip install pymysql 
    # host: localhost, username: root, password:admin 
    # thats takes in host, username, password, database and query arguments 
    def fromMYSQL(self, host, username, password, database, query): 
        # checks if any of these arguments are not provided and if any of them re missing 
        if not host or not username or not database or not query:
            # raises an exception with a message indicating that all arguments must be provided 
            raise Exception("Please make sure you input a valid host, \username, password, database and query") 
        # import pymysql and uses it to connect to a MYSQL databases 
        import pymysql 
        # with a specified host, username, password, database and cursorclass 
        db = pymysql.connect(host = host, user = username, password = password, database = database, cursorclass = pymysql.cursors.DictCursor) 
        # It then sets the cursorclass to pymysql.cursors.DictCursor, which tells 
        # the pymysql module to return the data as a dictionary instead of a tuple.
        # cursor object 
        cur = db.cursor() 
        # cursor object and uses it to execute the given query on the database.
        cur.execute(query) 
        # dataset is put into a list 
        dataset = list() 
        # iterates over the results of the query and appends each row to a list called dataset.
        for r in cur:
            dataset.append(r) 
        # commits the changes to the database, 
        # closes the cursor, and 
        # closes the connection to the database, and returns the dataset list.
        db.commit() 
        cur.close() 
        db.close() 
        # return dataset 
        return dataset 
    # host: localhost, port: 27017, username: admin, password: admin 
    def fromMongoDB(self, host, port, username, password, db, collection, query=None): 
        if not host or not port or not username or not db or not collection:
            raise Exception("Please make sure that you input a valid host, username, password, database and collection")
            import pymongo 
            client = pymongo.MongoClient(host=host, port=port, username=username, password=password) 
            tmp_database = client[db] 
            tmp_collection = tmp_database[collection] 
            dataset = list() 
            if query:
                for document in tmp_collection.find(query):
                    dataset.append(document) 
                return dataset 
            for document in tmp_collection.find():
                dataset.append(document) 
            return dataset 


e = extract() 
dataset = e.fromJson(file_path="data/person.json")
print(dataset) 
print(len(dataset)) 


# TRANSFORM CLASS 
# use these steps 
# 1. confirm the dataset exists 
# 2. see what columns and attributes exist in the dataset 
# 3. to determine what columns are named 
# 4, to examine what kind of data is in each column or attribute 
class transform:
    # large datasets and want to verify if that dataset exists 
    # return the top N records from the dataset 
    def head(self, dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty")
        if step < 1:
            raise Exception("The step value must be positive")
        return dataset[0:step]
    # return the last N records from the dataset 
    def tail(self, dataset, step):
        if not dataset:
            raise Exception("Dataset cannot be empty") 
        if step < 1:
            raise Exception("The step value must be positive")
        return dataset[len(dataset) - step:len(dataset)]
    # 
    def rename_attribute(self, dataset, attribute, new_attribute):
        if not dataset:
            raise Exception("Dataset cannot be empty") 
        if not attribute:
            raise Exception("The attribute key must be a valid key")
        # create a new list 
        new_dataset = list() 
        for row in dataset:
            if attribute in row.keys():
                val = row[attribute] 
                new_row = row.copy() 
                del new_row[attribute]
                new_row[new_attribute] = val 
                new_dataset.append(new_row) 
            else:
                raise Exception("Operations is not possible because the \ column" + str(column_name) + "dpes not exist in one of the rows \ in the dataset")
        return new_dataset 

    def remove_attribute(self, dataset, attribute):
        new_dataset = list() 
        for row in dataset:
            new_row = row 
            if attribute in new_row.keys():
                del new_row[attribute] 
                new_dataset.append(new_row) 
        return new_dataset 

    def transform(self, dataset, attribute, new_attribute, transform_function, *args): 
        if not dataset:
            raise Exception("Dataset cannot be empty") 
        if not attribute or not new_attribute:
            raise Exception('The input attribute cannot be empty') 
        if not transform_function:
            raise Exception("The transform function cannot be None") 
        new_dataset = list() # output of this function 
        for row in dataset:
            t = transform_function(row[attribute], *args) # apply transformation function on column 
            z = row.copy() 
            z.update({new_attribute: t})
            new_dataset.append(z) 
        return new_dataset 
        

t = transform()
dataset_1 = t.head(dataset=dataset, step=5) 
print("Top 5 records in the dataset")
for row in dataset_1:
    print(row['_id'])

dataset_2 = t.tail(dataset=dataset, step=5) 
print("\nBottom 5 records in the dataset") 
for row in dataset_2:
    print(row['_id']) 

t = transform() 
new_dataset = t.transform(dataset = dataset, attribute = "Open", new_attribute = "open_price_rounded") 


# LOAD CLASS 
class load: 
    def toCSV(self):
        def toCSV(self, file_path, dataset):
            if not dataset:
                raise Exception("Input dataset must have atleast one item")
            if not file_path:
                raise Exception("You must provide a valid csv file path")
            import csv 
            with open(file_path, 'w') as csvfile:
                fieldnames = dataset[0].keys() 
                writer = csv.DictWriter(csvfile, fieldnames = fieldnames) 
                writer.writeheader() 
                writer.writerows(dataset) 

    def toJson(self):
        pass 

    def toMYSQL(self, host, username, password, database, table, dataset): 
        if not dataset:
            raise Exception("Input dataset must have atleast one item")
        if not database:
            raise Exception("You must provide a valid database name") 
        if not table:
            raise Exception("You must input a valid table name") 
        import pymysql 
        database = pymysql.connect(host = host, user = username, password = password, database = database, cursorclass = pymysql.cursors.DictCursor) 
        cur = database.cursor() 
        for row in dataset:
            placeholder = ", ".join(["%s"] * len(row)) 
            stmt = "insert into [table] ({columns}) values ({values});".format(table=table, columns=", ".join(row.keys()), values=placeholder) 
            cur.execute(stmt, list(row.values())) 
        database.commit() 
        cur.close() 
        database.close() 

    def toMongoDB(self):
        pass 


# IMPROVE ETL SCRIPTING WITH STATIC METHODS 