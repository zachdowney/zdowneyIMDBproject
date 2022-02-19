# zdowneyIMDBproject
1. Zach Downey
2. I think you only need to import requests, import sprintTwo into test.py. When I created the shows database, you have to make sure the shows.db file is empty,
   for some reason, if you try to run it twice it says "UNIQUE constraint failed" etc. Same things goes when you are testing the test.py second test. You need to make sure 
   you delete anything from the tests.db file to run it. Other than that, I think every thing works normally.
3. My project grabs data from an API, creates a database and creates two tables, one for shows and one for user ratings. It puts the top 250 shows in the shows table
   followed by the "Wheel of time" to make 251 using a for loop. Then using another for loop, it takes the id from shows in the shows table and puts specific ones into a ratings table, which results in 5 entries in the ratings table. I also have two test methods in test.py to ensure the data set of 250 shows contains 250 shows and another one to test creating a database and inputing one entry. 
4. My database was created and then creates two tables shows and ratings, to view the tables I used DB browser and opened database 'shows.db' and then to view my test table I open tests.db. Also, I need to make sure both shows.db and tests.db are empty on pycharm to ensure the program will run again. 
5. I don't know what my program is missing but I wasn't able to get the pytest workflows to work unfortunately. 
