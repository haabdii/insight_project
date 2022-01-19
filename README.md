# Predicting NBA Knee Injuries 
At Insight, I built a simple ML model for predicting knee injuries in NBA. In what follows, I describe different steps of the project.

## Use Case 
Injuries significantly lower a team's odds of success. Assume you are an NBA team manager and you have a tool that predicts the risk of injury of your players. Now, you can prepare for worst case scenarios by training backups for players at high risk of injury. You also have the option to not to hire a player who is at high risk of injury. At Insigt, I decided to take a shot at building a ML model for predicting knee injuries (i.e. most common injury in NBA). For the first iteration of the model, my goal was to beat random guess. 

## Data Collection
I scarrped data from NBA databases. First, I collected all the injury reports from 2010 to 2018 from "prosportstransactions.com". Here is an example of an injury report: 


![](Figures/lebron_james_injuries.png)

I also collected data such as weight, height, date of birth, start year of career, end year of career and position on all the players who played within 2010 and 2018 timespan (~ 1000 players). Below is an example of that: 

![](Figures/lebron_james_info.png)

I cleaned these two datasets and joined them so I could analyze the data. 

## Data Analysis 

The most frequent injury in NBA is knee injury. 

![](Figures/all_injuries.png)

Forwards are at a higher risk of knee injuries than the players who play other positions. 

![](Figures/knee_injury_position.png)

One important feature is the "total years played". It turns out that the median injured player has played four years longer than the median uninjured player. 

![](Figures/number_years_played_hist.png)

In addition, the history of the past injuries matter. The risk of re-injury is consistently higher than the risk of injury. If you get injured once, you are more likely to get injured again. 

![](Figures/risk_injury_reinjury.png)

## Modeling
I used logistic regression to predict the risk of knee injury. It is a great option for binary classification (injured vs uninjured) and it outputs the probablity of belonging to each class. Each year the number of uninjured players were approximately 20 times the number of injured players. I upsampled the minority class to balance the dataset. Below is a simple demonstration of how the model works:

![](Figures/model.png)

I decided to use F-1 score as the success metric since we need to minimize both the false positives and the false negatives. The figure below shows that at the optimal treshhold, the logistic regression model performs 2.5x better than random guess. I would call this a successful first iteration!  

![](Figures/model_performance.png)

