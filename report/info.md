## first generate results running

To produce a report running an example 
copy the output files from phase 2 and phase 3 (a and be) rom results into reports report/data folder

Replace the filenames in desc_analysis.py under function "generate_descriptive_stats() "
(projects files):
"ft_account_values.csv"
"sen_account_values_norm.csv"
"sen_account_values_mapped.csv"
and run python desc_analysis.py.py

which will create the descriptive statistics for every window

These results then used in the notebook data_analysis.ipynb. The filenames used in the notebook match the results files (under report).

