# Interaktive Visualisierung von Medikamentenwirkung auf Proteine/Interactive visualization of drug effects on proteins
Our platform provides an immersive experience for exploring and analyzing a segment of the dataset from [Gonçalves et al.](https://pubmed.ncbi.nlm.nih.gov/35839778/). 
With a primary focus on identifying associated proteins and drugs for individual or groups of proteins, SPIDER offers comprehensive tools for in-depth research.

This repository contains the code for the **S**ystem for **P**rotein, **I**nteractions, **D**rugs, and **E**xploratory **R**esearch (**SPIDER**).
To use SPIDER locally on your PC, we recommend using the Docker version of SPIDER. For detailed instructions, see the [Docker installation instructions](#docker).



## Structure

The code is divided into three main categories:

1. **Frontend** - Code for the SPIDER frontend
2. **Backend** - FastAPI server, Neo4j dump, and other utilities
3. **Docker** - docker-compose.yml to install and run SPIDER in a Docker container

These categories are further divided into subcategories.

## Frontend

The frontend is divided into several components:

1. **build**: Output file for deployment and other assets.
2. **node_modules**: Used node modules for SPIDER.
3. **public**: Used images.
4. **src/components**: Includes all the components of the web application.
    1. **Database**: List and information for used datasets.
    2. **FAQ**: General information, used licenses, and answers to common questions.
    3. **Graph**: Network graph and tools for the graph (e.g., filters).
    4. **ListSearch**: Search for a group of entities.
    5. **NavigationBar**: Allows access to all sub-websites.
    6. **Overview**: Show ProCan Plots.
    7. **SearchBar**: Search for one entity.
    8. **Upload**: Upload new data to the database.
5. **App**: Main component of the React application.
6. **index**: Entry point of the React application.

## Backend

The backend is divided into several subcategories:

1. **challenge_data**: Data from the ProCan study/challenge.
2. **data**: Stores the uploaded files.
3. **data_info**: Stores the uploaded md files.
4. **example**: Contains example files that can be used for uploading data.
5. **help_data**: Files created during data processing.
6. **help_tools**: Programs that help with adding data to the database, performing investigations, and creating diagrams.
7. **neo4j_database_dump**: Backup of the Neo4j database.
8. **settings**: Contains files that specify how an uploaded file should be integrated into the database.
9. **similarity_data**: Calcukated similarity values.
10. **allgemeine_info**: Contains all data for filter options.
11. **database**: Contains all information about the used datasets.
12. **datasets**: List of used datasets.
13. **file_converter**: Integrates the uploaded file into the Neo4j database.
14. **main**: FastAPI Server.
15. **updateDBInfo**: Updates the allgemeine_info file after new data has been integrated into the database.


## Development Setup

- Install all necessary Python and JS libraries.
- Setup a local Neo4j database (Version: 5.12.0 Community Edition) with the APOC and  Graph Data Science Library.
&rarr; Load backup into the new Neo4j database.

```
neo4j stop
neo4j-admin database load --from-path=C:\backup\backup neo4j --overwrite-destination=true
neo4j start
```
Note: change the file paths according to your configuration
- Call http://localhost:7474/browser/ and execute the following Neo4j cipher
```
CREATE INDEX IF NOT EXISTS FOR (d:Drug) ON (d.name);
CREATE INDEX IF NOT EXISTS FOR (p:Protein) ON (p.name);
CREATE INDEX IF NOT EXISTS FOR (c:Cell_Line) ON (c.name);
CREATE INDEX IF NOT EXISTS FOR (d:Drug) ON (d.uid);
CREATE INDEX IF NOT EXISTS FOR (p:Protein) ON (p.uid);
CREATE INDEX IF NOT EXISTS FOR (c:Cell_Line) ON (c.uid);
CREATE INDEX IF NOT EXISTS FOR (d:Drug) ON (d.drug_id);
CREATE INDEX IF NOT EXISTS FOR (d:Drug) ON (d.CHEMBL);
CREATE INDEX IF NOT EXISTS FOR (c:Cell_Line) ON (c.COSMIC_ID);
CREATE INDEX IF NOT EXISTS FOR (p:Protein) ON (p.swiss);
CALL gds.graph.project("graph", "Protein", {PPI: {orientation: "UNDIRECTED"}});
```
- Start the fastapi server
```
cd backend
python  -m uvicorn main:app 
```
- Start the development server
```
cd frontend
npm start
```

## Production-Setup
To use SPIDER, you have two options: either utilize Docker or set up your own server.

***
### Docker
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Optional: Restart your pc after the installation
3. Download the [docker-compose.yml from the docker folder](./docker/docker-compose.yml) of this repository. Important: Do not use the wrong docker-compose file!
4. Open the Terminal in the folder where you placed the docker-compose.yml and run the following command:
```
docker-compose up
```
(Optional: First run docker-compose pull)
This process can take some time (approximately 40 minutes).
5. Call http://localhost:7474/browser/ and execute the following Neo4j cipher (user: neo4j, password: workwork).
```
CREATE INDEX IF NOT EXISTS FOR (d:Drug) ON (d.name);
CREATE INDEX IF NOT EXISTS FOR (p:Protein) ON (p.name);
CREATE INDEX IF NOT EXISTS FOR (c:Cell_Line) ON (c.name);
CREATE INDEX IF NOT EXISTS FOR (d:Drug) ON (d.uid);
CREATE INDEX IF NOT EXISTS FOR (p:Protein) ON (p.uid);
CREATE INDEX IF NOT EXISTS FOR (c:Cell_Line) ON (c.uid);
CREATE INDEX IF NOT EXISTS FOR (d:Drug) ON (d.drug_id);
CREATE INDEX IF NOT EXISTS FOR (d:Drug) ON (d.CHEMBL);
CREATE INDEX IF NOT EXISTS FOR (c:Cell_Line) ON (c.COSMIC_ID);
CREATE INDEX IF NOT EXISTS FOR (p:Protein) ON (p.swiss);
CALL gds.graph.project("graph", "Protein", {PPI: {orientation: "UNDIRECTED"}});
```
6. The website should be running on http://localhost:3000/
***

### Server
- Install all necessary python and js libraries
- Setup a local Neo4j database (Version: 5.12.0 Community Edition) with the APOC and  Graph Data Science Library.
&rarr; load backup in to the new neo4j database
```
neo4j stop
neo4j-admin database load --from-path=C:\backup\backup neo4j --overwrite-destination=true
neo4j start
```
Note: change the file paths according to your configuration
- Call http://localhost:7474/browser/ and execute the following Neo4j cipher
```
CREATE INDEX IF NOT EXISTS FOR (d:Drug) ON (d.name);
CREATE INDEX IF NOT EXISTS FOR (p:Protein) ON (p.name);
CREATE INDEX IF NOT EXISTS FOR (c:Cell_Line) ON (c.name);
CREATE INDEX IF NOT EXISTS FOR (d:Drug) ON (d.uid);
CREATE INDEX IF NOT EXISTS FOR (p:Protein) ON (p.uid);
CREATE INDEX IF NOT EXISTS FOR (c:Cell_Line) ON (c.uid);
CREATE INDEX IF NOT EXISTS FOR (d:Drug) ON (d.drug_id);
CREATE INDEX IF NOT EXISTS FOR (d:Drug) ON (d.CHEMBL);
CREATE INDEX IF NOT EXISTS FOR (c:Cell_Line) ON (c.COSMIC_ID);
CREATE INDEX IF NOT EXISTS FOR (p:Protein) ON (p.swiss);
CALL gds.graph.project("graph", "Protein", {PPI: {orientation: "UNDIRECTED"}});
```
- Start the fastapi server
```
cd backend
python  -m uvicorn main:app 
```
- Start the development server
```
cd frontend
npm run build
cd build
python -m SimpleHTTPServer 7000
```

## Licensed content
- DrugBank under Creative Common's Attribution-NonCommercial 4.0 International License. [Link to download](https://go.drugbank.com/releases/latest)
- BioGRID under MIT License. [Link to download](https://downloads.thebiogrid.org/File/BioGRID/Release-Archive/BIOGRID-4.4.227/BIOGRID-ALL-4.4.227.tab3.zip)
- Cell Line node picture: Image of a biology cancer cell, obtained from Iconduck and licensed under CC BY 3.0. [Link to image](https://iconduck.com/illustrations/122610/biology-cancer-cell-disease-health-human-tumor)
- Spider picture: Modified image of bug spider 2, sourced from Iconduck and licensed under CC0. [Link to image](https://iconduck.com/icons/250210/bug-spider-2)