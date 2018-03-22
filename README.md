# EDGAR-Crawling-using-Python
Simple API to extract the text files from EDGAR website forms

Steps to be followed: (Data for form 10-K and January 2017)

1) Get the form.gz data from (https://www.sec.gov/Archives/edgar/full-index/2017/QTR1/) which contained data of Form Type, Company Name, CIK, Date Filed, and File Name (path of the file in the database)

2) Run api.py to extract the file names on the basis of conditions as per your need.

3) Save the data to directory in text format

Its the basic code, you can make it more useful by changing the condition as input element, where you can enter the conditions as per the requirement.
