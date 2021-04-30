# **_SQL_**

SQL is a RDBMS (Relational Database Management System)

## Usages

### 1. Create a Database
```sql
CREATE DATABASE database_name;
```

### 2. Create a Table in a Database

ex: A table 'people' which contains first names and last names
```sql
CREATE TABLE people (
        first_name VARCHAR(30),
        last_name VARCHAR(30)
);
```

### 3. Populate a Table
ex: INSERT in 'people' table value first name (Guy) and last name (Cherubin)

Option 1
```sql
INSERT INTO people VALUES ('Guy', 'Cherubin');
```

Option 2
```sql
INSERT INTO people(first_name, last_name) VALUES ('Guy', 'Cherubin');
```

### 4. Add a new Column in a Table
```sql
ALTER TABLE people ADD COLUMN id INT NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST ;
```

==> Here we are adding a Primary Key (a column or a set of columns that uniquely identifies
a row of data in a table)

==> 'FIRST' means to put the column in the first position (it is known as a keyword magnets)

==> Keyword magnets can be: FIRST, SECOND, ..., BEFORE column_name, or AFTER column_name, LAST

### 5. Rename a Table
```sql
ALTER TABLE people RENAME TO person;
``` 

### 6.  Change a column in a table
```sql
ALTER TABLE table_name CHANGE COLUMN col_name new_col_name VARCHAR(30);
```

==> You can change as many column (existing in the table) you want in the same sentence

==> When you are changing data type for a column, you may lose data!

==> To change just the data type of a column:
```sql
ALTER TABLE table_name MODIFY COLUMN col_name VARCHAR(30);
```
==> You substitute the names and the type with what you want!

### 7. Drop a Column
```sql
ALTER TABLE table_name DROP COLUMN col_name;
```
==> Once you drop a column, everything that was stored in it is removed too! 

### 8. Retrieve data from a Table

Option 1
```sql
SELECT * FROM table_name;
```
Option 2
```sql
SELECT col1, col2, col3,..., colN FROM table_name;
```
Option 3
```sql
SELECT col1, col2, col3,..., colN FROM table_name WHERE condtion;
```

### 9. Modify a Column
```sql
UPDATE table_name SET col_name = data;
```
==> This will loop over every row in the column to change the data

==> If you want for a specific row(s), you add the WHERE clause 