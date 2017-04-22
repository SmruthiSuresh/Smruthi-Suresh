#Analysis 2.
Analysis in this question has been split up in 2 parts
#Part 1: Variation in the ranking of Northeastern University from 2005 to 2015.
#Part 2: A radar chart showing the score that Neu was given in terms of research, income, citations,teaching, international.
VARIATION IN RANKING OF NEU FROM 2005 TO 2015
•	All the three files (times data,cwurdata and shangaiData) are read
•	Name of university is set to Northeastern Unievrsity like(myuniv name=['Northeastern University'])
•	All the university names from all the three data are made into a list by using the union fucntion between cwur, shangaiData and timesData 
•	under the dictionary all_universities_names_list.
•	All unique university names are sorted and then printed.
•	To get the rank , the first digit of the rank is parsed in all three files.
•	Only the first digit is parsed to get the date ranges.
•	Styling is done on the data

<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Ana2PArt1img.PNG" alt='sadad'/>

Part 2: A radar chart showing the score that Neu was given in terms of research, income, citations,teaching,
international only for the year 2016.

Necessary libraries like matplotlib.path, matplotlib.pyplot and matplotlib.patches are imported.
Data of timesData is read
Factors that we would like to condiser in making the radar chart like teaching, international, citations, research and income are 
taken into a list named "properties".
Set the text of the title of the radar graph by joining both the university name and the year by using the "join" fucntion.
The radar graph is plotted by setting the axis plot as polar.

The radar graph shows the different properties of northeastern defined in the dictionary for the year 2016.

<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Anal%202%20part%202img.PNG" alt='sadad'/>



#Analysis 3
Part 1: Analyzing the difference in quality of Education is represented by plotting a seaborn plot.
Part 2: Analyzing the difference in ranking from 2011 to 2015 for the top 81 universities in terms of the shanghaiData.
Analysis is done on the cwur rankings file
Firstly the file is read
Function that returns the quality of educaiton is defined
A dataframe containing worldrank,country and quality of education of USA ad UK is defined
USA is passed as the argument to the funciton so that the quality of education of only the universities in USA is considered

A seaborn plot showing the quality of education of both UK and USA is plotted


<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Analysis3Part1.PNG" alt='sadad'/>


<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Anal3Part1b.PNG" alt='sadad'/>

Part 2: Analysing the difference in ranking from 2005 to 2015 for the top 81 universities

The shangaiData is read
All the universities of the shanghaiData are considered.
Only top 81 universities are taken for the analysis.
Using the sns the plot is generated
AUnique university names and ranks are considered
a variable called var is first initialized to -1
It is compared with the rank's last digit to find which range of rank the universisty lies in
Depending on that the variable is incremented
A darkgrid theme of seaborn is used to plot the rankigns of the universities from 2011 to 2015 of the shangaiData.

<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Analysis3part2finala.PNG" alt='sadad'/>

<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Analysis3part2finalb.PNG" alt='sadad'/>
























