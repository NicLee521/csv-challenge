# CSV Combiner

This program takes any amount of csvs given in the initial argument and adds an additional column with the filename of the csv to the end of each. Then takes all of the csvs and combines them on after another into a new csv which then is outputed to `stdout` and a newly created file in the same location as the script with the name `combined.csv`

## Input

While running the script the arguments should be given as follows:
```
python csv_combiner.py fixtures\accessories.csv fixtures\clothing.csv
```
With the file paths being in relation to the location of the script and seperated by spaces in the command

