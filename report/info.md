## first generate results running

copy the output files from phase 2 and phase 3 (a and be) into reports data folder
This is to ensure any accidental overwrites from the outer project (experiement generation) does not 
effect the reporting and its results.

inside the report folder
run
python results_analysis.py
which will create the descriptive statistics for every window

These results then used in the notebook data_analysis.ipynb. The filenames used in the notebook match the results files (under report).

