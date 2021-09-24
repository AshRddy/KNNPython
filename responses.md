#Question 1

#Answers :
    a. Testing error rate increases with the higher value because the number of sample where the distance is calculated increases. 
        With the increase in the number of samples, they may result in ambiguity, on what to pick, in this situation KNNClassifier randomly picks one, which may be a wrong guess. 
        Hence with the number of nearest samples increases the rate of error also increases.
    b.  For the lowest K value of 1 the error rate is 0. This is not a reliable term because in the data space the model only makes a prediction based on the first nearest element in the space. 
        It does not make any length calculations for multiple elements and does not make any voting system to predict the value. 
        Hence the rates of lower K values is unreliable.


# Question 2

#Answers:

#Dataset : 
        - Water Potability Dataset, this is a set of data collected from household drinking water using measuring devices from different parts of the world
        - Total Samples ( Total Right Sampels without any missing columns) = 2013 (Individual Samples without any data missing)
###Total Data Frame
        - Samples of Interest (ie. Samples stating that water is  potable for drinking) = 813
        - Smaples not of Interest (ie. Samples stating that water not potable for drinking) = 1200
###Training Dataset :
        - Samples of Interest = 609
        - Sample not of Interest = 1044
        - Total Samples = 1653
###Testing Dataset :  
        - Smaple of Interest = 204
        - Smaple not of Interest = 156
        - Total Samples = 360

#Features in the Dataset :
    
### ph 
        - PH valued defines the acidity level of the water 
        - PH in the range of (6.5–8.5) (Considered for model creation) # Reference : https://www.who.int/water_sanitation_health/dwq/chemicals/ph.pdf (Conclusion part gives the answer)

### Hardness:
        - Harness is the measure of dissolved magnesium and calcium solts in the water. 
        - Measure in the dataset is for milligram of salts in a liter of water
        - Allowed Range is anything below 75 mg/L ref : https://www.healthvermont.gov/environment/drinking-water/hardness-drinking-water
    
### Total dissolved solids : 
        - As per WHO TDS means the total concentration of dissolved substances in the water. 
        - TDS calculates both organic and inorganic matter in the water 
        - As per WHO allowed range is 300 - 700 
        - Reference : https://www.safewater.org/fact-sheets-1/2017/1/23/tds-and-ph

### Chloramines : 
        - Chloramines is the count of disinfectent materials used to make the water consumable, But if the content is little more makes hazardas effects in human health.
        - There are different types of Chloramines; Monochloramine, Dichloramine, Nitrogen Trichloride etc. Ref : https://www.wqa.org/learn-about-water/common-contaminants/chloramine
        - Any chloramine concentration should not be more than 4 - 5 mg/L else its considered not potable. Ref : https://www.wqa.org/portals/0/technical/technical%20fact%20sheets/2014_chloramine.pdf
    
### Sulfate : 
        - Sulfate defines to the add on content to add in sweet or salts in the water
        - They can be of different formats like, Na2So4 (Sodium Sulphate), Ca2SO3 (Calcium Sulphate) etc.
        - WHO recommended sulfate rate is 250 mg/ L ref : https://www.who.int/water_sanitation_health/dwq/chemicals/sulfate.pdf

### Conductivity : 
        - Ability of the water to conduct electricity in water.
        - Pure water has more resistance than the contaminated water which results in lower conductivity for pure water. 
        - Conductivity rate for a pure water should be between 200 to 800 µS/cm Ref : https://sensorex.com/blog/2017/07/12/conductivity-monitoring-reverse-osmosis/#:~:text=Pure%20distilled%20and%20deionized%20water,200%20to%20800%20%C2%B5S%2Fcm

###Organic_carbon : 
        - Propotion of organic carbon or living materials present in the water.
        - Higher organic carbon means the water is contaminated by living organisms which means those are not good for drinking
        - Anywhere betweem 1 - 8 % in a liter of water is okay for a drinking  Ref : https://www.mdpi.com/2504-3900/51/1/35/pdf

### Trihalomethanes : 
        - Chlorinated water will produce some by products those are called the Trihalomethanes 
        - They are of different types and each gov has some rate in their water, this differs with the country to country place to place.
        - Alowed rate as per WHO is 50 - 100 materials/L, countries chose them as per the weather. 

### Turbidity : 
        - Its the amount of insoluble substances such as mud, charcoal etc present in the water. 
        - Higher turbidity is not good for health it may cause kidney stones etc
        - Allowed rate as per the WHO is : 0 - 4 mg/L : https://www.who.int/water_sanitation_health/publications/turbidity-information-200217.pdf

    
## AUC Values

| SN | Features | Score |
|:---|:---------:|:-----:|
|  1 .    | Solids |     0.52061  |
|  2 .    | Turbidity |     0.51320   |
|  3 .    | Chloramines |     0.51275   |
|  4 .    | ph |     0.50825   |
|  5 .    | Hardness |     0.50506   |
|  6 .    | Trihalomethanes |     0.50217   |
|  7 .    | Sulfate |     0.49470   |
|  8 .    | Organic_carbon |     0.49175  |
|  9 .    | Conductivity |     0.48949  |



    
        