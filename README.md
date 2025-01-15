# leettools.github.io
Documentation for LeetTools.

# Installation

- use conda to create a python (>= 3.8) environment
- `pip install mkdocs`
- `mkdocs new .`

# Configuration

- edit mkdocs.yml 
- add documents into docs/

# Local test

- `mkdocs serve`
- check at http://127.0.0.1:8000

# Deployment

- use `mkdocs build` to generate site/
- push all that under site/ into a publish branch (a new branch)
- deploy pages at github by using the publish branch

# Suggested Branch 

- Main
    Manual for
    - Installation
    - Configuration
    - Deployment
- leettools-doc-workshop: using MKdoc framework to build static site
- leettools-doc-publish: github page service will use this branch to deploy the document site