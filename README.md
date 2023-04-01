## CIS3330-CODE-16-Read-Write-Files-Pandas

## Instructions

In this coding assignment, you are asked to create a little program to find information in a CSV file. You can code your program using the libraries CSV or Pandas. Your program should include the following functions:

* `get_mario_games`
  + The function should return all games that include "Mario" in the "Title" column
* `get_zelda_games`
  + The function should return all games that include "Zelda" in the "Title" column
* `get_xbox_games`
  + The function should return all games which "Release.Console" column is "X360"

## Useful python statements
  * To query elements in a data frame you can use `df.query()`
    * The query for querying if elements from a column called `column` has a `word` you can use `df.query('Column.str.contains("word")')`
    * The query for finding an exact element can look as follows `df = df.query('Column == "keyword"')`
    * Tip: for using `Release.Console` in a query statement, be sure to encapsulate the name with the character **`**
  * To list the columns of a file, you can execute `df.columns()`
  

## License disclosure

The dataset was obtained from https://think.cs.vt.edu/corgis/csv/video_games/
