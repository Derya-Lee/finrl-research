
Guide me writting the methodology section for my dissertation, providing references when appropriate or necessary.
In my methodology I need to explain the research procedures, methods and methodologies I used. These are the steps I followed: I searched about what AI techniques are available, if AI use human behaviour related data or effected by it. 
I also looked at what AI techniques are more common and one I can use. Deep Reinforcement Learning made sense to use for my dissertation, because it involves learning from patterns (I don't know if the others do), also found the Ensemble Strategy paper by Yang et. al. I am not researching about what model (A2C, PPO, DDPG) is the best; but by combining different models helps provide control and or avoid bias (for example, if the results show consistent failure distinguishing noise and turbulence or sentiment, it could be due to one particular model).
Using the example provided by the ensemble paper I have generated a phyton code (I have made changes, which I will cover in more detail in Data section - or advice if I should do so in this section.) 
Also advice me if I should mention here what my qualitative and quantitative, primary or secondary data are? Help me identify what they refer to in my case.

This is the list of papers I looked, some were suggested by you, and some I have attached in our previous converations. While I don't have to use all these papers, or limited to this list, I need to extract references to support different sections of my dissertation.

1.
“Rise of the machines? Intraday high-frequency trading patterns of cryptocurrencies"
Alla A. Petukhina, Raphael C. G. Reule & Wolfgang Karl Härdle

https://doi.org/10.1080/1351847X.2020.1789684

2.
"Deep Reinforcement Learning for Automated Stock Trading: An Ensemble Strategy"
Hongyang Yang, Xiao-Yang Liu, Shan Zhong, Anwar Walid

https://doi.org/10.1145/3383455.3422540

3.
"An-Application-of-Deep-Reinforcement-Learning-to-Algorithmic-Trading"
By Thibaut Théate and Damien Ernst  (2020)
https://doi.org/10.1016/j.eswa.2021.114632

4.
"High-Frequency Jump Analysis of the Bitcoin Market Olivier Scaillet" 
 Adrien Treccani 2 and Christopher Trevisan 
doi: 10.1093/jjfinec/nby013

5.
"Machine learning in financial markets: A critical review of algorithmic trading and
risk management"
Wilhelmina Afua Addy , Adeola Olusola Ajayi-Nifise, Binaebi Gloria Bello, Sunday Tubokirifuruar Tula

https://doi.org/10.30574/ijsra.2024.11.1.0292

6. 
“FinRL: A Deep Reinforcement Learning Library for Automated Stock Trading”
Xiao-Yang Liu, Hongyang Yang, Qian Chen, Runjia Zhang, Liuqing Yang, Bowen Xiao, Christina Dan Wang

7.
"Algorithmic Trading and AI: A Review of Strategies and Market Impact"
Wilhelmina Afua Addy,  Adeola Olusola Ajayi-Nifise, Binaebi Gloria Bello, Sunday Tubokirifuruar Tula,

https://doi.org/10.30574/wjaets.2024.11.1.0054

8.
"Deep Reinforcement Learning for Automated Stock Trading: An Ensemble Strategy"
Yang et al. 2021
https://doi.org/10.1145/3383455.3422540

9.
Unconscious Herding Behavior as the Psychological Basis of Financial Market Trends and Patterns
Robert R. Prechter Jr.

https://doi.org/10.1207/S15327760JPFM0203_1

10.
"Algorithmic Trading and Financial Forecasting Using Advanced Artificial Intelligence Methodologies"
Gil Cohen (2022)

https://doi.org/10.3390/math10183302

11.
"An Analytical Examination of Sharpe Ratio, Sortino Ratio, and Jensen's Alpha in Portfolio Performance Evaluation"
https://www.adarie.com/articles/16

12.  
"Explainable AI for Psychological Profiling from Financial Data"
Ramon et al. (2021)



titles only:
“Deep Reinforcement Learning in High Frequency Trading”
“Deep Reinforcement Learning for Cryptocurrency Trading”
“Cryptocurrency Trading with Deep Learning and Sentiment Analysis”
“Transformer-based Deep Reinforcement Learning for Cryptocurrency Trading”


                   metric , mean_diff , median_diff , positive_windows  
        annualized_sharpe ,  0.043803 ,    0.057326 ,               13   
    annualized_volatility , -0.003583 ,   -0.001320 ,               11   
       annualized_sortino ,  0.188427 ,    0.145904 ,               13   
             max_drawdown ,  0.028247 ,    0.004790 ,               13   
  total_return-annualized ,  0.182927 ,    0.023420 ,               12   

  negative_windows,    t_stat,   p_value  
                 9,  0.229238,  0.820902  
                11, -0.124148,  0.902379  
                 9,  0.619673,  0.542139  
                 9,  1.733296,  0.097703  
                10,  1.115922,  0.277062  


annualized_sharpe
annualized_volatility
annualized_sortino
max_drawdown
total_return-annualized



Exp 2
Simple reg

Provided below is the regression results for annualized sortino and max-drawdown, run individually and in multiple regression. Please provide an explanation for all, and  provide a text for the data analysis section. 
Sortino -> Volatility
Model 	Variable 	coef 	std err 	t 	p>|t| 	[0.025 	0.975]
0 	Model 	Intercept 	2.5829 	2.0796 	1.24 	0.2142 	-1.4931 	6.6589
1 	Model 	Q('Volatility_ann') 	-2.8802 	3.3124 	-0.87 	0.3846 	-9.3723 	3.6119
2 	Model 	R-squared 	0.0440 					
3 	Model 	Adj. R-squared 	-0.0030 		

Sortino -> Turbulence
Model 	Variable 	coef 	std err 	t 	p>|t| 	[0.025 	0.975]
0 	Model 	Intercept 	-2.8900 	3.8106 	-0.76 	0.4482 	-10.3586 	4.5786
1 	Model 	Q('Turbulence_ann') 	0.5914 	0.6369 	0.93 	0.3531 	-0.6568 	1.8396
2 	Model 	R-squared 	0.1160 					
3 	Model 	Adj. R-squared 	0.0720 					

 Multiple regression result for Annualized Sortino 
  	Model 	Variable 	coef 	std err 	t 	p>|t| 	[0.025 	0.975]
0 	Model 	Intercept 	-1.2255 	4.2553 	-0.29 	0.7733 	-9.5657 	7.1146
1 	Model 	Q('Volatility_ann') 	-2.5719 	3.6322 	-0.71 	0.4789 	-9.691 	4.5471
2 	Model 	Q('Turbulence_ann') 	0.5688 	0.5839 	0.97 	0.33 	-0.5756 	1.7132
3 	Model 	R-squared 	0.1510 					
4 	Model 	Adj. R-squared 	0.0620 	

Max_Drawdown -> Volatility
Model 	Variable 	coef 	std err 	t 	p>|t| 	[0.025 	0.975]
0 	Model 	Intercept 	0.0626 	0.0432 	1.45 	0.1468 	-0.022 	0.1473
1 	Model 	Q('Volatility_ann') 	0.4158 	0.0717 	5.8 	0.0 	0.2753 	0.5564
2 	Model 	R-squared 	0.5900 					
3 	Model 	Adj. R-squared 	0.5700 		

Max_Drawdown -> Turbulence
Model 	Variable 	coef 	std err 	t 	p>|t| 	[0.025 	0.975]
0 	Model 	Intercept 	0.1711 	0.1179 	1.45 	0.1467 	-0.06 	0.4022
1 	Model 	Q('Turbulence_ann') 	0.0216 	0.0197 	1.09 	0.2735 	-0.017 	0.0601
2 	Model 	R-squared 	0.0980 					
3 	Model 	Adj. R-squared 	0.0530 		

Experiment 2 Multiple regression result for Max_Drawdown 
 	Model 	Variable 	coef 	std err 	t 	p>|t| 	[0.025 	0.975]
0 	Model 	Intercept 	-0.1069 	0.0666 	-1.6 	0.1086 	-0.2375 	0.0237
1 	Model 	Q('Volatility_ann') 	0.4296 	0.0562 	7.64 	0.0 	0.3194 	0.5397
2 	Model 	Q('Turbulence_ann') 	0.0253 	0.0072 	3.5 	0.0005 	0.0111 	0.0395
3 	Model 	R-squared 	0.7250 					
4 	Model 	Adj. R-squared 	0.6960 			

EXP.2 combined results

| Model                 | Predictor       | Coef. | t-stat | p-value | R²   | Adj. R² |
| --------------------- | --------------- | ----- | ------ | ------- | ---- | ------- |
| Sharpe → Volatility   | Volatility\_ann | –0.81 | –0.91  | 0.37    | 0.07 | 0.02    |
| Sharpe → Turbulence   | Turbulence\_ann | 0.89  | 1.21   | 0.23    | 0.12 | 0.08    |
| Sortino → Volatility  | Volatility\_ann | –2.88 | –0.87  | 0.38    | 0.04 | –0.00   |
| Sortino → Turbulence  | Turbulence\_ann | 0.59  | 0.93   | 0.35    | 0.12 | 0.07    |
| Max DD → Volatility   | Volatility\_ann | 0.42  | 5.80   | 0.00    | 0.59 | 0.57    |
| Max DD → Turbulence   | Turbulence\_ann | 0.02  | 1.09   | 0.27    | 0.10 | 0.05    |
| Max DD → Vol. + Turb. | Vol., Turb.     | sig.  | —      | <0.01   | 0.73 | 0.70    |

Provided below is the regression results for annualized sharp, sortino and max-drawdown using normalized Fear & Greed data (mean value taken over each window). Please provide an explanation for all 3 simple regressions, and provide a text for the data analysis section, including any table / figure useful to show alongside. 

Experiment 3. Simple Regressions for Annual sharp -> Fear & Greed normalized (mean)
Model 	Variable 	coef 	std err 	t 	p>|t| 	[0.025 	0.975]
0 	Model 	Intercept 	0.6954 	0.3177 	2.19 	0.0286 	0.0728 	1.3181
1 	Model 	Q('FG_norm_mean') 	3.4410 	1.2118 	2.84 	0.0045 	1.0659 	5.8161
2 	Model 	R-squared 	0.4030 					
3 	Model 	Adj. R-squared 	0.3730 					

Experiment 3. Simple Regressions for Annual Sortino -> Fear & Greed normalized (mean)
Model 	Variable 	coef 	std err 	t 	p>|t| 	[0.025 	0.975]
0 	Model 	Intercept 	1.2528 	0.5222 	2.4 	0.0164 	0.2292 	2.2763
1 	Model 	Q('FG_norm_mean') 	5.2052 	1.7432 	2.99 	0.0028 	1.7886 	8.6219
2 	Model 	R-squared 	0.3680 					
3 	Model 	Adj. R-squared 	0.3360 	


Experiment 3. Simple Regressions for Annual Maxdrawdown ->  Fear & Greed normalized (mean)
 	Model 	Variable 	coef 	std err 	t 	p>|t| 	[0.025 	0.975]
0 	Model 	Intercept 	0.3029 	0.0241 	12.57 	0.0 	0.2557 	0.3502
1 	Model 	Q('FG_norm_mean') 	-0.0874 	0.1133 	-0.77 	0.4403 	-0.3095 	0.1346
2 	Model 	R-squared 	0.0730 					
3 	Model 	Adj. R-squared 	0.0260 		


4.1 Data Collection - 	,679
4.2. Data Analysis -, 1076	
4.3 Experiment Comparisons -, 420	
4.4 Regression Results - ,567	
4.5 Summary - Findings Across Experiments ,215
,