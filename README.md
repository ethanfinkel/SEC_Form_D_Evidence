# SEC_Form_D_Evidence
Open source repo from my blog post: https://www.ethanfinkel.com/posts/evidence-project. 

For a demo of this project, I have it hosted on my website at: https://data.ethanfinkel.com/.

This repo contains both the data prep and display layer for analyzing VC Form D SEC filings. 

## File Prep
To get Form D data, download TSVs from the link below and drop them in the empty Form_D_Data folder in this repo.

Link: https://www.sec.gov/data-research/sec-markets-data/form-d-data-sets. 

## Data Prep
In the Jupyter notebook and python file, there is code to combine TSV files, clean, and join the data. The end product of running all of the code is a DuckDB formatted file called vc_database.duckdb. I've already created this file and added it as a source for Evidence.dev, but you can re-create that file using the notebook or python file.

The data is prepped with DuckDB with some light datacleaning using Pandas, Numpy, and dateutil. 

## Evidence
Run the Evidence project by installing Evidence and starting your dev server. For instructions on installing Evidence and running code locally, check out their documentation here: https://docs.evidence.dev/install-evidence/. Since this project is already created and setup, you can just utalize the Start Evidence command rather than creating a new project. 

All of the code for the Evidence project is in the Evidence/pages/index.md file. Feel free to change this as you see fit and check out updates in your local npm server on localhost:3000.

## Closing
Hope people enjoy this open source example of prepping and cleaning data using DuckDB and visualizing it in Evidence.dev. Feel free to leave some comments and reach out to me on Twitter here: https://twitter.com/ethanf_17
