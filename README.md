# Capstone Project: Create a Customer Segmentation Report for Arvato Financial Services

* libraries used, the motivation for the project, the files in the repository with a small description of each
* a summary of the results of the analysis, and necessary acknowledgements
* the Project Definition, Analysis, and Conclusion

### About the project

This repository is for the final project of Udacity's Data Science Nanodegree program.  

There are 2 main goals in the project:
using machine learning algorithms and datasets provided by Arvato, a mail-order sales company in Germany, 
* the characteristics of the company's customers compared to general republic should be clarified  
* a forecasting model to predict customers' response for a marketing campaign needs to be developed

### Datasets

* Udacity_AZDIAS_052018.csv: Demographics data for the general population of Germany; 891 211 persons (rows) x 366 features (columns)
* Udacity_CUSTOMERS_052018.csv: Demographics data for customers of a mail-order company; 191 652 persons (rows) x 369 features (columns)
* Udacity_MAILOUT_052018_TRAIN.csv: Demographics data for individuals who were targets of a marketing campaign; 42 982 persons (rows) x 367 (columns)
* DIAS Information Levels: a top-level list of attributes and descriptions in Excel
* DIAS Attribute: a detailed mapping of data values for each feature in alphabetical order in Excel

### Part 0 - Data understanding and pre-processing

There are 5 datasets given:
* 3 dataset files - azdias, customers and mailout
* 2 reference files - ref_info and ref_attr:  
  - ref_info (DIAS Information Levels) is to explain dataset features in unreadable German acronyms  
  - ref_attr (DIAS Attribute) is to clarify the meanings of dataset Scores in numbers and acronyms

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

### Part 1 - Data understanding and pre-processing


this section focuses on the reference files that can help in understanding dataset contents.

This section aims to understand outlines of the 2 datasets and identify baseline factors.  
