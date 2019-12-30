Title: Quick tutorial on MySQL
Date: 2015-01-16 16:07
Author: jslandy
Category: Tools
Slug: quick-tutorial-on-mysql
Status: published
Attachments: wp-content/uploads/2015/01/Detroit_Pistons_logo.svg_.png, wp-content/uploads/2015/01/past_week.txt, wp-content/uploads/2015/01/50x50-Primary-Team-Logos-Sprite.png, wp-content/uploads/2015/01/500px-San_Antonio_Spurs.svg_.png, wp-content/uploads/2015/01/predictions10.txt, wp-content/uploads/2015/01/720px-LosAngeles_Lakers_logo.svg_.png, wp-content/uploads/2015/01/dataWeek10.txt, wp-content/uploads/2015/01/alg_2_week_2.rtf, wp-content/uploads/2015/01/nba2013.txt, wp-content/uploads/2015/01/500px-Oklahoma_City_Thunder.svg_.png, wp-content/uploads/2015/01/nba2011.txt, wp-content/uploads/2015/01/500px-Atlanta_Hawks.svg_.png, wp-content/uploads/2015/01/Screen-Shot-2015-02-27-at-11.22.02-AM.png, wp-content/uploads/2015/01/Brooklyn_Nets_logo.png, wp-content/uploads/2015/01/nba2012.txt, wp-content/uploads/2015/01/500px-Denver_Nuggets.svg_.png, wp-content/uploads/2015/01/Cleveland_Cavaliers_2010.svg_.png, wp-content/uploads/2015/01/500px-Indiana_Pacers.svg_.png, wp-content/uploads/2015/01/nba2010.txt, wp-content/uploads/2015/01/408px-Chicago_Bulls_logo.svg_.png, wp-content/uploads/2015/01/plot.pdf, wp-content/uploads/2015/01/500px-Phoenix_Suns.svg_.png, wp-content/uploads/2015/01/BostonCelticsLogo.png, wp-content/uploads/2015/01/Chicago_Bulls_Logo.png, wp-content/uploads/2015/01/Charlotte_Bobcats_2012.png, wp-content/uploads/2015/01/500px-Minnesota_Timberwolves.svg_.png, wp-content/uploads/2015/01/nba2014_complete.txt, wp-content/uploads/2015/01/new_week.txt, wp-content/uploads/2015/01/76ers.png, wp-content/uploads/2015/01/Screen-Shot-2014-10-31-at-4.57.50-PM.png, wp-content/uploads/2015/01/500px-Toronto_Raptors.svg_.png, wp-content/uploads/2015/01/library6.jpg, wp-content/uploads/2015/01/Dallas_Mavericks_logo.svg_.png, wp-content/uploads/2015/01/500px-Boston_Celtics.svg_.png

Here, we give a quick (< 30 mins) introduction to the open source database software package MySQL. The post is intended to be useful for folks totally new to the program, as well as for those who find that they often need reminders on its basic syntax (that is, people like us).  

[Follow @efavdb](http://twitter.com/efavdb)  

Follow us on twitter for new submission alerts!

#### **Getting started**

MySQL is a database software package that allows users to quickly access subsets of data contained within tables, and also to carry out simple operations on this data. The software is quite powerful, but it can be surprisingly unintuitive for beginners. The best way to get the hang of it is to play around with it a bit. This post provides a set of commands that should help you get a feel for how it works. If you're a beginner reading this, we suggest [installing](http://dev.mysql.com/doc/refman/5.5/en/installing.html) it on your personal computer or server, and following along by trying each of the commands we go through here. Once it's installed and you have its server running, you can often access MySQL from the command line by typing

```  
mysql  
```

On a mac, you may need to use the following though

```  
/usr/local/mysql/bin/mysql -uroot  
```

Once mysql is loaded, you can see what databases are available by typing

```  
SHOW DATABASES;  
```

Notice that a semi-colon is used to terminate commands: In general, these can extend across multiple lines and the semi-colon tells the program where the command stops. Also, MySQL is case-insensitive, but it is considered good form to have all command calls capitalized for easier reading. If no databases yet exist, you can create one as follows:

```  
CREATE DATABASE animalDB;  
```

Here, `animalDB` is the name of the database. From the list of available databases,  
you can select one of interest with the `USE` command. For example,

```  
USE animalDB;  
```

Each database can contain many tables. To see the tables contained in a database, use the SHOW command,

```  
SHOW tables;  
```

#### **Table creation and alteration**

SQL tables have a name and a set of rows and columns. The columns have types that are defined upon table creation (`INT, BIGINT, FLOAT, DOUBLE, CHAR, VARCHAR`, etc.). The rows correspond to individual table entries. To illustrate, we’ll now create a table called “MyPets”, with a column for pet name, species, and age. This is done with the command

```  
CREATE TABLE MyPets (name VARCHAR(10),  
species VARCHAR(10), age INT);  
```

Here, we are using the `VARCHAR` type for our two string columns. The argument supplied allows us to use strings up to length `10` for these entries. We could also have used the `CHAR(10)` type here, but that would result in trailing spaces following names shorter than `10` characters. We now insert some entries using the `INSERT` command,

```  
INSERT INTO MyPets VALUES ("Bottles", "Dog", 3);  
INSERT INTO MyPets (name, species) VALUES ("Mac", "Dog");  
INSERT INTO MyPets VALUES ("Hector", "Cat", 1);  
```

Here, we’ve illustrated two different methods to do insertion. In the first and third lines, we have values for all columns. However, in the second, no age is supplied, so we have to specify which columns the values we are supplying correspond to. The age column for this entry will read `NULL`, since no value was provided for it. To view the table, we write – with `SELECT` and `∗` meaning \`\`retrieve" and “all”, respectively –

```  
SELECT * FROM MyPets;  
>>  
+---------+---------+------+  
| name | species | age |  
+---------+---------+------+  
| Bottles | Dog | 3 |  
| Mac | Dog | NULL |  
| Hector | Cat | 1 |  
+---------+---------+------+  
```

Additional `SELECT` queries are given below that illustrate how one can select and operate on subsets of the columns and rows. To add an age for Mac, we use the `UPDATE, SET`, and `WHERE` commands, writing

```  
UPDATE MyPets  
SET age = 7  
WHERE name = "Mac";  
```

To see that this and the other commands that follow work as expected, try running the `SELECT` command above after each application. To delete a row from the table, we use the DELETE command,

```  
DELETE from MyPets  
WHERE name = "Hector";  
```

It is also possible to add or subtract columns from a table. To add a column, we use  
the `ALTER` and `ADD COLUMN` commands,

```  
ALTER TABLE MyPets  
ADD COLUMN litters INT  
DEFAULT 0;  
```

The last line here is not necessary. Without it, the command would create the column and set each row’s value there to `NULL`. To delete a column, we use the `DROP` command,

```  
ALTER TABLE MyPets  
DROP litters;  
```

*Caveat:* While row addition and removal can always be carried out quickly, addition and removal of columns scales linearly with table size. The reason is that these operations are generally carried out by copying the original table into a second table having the desired new structure. For this reason, it is generally a good idea to plan ahead and make sure any new table has all the columns you foresee might be needed.

#### **SELECTION queries -- learn by example**

Example conditional commands:

1.  What is the name and age each of my pets?

    ```  
    SELECT name, age FROM mypets;  
    ```

2.  How many dogs have I got?

    ```  
    SELECT COUNT(*) FROM mypets WHERE species = "dog";  
    ```

3.  Show me just the first two pets in my table.

    ```  
    SELECT * FROM mypets LIMIT 2;  
    ```

4.  Show me my pets in age-descending order.

    ```  
    SELECT * FROM MyPets ORDER BY age;  
    ```

5.  Which of my dogs are under 4 years old?

    ```  
    SELECT * FROM MyPets WHERE age < 4 AND species = "dog";  
    ```

6.  Which animals have names that start with the letter “M”?

    ```  
    SELECT * FROM mypets WHERE name LIKE "M%";  
    ```

7.  Which animals have the letter “E” somewhere in their name?
    ```  
    SELECT * FROM mypets WHERE name LIKE "%E%";  
    ```

Example GROUP BY commands (see also `MIN, MAX, SUM, STD`, etc.):

1.  How many pets have I got of each species?

    ```  
    SELECT species, count(*) FROM mypets GROUP BY species;  
    ```

2.  What is the average age of my pets, grouped by species?
    ```  
    SELECT species, AVG(age) FROM mypets GROUP BY species;  
    ```

#### **Actions on multiple tables**

1.  To solidify what we've learned above, try to now create a second table, called `PetDetails`, like that above but with different age and species values. You can add other columns to it if you like. Once that's done, apply the `SHOW TABLES` command to see that both tables are available. Next, learn to copy specific values from this new table into the first one, using commands like

    ```  
    UPDATE MyPets, PetDetails  
    SET MyPets.age = PetDetails.age  
    WHERE MyPets.name = PetDetails.name;  
    ```

    Note the use of the period here to specify from which table a certain column is to be selected from.

2.  *The* `JOIN/ON` *commands*. The `JOIN` command essentially creates something like a flattened outer product of two tables: If there are $n$ entries in the first table and $m$ in the second, the command returns a table with $n \times m$ rows. There is one row for each possible pairing, one entry taken from the first table and one from the second. All columns from both tables are then included in the new table. The ON command can be used to specify conditions on which pairs are to be included in the combined table. To illustrate, let’s define a new table of pet-trick pairs

    ```  
    CREATE TABLE PetTricks (name VARCHAR(10), trick VARCHAR(10));  
    INSERT INTO PetTricks VALUES ("Bottles", "Shake");  
    INSERT INTO PetTricks VALUES ("Bottles", "Play dead");  
    INSERT INTO PetTricks VALUES ("Mac", "Shake");  
    INSERT INTO PetTricks VALUES ("Dogbert", "Consulting");  
    ```

    With the following, we get the number of tricks each of my pets can do

    ```  
    SELECT MyPets.name AS name, count(*) AS num_tricks  
    FROM (MyPets JOIN PetTricks  
    ON MyPets.name = PetTricks.name)  
    GROUP BY MyPets.name;  
    ```  
    Here, we see for the first time that it is possible to select values from a table created \`\`on the fly" (the table in parentheses, which you can print using the `SELECT` command). We also see for the first time the concept of aliasing, applied through use of the `AS` command.

3.  Our last -- and most complicated -- example combines many of the ideas discussed above. If you can get to the point where you can replicate commands like this one, you'll be pretty much set to construct your own complex SQL queries: Let’s add a trick count to our first table, and then fill it in by querying the PetTricks table.

    ```  
    ALTER TABLE MyPets  
    ADD COLUMN num_tricks INT  
    DEFAULT 0;

    UPDATE MyPets AS T1,  
    (Select name, count(*) AS tot  
    FROM PetTricks  
    GROUP BY name) AS T2  
    SET T1.num_tricks = T2.tot  
    WHERE T1.name = T2.name;

    SELECT * FROM MyPets;  
    >>  
    +---------+---------+------+------------+  
    | name | species | age | num_tricks |  
    +---------+---------+------+------------+  
    | Bottles | Dog | 3 | 2 |  
    | Mac | Dog | 7 | 1 |  
    | Hector | Cat | 1 | 0 |  
    +---------+---------+------+------------+  
    ```

#### **Other tips**

Lastly, a few one-off tips that can be very helpful.

1.  *Creating a new table similar another.* The following command can come in handy when you’re dealing with tables that have many columns:

    ```  
    CREATE TABLE TNew LIKE T1;  
    ```

    Here, the command creates `TNew`, a new table with column names and types like those of `T1`. The entries of `T1` are not copied over. If you want to copy some of them over, you can do that with a command like

    ```  
    INSERT INTO TNew (SELECT * FROM T1 WHERE ...);  
    ```

2.  *Saving to a text file.* Printing a table to a text file can sometimes be useful. To proceed, you first need to create a directory that MySQL can have write access to. On a mac, you can accomplish this from the terminal with the following

    ```  
    cd /usr/local  
    mkdir MySQLOutput  
    sudo chmod -R 777 MySQLOutput  
    ```

    This creates the directory `/usr/local/MYSQLOutput` with global read, write, and execute permissions. With this setup, we can write to a file from within MySQL with a command like

    ```  
    SELECT * FROM MyPets  
    INTO OUTFILE "/usr/local/MySQLOutput/test.txt"  
    ```

3.  *Scripts.* For complicated queries, or queries that you would like to be able to run multiple times, it is useful to employ scripts. These can then be executed from within mysql using the `SOURCE` command. To illustrate, suppose we have a text file called `/usr/local/MySQLOutput/test.txt` within which we have written the commands

    ```  
    CREATE table Bad_dogs (DogID BIGINT, Barks INT);  
    INSERT INTO Bad_dogs VALUES (1234567890, 666);  
    ```

    We can run this from within MySQL using the command

    ```  
    SOURCE /usr/local/MySQLOutput/test.txt;  
    ```

    This creates the table and inserts the example entry.

4.  *Indexing.* By creating an index, one can speed up `SELECT` calls on large tables. You can think of an index heuristically as a second table having two columns: The first is a sorted version of one of the original table’s columns, and the second column is a pointer to the memory block where its corresponding entry sits (actually, an index usually sits in a B-tree, a structure similar to a binary-search tree). Entries can be quickly accessed via the index, generally in logarithmic time. To add a key to our first table, write

    ```  
    ALTER TABLE MyPets  
    ADD PRIMARY KEY (name);  
    ```  
    This selects the name column as our index, which will speed up all `SELECT` calls seeking entries with `name` values satisfying some condition -- specified using `WHERE name = ...`. You can actually index as many columns of a table as you like. However, this takes up disk space, and so should be avoided when the extra indexes are not useful. It is also possible to specify that you want one or more columns to be keys upon table creation.

5.  *Further study.* At this point, we have covered most of the basics, but only the basics. If you get stumped by any tricky queries moving forward, we suggest visiting both [stackoverflow.com](http://stackoverflow.com/) -- which has tons of interesting discussions on the topic -- and the [MySQL documentation page](http://dev.mysql.com/doc/), which goes over most everything and includes a tutorial in chapter 3 similar to this one. Both are excellent resources.

