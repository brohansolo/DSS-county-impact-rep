# Covid-19 Per-County Severity Analysis


## Intro to Problem Statement
-----------------------------

Moderna, Pfizer, AstraZeneca-Oxford, BioNTech, Sputnik V – These are all names synonymous with hope, hope that one day our world returns to normality.
While leading vaccine researchers and manufacturers lead the charge of coming up with a reliable and functional vaccine, public policy experts are racing to identify the various scenarios around the distribution of these vaccines.

There is strong evidence from companies leading the charge for a working vaccine, that they will have a limited number of vials supply to begin with.
Eg. Pfizer in its first phase of vaccine doses distribution, would only be able to supply the American government with doses enough for 12.5 million people: [How Pfizer Will Distribute Its Covid-19 Vaccine.](https://www.nytimes.com/2020/11/12/business/pfizer-covid-vaccine-coronavirus.html)
This begs the question – **how can we maximise the number of American lives saved by harnessing insights from data and utilizing our understanding of what we know about vaccines and COVID so far?**

Our team, consisting of UCLA Juniors Rohan Bansal, Adhviath Vijay, and UCLA Sophomore Agrim Gupta, attempted to answer this question.


### Methodology and Assumptions
--------------------------------
An study to see which counties have been hardest hit by covid-19 and trying to assess which counties we should prioritize during vaccine distribution.

We started off by brainstorming the role of a vaccine in a pandemic, especially in context of COVID-19 and its recurring cases.
We were able to single out the most important thing a vaccine does – decrease the transmission rate within local communities.
Next, we brainstormed the most wishful impact we would want a vaccine to have on our communities – decrease the death rate.

Keeping both of those things in mind and the fact that we would be working with a limited number of vials, we decided that we would have to prioritize certain sets of population over others in order to maximise the impact of a vaccine.
We set out to find the various parameters based on which we could find and administer vaccines to critical populations.

Firstly, we identified the size of population we would want to conduct this exercise for. 
A state would’ve been too large to conduct this analysis for, a neighbourhood would’ve been too small a sample to gather meaningful data for, so we chose counties. 
It was not only the ideal size, but also something for which we could easily gather data and perform analysis. 

For identifying parameters, the most obvious parameters were death rate among communities. 
We realized that the rate at which death rate changed was heavily correlated with the rate at which the cases were changing. 
So we calculated the first and second and derivatives of the number of cases (rate of change in cases and rate of rate of change in cases respectively) for every single county in the United States.

Next, we sought more comprehensive parameters for identification of critical populations by looking at the documentation being done by relevant authorities like CDC, WHO etc. 
On CDC’s website, we found [numerous such recommended parameters](https://www.cdc.gov/vaccines/imz-managers/downloads/COVID-19-Vaccination-Program-Interim_Playbook.pdf) (visit page 15 of link). We identified the following parameters and made them subject to further analysis:

1. Age of Population
2. Transmission rate
3. Recovery Rate
4. Income
5. Number of hospital beds available
6. Number of hospitals
7. People with pre-existing conditions
8. Habits of mask wearing
9. Anti-vaxx sentiment
10. Number of uninsured people
11. Number of hospitals

Our goal for the next 24 hours was to explore these parameters, and filter out those which were able to provide us with meaningful results.

Some of the assumptions stated in this section and our project overall were:-
1. The first companies to come up with actual supply of vaccines will initially begin with a limited number of supply. 
2. The parameters identified by authorities like CDC and WHO are meaningful and backed by scientific evidence.
3. Census data, data from CMS, CDC, The New York Times, is accurately reported and representative of reality.
4. Any hospital can take up the task of and is equipped for administering vaccines in the particular county it is located in.
5. Demographics like people in prisons, people in colleges etc would have an entirely separate plan of action and distribution chain for COVID vaccines.
6. For national interest purposes, the only demographic a vaccine distribution campaign will deal with is American citizens (thereby validating our use of census.gov data).

## Short Description of the Sources Used
----------------------------------------

1. data.census.gov - The Census Bureau is the leading source of quality data about the demographics of the United States Population and their conditions
2. CMS (Centers for Medicare & Medicaid Services) - Their medicare coverage database provides national information about healthcare coverage for various conditions and insurance costs.
3. [New York Times Daily Updated COVID-Data](https://github.com/nytimes/covid-19-data) 


## Analysis Process
-------------------

We started processing our data by gathering data. 
We began gathering data initially from data.census.gov by using the tools demonstrated by Ms. Ana-Maria Garcia. 
We downloaded those datasets and began combining them on the shared column – FIPS code. 
We aggregated the following parameters for which we found relevant data (all data is per county):

* Population
* Population of elderly (65+)
* Uninsured elderly
* Uninsured elderly with disabilities
* (Median) amount of insurance coverage for pre-existing conditions
* Median Income
* Total households
* Households earning less than 50k
* COVID cases
* COVID deaths
* COVID cases / population
* COVID deaths / population
* Mask wearing habits
* Hospitals per county
* Rate of Change of Cases
* Rate of Change of the Rate of Change of Cases

However, there were certain parameters for which gathering data was either not feasible or unfair. 
We were unable to find the proportion of total hospital beds filled by COVID infected people per county. 
While we were able to find that data for individual states, we had to disregard that data point since we were specifically looking to identify counties. 



## Explanations of Visualizations
---------------------------------

Most of the visualizations we’ve created center around choropleth maps of the United States.
We created interactive maps with each predefined area indicating a US county.
The colors regions represent statistical variables that represent an aggregate summary of a geographic characteristic within each county.

Here are the descripttions of some of those
1. ICU Map - Represents number of ICU beds per county.
2. % Elderly People Map - Gives the ratio of people over the age of 65 for each touny.
3. Number of cases by county
4. Rate of Change of Cases - Tracks how many more cases have 
5. Rate of Change of Rate of Change of Cases


## Why our use of external data stands out
------------------------------------------

1. We address a timely and relevant problem, especially since we’re in the onset of vaccine distribution (granted research still ongoing).
2. We utilize continously updated data and will continue to make change our analysis based on change in COVID cases, new census data etc. 

## Interesting Learnings and Outcomes
-------------------------------------
### Severity Index

Based on the different factors that we were able to find complete and legitimate data for on a county level, we were able to build a means to measure the severity of the situations that are faced by different counties.
The basis of this severity index is the gross amount of deaths that are occuring in the area. 
For each county we correlated the various factors to the death count in that specific county and were able to come out with a general trend that characterizes the situation. 

For example we found that a county with a large amount of elderly people was highly correlated with a higher death rate. 
Similarly we found that as the rate of change of the county case rate increases, the amount of deaths also increases but not very strongly. 
Through the strength of these correlations we’re able to build a severity index where we can plug in various statistics of a county and judge their severity.

Through this severity index we can find out which counties need the most support based on how severe their situations are at the moment.


**Some of the rather interesting things that we learned from doing this project were:**
The combined and normailzed weight of numerous factors paints a far better picture of the severity of COVID in the different counties of the United States as opposed to singled out factors.


## Impact of our Project
------------------------

Projected Numbers: