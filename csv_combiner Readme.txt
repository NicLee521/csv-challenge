How To Use

When running the script from the command prompt the user must put the file paths of the csvs they want to use
as arguments after the script call. These file paths have either be in the same folderas the script for in a 
sub-folder. Once called the script will run and will output the newly created csv into the console using stdout 
and will also create a file named "combined.csv" in the same folder as "csv_combiner.py"

EX. 
python csv_combiner.py fixtures\accessories.csv fixtures\clothing.csv
