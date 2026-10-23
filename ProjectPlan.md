
# IS 477 Course Project Plan

## 1. Overview
Our project aims to examine how the representation of artists and art styles varies across exhibitions at the Art Institute of Chicago. By analyzing the relationships between artworks, artists, and exhibitions, we hope to identify patterns in which artists and artistic styles are featured.

To accomplish this, we will use three datasets from the Art Institute of Chicago's Open Data API: Artworks, Agents, and Exhibitions. We will first assess data quality, identify missing or inconsistent information, and clean the datasets. Next, we will integrate them using shared artist and artwork identifiers. Once integrated, we will analyze patterns across exhibitions and create visualizations to present our findings.

Our goal is to develop a reproducible data curation workflow while gaining insight into how artistic representation differs across exhibitions.

## 2. Team
- Member 1: Jodi Domingo — Used Python to download 200 records from each of the Artworks, Agents, and Exhibitions datasets, converted the JSON data into CSV format, and uploaded the files to the GitHub repository's data folder. Updated the dataset information in ProjectPlan.md and added the Gaps section to address potential challenges with missing data, sample size, and dataset integration.
- Member 2: Rachel Tseng — [Responsibilities]
- Member 3: Deeya Patel — [Responsibilities]
- Member 4: [Name] — [Responsibilities]

## 3. Research or Business Questions
How does the representation of different artists and art styles change across exhibitions?

## 4. Datasets

### Dataset 1
- Name: Art Institute of Chicago - Artworks
- Source: Art Institute of Chicago Open Data API and GitHub
- Link: https://github.com/art-institute-of-chicago/api-data/tree/main/json/artworks
- Description: Contains information about artworks in the Art Institute of Chicago's collection, including artwork titles, artists, creation dates, departments, styles, classifications, and places of origin. Our group downloaded a sample of 200 artwork records and saved them in CSV format.
- Key variables: id, title, artist_id, artist_title, date_display, date_start, department_title, style_title, classification_title, place_of_origin
- Connection to other datasets: This dataset can be connected to the Agents dataset by matching artist_id with the Agents dataset's id. It can also be connected to the Exhibitions dataset by matching artwork IDs with the IDs listed in artwork_ids.

### Dataset 2
- Name: Art Institute of Chicago – Agents
- Source: Art Institute of Chicago Open Data API and GitHub
- Link: https://github.com/art-institute-of-chicago/api-data/tree/main/json/agents 
- Description: Contains information about people and organizations associated with the museum, including artist names, birth and death dates, and available biographical information. Our group downloaded 200 records from the API and converted the JSON responses into CSV format.
- Key variables: id, title, is_artist, agent_type_title, birth_date, death_date, description
- Connection to other datasets: This dataset can be connected to Artworks using artist IDs and to Exhibitions using the artist identifiers listed in artist_ids. These connections would allow us to examine information about artists associated with artworks and exhibitions.

### Dataset 3
- Name: Art Institute of Chicago – Exhibitions
- Source: Art Institute of Chicago Open Data API and GitHub
- Link: https://github.com/art-institute-of-chicago/api-data/tree/main/json/exhibitions
- Description: Contains information about exhibitions at the Art Institute of Chicago, including exhibition titles, dates, descriptions, and references to associated artworks and artists. Our group downloaded 200 records from the API and converted the JSON responses into CSV format.
- Key variables: id, title, short_description, aic_start_at, aic_end_at, status, artwork_ids, artist_ids
- Connection to other datasets: This dataset can be connected to Artworks using artwork_ids and to Agents using artist_ids. These relationships could help us examine which artists and artworks are associated with different exhibitions.

### Data Preparation: 
The Art Institute of Chicago provides data through its API in JSON format. We used Python to retrieve 200 records from each of the three datasets and converted them into CSV files using pandas. These files are stored in our group's GitHub repository to make the data easier to access, inspect, and analyze. In later project stages, we plan to clean the datasets and examine how they can be integrated using artwork and artist identifiers.

## 5. Timeline
Our team will complete the project in stages, focusing on data quality, integration, analysis, and reproducibility. We will track progress and individual contributions through GitHub.

| Timeline | Task | Description | Responsible |
|---|---|---|---|
| Oct. 19–25 | Data Collection | Collect and organize the three datasets. Document sources, licensing, and data acquisition methods. | Jodi, Saint |
| Oct. 26–Nov. 1 | Data Quality Assessment | Evaluate accuracy, completeness, timeliness, and consistency. Check missing values and dataset overlap. | Deeya, Rachel |
| Nov. 2–8 | Data Cleaning | Standardize formats, address missing values, and prepare artist and artwork IDs for matching. | Rachel, Saint |
| Nov. 9–15 | Data Integration | Join Artworks, Agents, and Exhibitions using shared identifiers. Validate matches and resolve inconsistencies. | Deeya, Jodi |
| Nov. 16–22 | Analysis | Reassess integrated data quality, analyze artist and art-style representation across exhibitions, and create visualizations. | Deeya, Saint |
| Nov. 23–29 | Automation & Documentation | Build a reproducible workflow, document dependencies and data provenance, and create metadata and a data dictionary. | Jodi, Rachel |
| Nov. 30–Dec. 6 | Final Review | Complete the report, test the workflow, verify GitHub contributions, and prepare the final release. | All Members |

We will review progress weekly and adjust the timeline if needed. If the initial datasets have insufficient matching records, we will expand our sample before proceeding with analysis.

## 6. Constraints
Our primary constraint is the limited sample size of 200 records per dataset, which may not fully represent the Art Institute of Chicago's collection or provide enough overlapping records for integration.

Additionally, missing artist information, inconsistent date formats, and multi-valued identifiers may complicate data cleaning and matching. Since the datasets have different structures, we will need to verify relationships between artworks, artists, and exhibitions before analysis.

Time constraints may also limit how much data we can process and validate. We will prioritize accurate integration and reproducible methods over the size of our dataset.


## 7. Gaps
One of the main gaps in our project is determining whether our three datasets can be successfully integrated. Although the Artworks, Agents, and Exhibitions datasets contain common identifiers, we have not yet verified how many records actually match across them. We initially downloaded 200 records from each dataset, but these records were selected from the first two pages of each API endpoint rather than through random sampling. As a result, our current sample may not fully represent the museum's collection or contain enough related records for meaningful analysis.

Another gap is understanding the completeness and accuracy of the information provided. Some records may have missing artist information, creation dates, or exhibition details. We will need to examine these missing values and determine how they might affect our research questions and results.

Additionally, we need to investigate how to process certain variables, such as artwork_ids and artist_ids, which contain multiple identifiers within a single field. These will require additional cleaning before we can properly join the datasets.

As we continue, our group will need to decide whether to expand our sample, refine our research questions, and identify the most appropriate methods for cleaning, integrating, and analyzing the data.
