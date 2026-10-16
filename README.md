# CMIP7 Data Docs

Source for the [CMIP7 Data Documentation website](https://cmip7-data-docs.readthedocs.io): a guide to finding, accessing, understanding, and using CMIP7 climate model data on NCI in Australia.

Jointly created and maintained by [NCI](https://nci.org.au) and [ACCESS-NRI](https://access-nri.org.au).

## Contributing

Contributions are welcome! You can:

- use the **Edit this page** button (pencil icon) on any page of the site to propose a change
- [open an issue](https://github.com/ACCESS-NRI/cmip7-data-docs/issues) to report a problem or suggest new content
- open a pull request

Each pull request gets a website preview from Read the Docs, and a link to the preview is added to the pull request automatically. Links are checked on every pull request. When a pull request is merged into `main`, the live site updates automatically.

## Repository layout

```
documentation/
├── docs/              # Website pages (Markdown), images, CSS and JavaScript
│   └── pages/         # Content pages, one folder per site section
├── mkdocs.yml         # Site configuration and navigation menu
├── requirements.txt   # Python packages needed to build the site
├── hooks/             # Custom MkDocs build hooks
├── overrides/         # Theme template overrides (header, footer, etc.)
├── abbreviations.md   # Abbreviations shown as tooltips across the site
└── references.bib     # Bibliography for citations
.readthedocs.yaml      # Read the Docs build configuration
.github/workflows/     # Link checking and PR preview automation
```

To add a new page, create a Markdown file under `documentation/docs/pages/` and add it to the `nav` section of `documentation/mkdocs.yml`.

## Build locally

The site is built with [MkDocs](https://www.mkdocs.org) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme. To preview it on your own machine, run these commands from the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r documentation/requirements.txt
mkdocs serve -f documentation/mkdocs.yml
```

Then open <http://127.0.0.1:8000>. The preview reloads automatically when you save changes.

## Maintainers

**NCI:** Jo Croucher, Heather Leasor, ...

**ACCESS-NRI:** Paige Martin ([@paigem](https://github.com/paigem)), Kesley Druken ([@kdruken](https://github.com/kdruken)), Romain Beucher ([@rbeucher](https://github.com/rbeucher)), Peter Dobrofotoff ([@peterdobro](https://github.com/peterdobro))
