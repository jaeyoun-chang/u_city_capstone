# Capstone Project: Create a Customer Segmentation Report for Arvato Financial Services

### About the project

This repository is for the final project for the Data Science Nanodegree program at Udacity. The project focuses on utilizing various machine learning techniques to analyze demographic data from both the general population and customers of a sales company.
The project has two primary objectives:

* To understand the characteristics of the company’s customers in comparison to the general population, we will employ machine learning algorithms and datasets provided by Arvato, a mail-order company in Germany.
* The project also involves developing a model that can predict how customers will respond to marketing campaigns.

Through this project, our aim is to gain valuable insights into the customer base of the company and leverage those insights to create an effective marketing strategy.

There are five files associated with this project:
* `Udacity_AZDIAS_052018.csv`: Demographics data for the general population of Germany; 891 211 persons (rows) x 366 features (columns).
* `Udacity_CUSTOMERS_052018.csv`: Demographics data for customers of a mail-order company; 191 652 persons (rows) x 369 features (columns).
* `Udacity_MAILOUT_052018_TRAIN.csv`: Demographics data for individuals who were targets of a marketing campaign; 42 982 persons (rows) x 367 (columns)
* DIAS Information Levels - Attributes 2017.xlsx: a top-level list of attributes and descriptions, organized by informational category
* DIAS Attributes - Values 2017.xlsx: a detailed mapping of data values for each feature in alphabetical order

Please find the complete project report in [my blog](https://medium.com/@jaeyoun.chang/customer-segmentation-report-for-arvato-financial-services-e3a34ec5293a)

## Requirements
The Jupyter Notebook is written in Python (3.x. version required).

In addition to general modules like numpy, pandas, matplotlib, seaborn and sklearn,  
you need to install matplotlib.ticker, Image from IPython.display, missingno,  
Translator from googletrans, Levenshtein, pyarrow, pyarrow.parquet, pickle and tqdm by  
```bash
pip install matplotlib.ticker  
pip install IPython  
pip install missingno  
pip install googletrans==4.0.0-rc1  
pip install python-Levenshtein  
pip install pyarrow  
pip install pickle-mixin  
pip install tqdm  
```
To avoid complication, several custom functions are also used as noted in Jupyter Notebook.

## Acknowldgements
Special thanks to Udacity for this great course and project!