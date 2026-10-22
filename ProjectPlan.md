
# IS 477 Course Project Plan

## 1. Overview


## 2. Team
- Member 1: Jodi Domingo — [Responsibilities]
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

## 5. Timeline


## 6. Constraints



## 7. Gaps

