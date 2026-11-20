# IS 477 Course Project: Status Report

**Project:** Exploring Artistic Trends and Exhibitions at the Art Institute of Chicago

**Date:** November 19, 2026

## 1. Changes to Project Plan 

Since submitting our original project plan, we received feedback regarding the consistency of artwork classification labels across datasets. Our instructor pointed out that artworks may be described using different terminology, such as "1950s," "mid-century modern," or "abstract." These labels can refer to different characteristics, including time periods, artistic movements, and styles, which could make comparisons difficult.

To address this feedback, we plan to incorporate classification standardization into our data cleaning process. We will review the available style and classification fields, identify inconsistencies, and develop a working vocabulary or mapping dictionary. This will help us standardize comparable terminology while maintaining distinctions between different types of classifications.

We have also adjusted our project timeline to reflect our current progress. While data collection has been completed and an initial data quality assessment has begun, the remaining cleaning, integration, analysis, and automation tasks are still pending. Our overall research question and project goals remain unchanged.


## 2. Task Updates and Progress

The group has made progress on the project, completing the initial data collection stage and beginning the data quality assessment. As of November 19, the group has not yet started data cleaning, integration, or analysis.

For **data collection**, Jodi and Saint were responsible for gathering and organizing the three datasets from the Art Institute of Chicago's Open Data API: Artworks, Agents, and Exhibitions. Python was used to download 200 records from each dataset and convert the original JSON data into CSV format using pandas. The datasets were uploaded to the GitHub repository, along with the Python script used to retrieve them.

- [Data download script](download_data.py)
- [Artworks dataset](data/artworks.csv)
- [Agents dataset](data/agents.csv)
- [Exhibitions dataset](data/exhibitions.csv)

For **data quality assessment**, Deeya began examining the datasets by creating and running a Python script that identifies dataset dimensions, missing values, duplicate records, and available columns. The results will help the group identify potential data quality issues and determine which fields require additional cleaning.

- [Data quality assessment script](data_quality.py)
- [Data quality assessment results](data_quality_results.txt)

For **data cleaning**, Rachel and Saint will focus on addressing missing information, standardizing data formats, and preparing the datasets for integration. Based on instructor feedback, this stage will also include developing a working vocabulary to standardize comparable artwork classification terminology.

During **data integration**, Deeya and Jodi will work on connecting the three datasets using shared artwork and artist identifiers. Before completing the joins, the group will evaluate identifier overlap to determine whether the current samples contain enough matching records.

For **analysis**, Deeya and Saint will examine the integrated data to identify patterns in artist and art-style representation across exhibitions. This stage will also include creating visualizations to communicate the findings.

The remaining tasks will include developing a reproducible workflow, completing documentation, and conducting a final review before submission.


## 3. Updated Timeline


The group has revised the original timeline to reflect our current progress and the additional classification standardization work identified through instructor feedback.

| Timeline | Task | Responsible | Status |
|---|---|---|---|
| Oct. 19–25 | Data Collection | Jodi, Saint | Completed |
| Nov. 19–21 | Data Quality Assessment | Deeya, Rachel | In Progress |
| Nov. 21–23 | Data Cleaning and Classification Standardization | Rachel, Saint | Pending |
| Nov. 23–26 | Data Integration | Deeya, Jodi | Pending |
| Nov. 26–29 | Analysis and Visualizations | Deeya, Saint | Pending |
| Nov. 29–Dec. 2 | Automation & Documentation | Jodi, Rachel | Pending |
| Dec. 3–6 | Final Review | All Members | Pending |

Our group will prioritize data quality assessment and integration before proceeding with analysis. If the initial datasets contain insufficient matching records, we will consider expanding the sample or adjusting the scope of our analysis.

These revised dates will be confirmed with the group to ensure that responsibilities and deadlines remain manageable.


## 4. Challenges and Solutions


### Inconsistent Classification Terminology

One challenge identified through instructor feedback is the potential inconsistency of artwork classification labels. Different terms may describe an artwork's historical period, movement, or style, making it difficult to compare classifications across records.

To address this, we plan to develop a working vocabulary or mapping dictionary that standardizes comparable terms while preserving meaningful distinctions. We will document the original classifications and any changes made during cleaning.

### Limited Dataset Overlap

Our group initially downloaded 200 records from each dataset. However, because the records were collected from the first pages of the API, there may not be enough overlapping artist and artwork identifiers to support meaningful integration.

To address this, we will examine identifier overlap before joining the datasets. If the number of matching records is too small, we will consider expanding the dataset samples or narrowing the scope of our analysis.

### Missing Values and Data Formatting

The three datasets contain different types of information, and some fields may contain missing values or multiple identifiers. These differences could complicate cleaning and integration.

We have begun addressing this challenge through an initial data quality assessment that identifies missing values, duplicate records, and available columns. Our next step is to review these findings and determine which fields require additional cleaning or restructuring.

### Project Timeline

Although initial data collection has been completed, several stages originally scheduled for earlier in the semester remain unfinished.

To address this, we have revised the project timeline and identified the remaining responsibilities for each group member. We will prioritize essential data preparation, integration, and analysis tasks to keep the project manageable before the final submission.



## 5. Individual Contributions — All Members

### Jodi Domingo

Contributed to the initial data collection by developing a Python script to retrieve records from the Art Institute of Chicago's API and converting the datasets into CSV format. Helped organize the data files in the GitHub repository and contributed to the original project plan by documenting dataset descriptions and potential limitations.

### Deeya Patel

Contributed to the original project plan by developing the project timeline, organizing tasks, and assigning responsibilities across the group. For the status report milestone, created and ran a Python script to begin assessing data quality across the three datasets. Also helped revise the timeline and identify next steps based on instructor feedback.

### Saint Luan

Contributed to the initial project planning and data collection responsibilities, including organizing the datasets needed for analysis. Helped establish the planned approach for examining artistic trends and identifying potential challenges with dataset compatibility. Also worked on the constraints for the Plan submission and focused on setting the tag correctly. Will focus on data cleaning, classification standardization, and analysis during the remaining stages.

