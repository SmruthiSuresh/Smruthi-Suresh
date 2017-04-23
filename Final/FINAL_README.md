# Analysis 2.
#### Analysis in this question has been split up in 2 parts
## Part 1: Variation in the ranking of Northeastern University from 2005 to 2015.
## Part 2: A radar chart showing the score that Neu was given in terms of research, income, citations,teaching, international.
#### VARIATION IN RANKING OF NEU FROM 2005 TO 2015
### Part 1:
#### •	All the three files (times data,cwurdata and shangaiData) are read
#### •	Name of university is set to Northeastern Unievrsity like(myuniv name=['Northeastern University'])
#### •	All the university names from all the three data are made into a list by using the union fucntion between cwur, shangaiData and timesData 
#### •	Under the dictionary all_universities_names_list.
#### •	All unique university names are sorted and then printed.
#### •	To get the rank , the first digit of the rank is parsed in all three files.
#### •	Only the first digit is parsed to get the date ranges.
#### •	Styling is done on the data

<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Ana2PArt1img.PNG" alt='sadad'/>

### Part 2: A radar chart showing the score that Neu was given in terms of research, income, citations,teaching,
international only for the year 2016.
#### •	Necessary libraries like matplotlib.path, matplotlib.pyplot and matplotlib.patches are imported.
#### •	Data of timesData is read
#### •	Factors that we would like to condiser in making the radar chart like teaching, international, citations, research and income are 
#### •	taken into a list named "properties".
#### •	Set the text of the title of the radar graph by joining both the university name and the year by using the "join" fucntion.
#### •	The radar graph is plotted by setting the axis plot as polar.

#### •	The radar graph shows the different properties of Northeastern defined in the dictionary for the year 2016.

<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Anal%202%20part%202img.PNG" alt='sadad'/>



# Analysis 3
## Part 1: Analyzing the difference in quality of Education is represented by plotting a seaborn plot.
## Part 2: Analyzing the difference in ranking from 2011 to 2015 for the top 81 universities in terms of the shanghaiData.

### Part 1:
#### •	Analysis is done on the cwur rankings file
#### •	Firstly the file is read
#### •	Function that returns the quality of educaiton is defined
#### •	A dataframe containing worldrank,country and quality of education of USA ad UK is defined
#### •	USA is passed as the argument to the funciton so that the quality of education of only the universities in USA is considered
#### •	A seaborn plot showing the quality of education of both UK and USA is plotted



<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Analysis3Part1.PNG" alt='sadad'/>


<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Anal3Part1b.PNG" alt='sadad'/>

### Part 2: Analysing the difference in ranking from 2005 to 2015 for the top 81 universities

#### •	The shangaiData is read
#### •	All the universities of the shanghaiData are considered.
#### •	Only top 81 universities are taken for the analysis.
#### •	Using the sns the plot is generated
#### •	A Unique university names and ranks are considered
#### •	A variable called var is first initialized to -1
#### •	It is compared with the rank's last digit to find which range of rank the universisty lies in
#### •	Depending on that the variable is incremented
#### •	A darkgrid theme of seaborn is used to plot the rankigns of the universities from 2011 to 2015 of the shangaiData.


<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Analysis3part2finala.PNG" alt='sadad'/>

<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Analysis3part2finalb.PNG" alt='sadad'/>




# Analysis 4
## Part 1 : TimesData is analysed and the difference in the income between USA and East Asian Countries's universities are plotted
## Part 2 : Plots between density and income is plotted.. Mean Income density of USA, JAPAn, Mixed income density is calculated.

### Part1:
#### •	Data of USA , Korea, China and Korea are selected.
#### •	All the universities in these countries without any income field are dropped.
#### •	Separate bar plots for China,Korea, Japan, USA are represented with their respective income values against the percentage of the number of universities with that income.

<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/analysis4part1.PNG" alt='sadad'/>

### Part 2:

#### Income is plotted in the x axis and the density in the y axis for the meand density of  Japan, US and mixed mean densities.

<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/analysis4part2.PNG" alt='sadad'/>

<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/analysis4part2b.PNG" alt='sadad'/>

# Analysis 1:
#### •	The data from timesData is read
#### •	École Polytechnique Fédérale de Lausanne University is considered for this analysis
#### •	World Rank, Total score, research and international are converted to float.
#### •	A plot is made that shows the world ranking of Polytechnique university from 2011 to 2016.

<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Analysis1%20part1a.PNG" alt='sadad'/>



Ranking vs total score is also plotted
<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Analysis1Part1b.PNG" alt='sadad'/>


#### A bar graph is also plotted that shows the quality of teaching, research etc throught the 5 years
#### Plotting a bar graph to show the quality of teaching,research, citations etc from 2011 to 2016.

<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Analysis1Part1b1.PNG" alt='sadad'/>

#### All 4 graphs(income, research, teaching, citations) is plotted.

<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/Analysis1part2a.PNG" alt='sadad'/>

# Analysis 5:
## Part 1: Only Data science Programs are analysed and their scores are found.
## Part 2: Difference between the Score valuesof cwur, Times and Shangai data are represented.

### Part 1:

#### •	A list of all the data-science programs are got from  this link "http://datascience.community/colleges" and is saved in the variable programs.
#### •	A 'checkuniv' funciton is defined 
#### •	If a program in the list of porograms defined matches programs in the cwur data then only the score of those universities with Data Science programs is considered.

<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/analysis5part1.PNG" alt='sadad'/>

### Part 2:
#### •	Cwur file is read
#### •	University scores of all years are grouped based on the name of the University.
#### •	Scores of cwur, Shanghai and Times Data as a whole are compared and plotted.
#### •	Universities with Nan values of scores are not considered in the analysis...if not np.isnan(x) is used to do the same.

<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/analysis5part2a.PNG" alt='sadad'/>

#### Boxplot is also done to show the difference in scores of cwur,times and shangaiData.
<img 
src="https://github.com/SmruthiSuresh/Smruthi-Suresh/blob/master/analysis5part2b.PNG" alt='sadad'/>
