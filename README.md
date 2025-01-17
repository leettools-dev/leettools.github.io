# leettools.github.io

Documentation for LeetTools. See at [https://leettools-dev.github.io/](https://leettools-dev.github.io/)


# Quick Start 

- Switch to the branch `leettools-doc-workshop`.
- Edit documents under `docs/`. You can modify configurations in `mkdocs.yml`. Use `mkdocs serve` to preview changes.
- Run `mkdocs build` to generate the site (this will create all the static HTML files in the `site/` directory).
- Commit and push changes to the `leettools-doc-workshop` branch.
- Run `python tool-copy_to_publish.py`. This script will switch to the `leettools-doc-publish` branch and copy all contents from `/site` to the root directory of `leettools-doc-publish`.
- Commit and push changes to the `leettools-doc-publish` branch. The website at [https://leettools-dev.github.io/](https://leettools-dev.github.io/) will be automatically updated.

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