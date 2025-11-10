# Azure-ETL-Portfolio-Project-Python-Blob-SQL-Power-BI-

End-to-end data analytics project using Azure Blob Storage, Azure SQL Database, Python ETL pipelines, and Power BI.
Includes a fully implemented star schema, automated ETL, and an interactive dashboard.

# Technologies

Python — Cleaning, transformation, dimension & fact creation

Azure Blob Storage — Raw and cleaned data storage

Azure SQL Server / SQL Database — Data warehouse (star schema)

Power BI — Visualization and reporting

# Dataset

Sample Superstore Dataset
Source: [Kaggle (vivek468/superstore-dataset-final)](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final/data)

This dataset contains sales, customer, product, and geographic information. The goal of the project was to take a raw CSV file and transform it into a clean, reliable, analytics-ready data model following a proper star-schema architecture.
The project started by uploading the Superstore dataset to Azure Blob Storage, which served as the central place to store both the raw file and any cleaned versions. From there, I used Python to clean and prepare the data: fixing column names, converting data types, removing inconsistencies, and creating additional fields like delivery days, profit ratio, and date-based attributes.

After preparing the data, I loaded everything into Azure SQL Database to build a proper star-schema data model. The dimensions (customer, product, date, location, shipping, and orders) and the main fact table were inserted.
Once the warehouse was ready, I connected Power BI to Azure SQL and built the dashboard.
