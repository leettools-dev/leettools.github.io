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

- Use conda to create a Python (>= 3.8) environment.
- Run `pip install mkdocs`.
- Run `mkdocs new .` to initialize a new MkDocs project.

# Configuration

- Edit `mkdocs.yml` to configure your project.
- Add documents into the `docs/` directory.

# Local Test

- Run `mkdocs serve` to start a local server.
- Check the site at http://127.0.0.1:8000. 

# Deployment

- Use `mkdocs build` to generate the site in the `site/` directory.
- Push all files under `site/` into a new branch dedicated to publishing.
- Deploy the pages on GitHub using this publish branch.

# Suggested Branches

- Main: Contains the main README and other essential project files.
- leettools-doc-workshop: Utilizes the MkDocs framework to build the static site.
- leettools-doc-publish: This branch is used by GitHub Pages to deploy the documentation site.
