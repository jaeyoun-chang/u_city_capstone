# Capstone Project: Create a Customer Segmentation Report for Arvato Financial Services

### About the project

This repository is for the final project of Udacity's Data Science Nanodegree program.  

There are 2 main goals in the project:  
using machine learning algorithms and datasets provided by Arvato, a mail-order sales company in Germany, 
* the characteristics of the company's customers compared to general republic should be clarified  
* a forecasting model to predict customers' response for a marketing campaign needs to be developed

### Part 0 - Data understanding and pre-processing

There are 5 datasets given:
* 3 dataset files
  - azdias: demographic data for the general population of Germany; 891 211 persons x 366 features  
  - customers: demographic data for customers of the company; 191 652 persons x 369 features  
  - mailout : demographic data for individuals targets of a marketing campaign; 42 982 persons x 367 features
* 2 reference files  
  - ref_info (DIAS Information Levels): a top-level list of attributes and descriptions in Excel.
    This file is to explain dataset features in unreadable German acronyms.  
  - ref_attr (DIAS Attribute): a detailed mapping of data values for each feature in alphabetical order in Excel.  
    This file is to clarify the meanings of dataset Scores in numbers and acronyms.

As the datasets do not have information on what column features and values exactly mean,  
3 steps were taken before finalizing pre-processing:
* step1: Baseline-understanding 
  - feature alignment among dataset and reference files was checked and improved  
  - 2 reference files were upgraded and cleaned to be used in the following sections
  - by analyzing ref_info, overall structure of datasets were studied
  - by analyzing ref_attr, contents of datasets were checked.
    At this stage the baseline of pre-processing items were made including data catagories (discrete or continuous) by feature, values to be replaced as null, etc.
* step2: Dataset exploration 
  - based on framework findings from step1, step2 analyzed actual datasets and refined findings.  
  - data catagories of features were adjusted, each continuous feature was deep-dived for possible pre-processing and the outlines of pre-processing in step1 were checked in detail.
* section3: Pre-processing
  - pre_processing items noted in step 1 and 2 were used
  - after pre-processing columns and rows with excessive missing values were removed 

|    | index                            | method      | by_feature                                                         |
|---:|:---------------------------------|:------------|:-------------------------------------------------------------------|
| 16 | 3.1.2-dtype                      | astype      | All features in numeric_discrete_features / change dtype to float  |
| 19 | 3.2.2-EINGEFUEGT_AM              | astype      | EINGEFUEGT_AM / change dtype to datetime only with year values     |
|  0 | 2.3.1-drop                       | drop        | All / drop features in to_drop                                     |
|  4 | 3.1.1-ANZ_HAUSHALTE_AKTIV        | log_scaling | ANZ_HAUSHALTE_AKTIV                                                |
|  8 | 3.1.1-KBA13_ANZAHL_PKW           | log_scaling | KBA13_ANZAHL_PKW                                                   |
| 17 | 3.2.1-ANZ_STATISTISCHE_HAUSHALTE | log_scaling | ANZ_STATISTISCHE_HAUSHALTE                                         |
|  2 | 2.3.1-to_null                    | mask        | All / replace Score to null if corresponding Meaning is in to_null |
|  3 | 2.3.1-unknown_9                  | mask        | category_small in unknown_9 / Score 9 to -1                        |
|  5 | 3.1.1-ANZ_PERSONEN               | np.where    | ANZ_PERSONEN / Score > 10 to -1                                    |
|  6 | 3.1.1-ANZ_TITEL                  | np.where    | ANZ_TITEL / Score of ANZ_PERSONEN > 10 to -1                       |
|  7 | 3.1.1-GEBURTSJAHR                | np.where    | GEBURTSJAHR / Score < 1900 to -1                                   |
| 18 | 3.2.1-EINGEZOGENAM_HH_JAHR       | np.where    | EINGEZOGENAM_HH_JAHR / Score < 1980 to -1                          |
|  1 | 2.3.1-minus1                     | replace     | All / {-1: np.nan}                                                 |
|  9 | 3.1.1-LP_FAMILIE_FEIN            | replace     | LP_FAMILIE_FEIN / {0: -1}                                          |
| 10 | 3.1.1-LP_FAMILIE_GROB            | replace     | LP_FAMILIE_GROB / {0: -1}                                          |
| 11 | 3.1.1-LP_LEBENSPHASE_FEIN        | replace     | LP_LEBENSPHASE_FEIN / {0: -1}                                      |
| 12 | 3.1.1-LP_LEBENSPHASE_GROB        | replace     | LP_LEBENSPHASE_GROB / {0: -1}                                      |
| 13 | 3.1.2-CAMEO_DEUG_2015X           | replace     | CAMEO_DEUG_2015 / {"X": -1}                                        |
| 14 | 3.1.2-CAMEO_DEU_2015             | replace     | CAMEO_DEU_2015 / {"XX": -1}                                        |
| 15 | 3.1.2-CAMEO_INTL_2015XX          | replace     | CAMEO_INTL_2015 / {"XX": -1}                                       |

### Part 1 - Customer Segmentation Report

<!-- ![cluster_number_elbow](./cluster_number_elbow.png) -->

<img align="left" width="800" height="500" src="./cluster_number_elbow.png">

<img align="left" width="800" height="500" src="./cluster_chart.png">

<!-- ![cluster_chart](./cluster_chart.png) -->

this section focuses on the reference files that can help in understanding dataset contents.

This section aims to understand outlines of the 2 datasets and identify baseline factors.  

* libraries used, the motivation for the project, the files in the repository with a small description of each
* a summary of the results of the analysis, and necessary acknowledgements
* the Project Definition, Analysis, and Conclusion

pip install googletrans==4.0.0-rc1
pip install missingno
pip install pyarrow
custom modules for convenience are in root folder

### Datasets

* Udacity_AZDIAS_052018.csv:  
  Demographics data for the general population of Germany; 891 211 persons (rows) x 366 features (columns)
* Udacity_CUSTOMERS_052018.csv:  
  Demographics data for customers of a mail-order company; 191 652 persons (rows) x 369 features (columns)
* Udacity_MAILOUT_052018_TRAIN.csv:  
  Demographics data for individuals who were targets of a marketing campaign; 42 982 persons (rows) x 367 (columns)
* DIAS Information Levels: a top-level list of attributes and descriptions in Excel
* DIAS Attribute: a detailed mapping of data values for each feature in alphabetical order in Excel