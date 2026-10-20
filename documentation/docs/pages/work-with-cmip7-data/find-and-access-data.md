# Find and access CMIP7 data

Start with the international publication index to see what exists. If you work on NCI Gadi, check which of those datasets are held locally before downloading files from ESGF. The [overview of CMIP7 availability](data-available.md) explains the difference between the two collections.

## Discover published data worldwide

1. Open the [Climate Resource CMIP7 availability dashboard](https://www.climate-resource.com/tools/esm-model/cmip7-availability) for a quick overview by model, experiment and variable. It summarises data published on ESGF; it does **not** show which files are on Gadi.
2. Search [ESGF MetaGrid](https://metagrid-ceda.east.esgf.io/search) when you need a specific dataset, version or file. Its filters let you narrow the distributed ESGF catalogue by model, experiment, variable and other CMIP7 facets.

The [WCRP CMIP7 guidance for data users](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_users/) explains ESGF access routes and the current status of its tools.

## Find data already on Gadi

NCI stores the ACCESS Consortium's CMIP7 publications in project `im55` and selected international replicas in `ib12`. You need an [NCI account and membership of the relevant data project](https://docs.access-hive.org.au/getting_started/set_up_nci_account/) to read the files. Check [what is available on Gadi](data-available.md#available-on-nci-gadi) before assuming an ESGF search result is local.

### Use the ACCESS-NRI catalogues

NCI provides collection-level Intake-ESM datastores for some of its data holdings, including `im55` and `ib12`. The [ACCESS-NRI Intake catalogue](https://access-nri-intake-catalog.readthedocs.io/en/latest/) brings indexed Gadi data products into a Python interface for finding and loading data. Its [quickstart tutorial](https://access-nri-intake-catalog.readthedocs.io/en/latest/usage/quickstart.html) shows how to search by attributes such as model, variable and frequency, then open the matching files.

The [ACCESS-NRI Interactive Data Catalogue](https://access-nri.github.io/interactive-data-catalogue/#/) provides a browser interface to the ACCESS-NRI catalogue. You can explore its entries without logging in to Gadi. For an indexed product, the usual workflow is:

1. Filter by the model, experiment, variable and frequency you need.
2. Inspect the matching product and required NCI project memberships.
3. Narrow the selection to the files you need and copy the generated Python code.
4. Run that code in an [ARE JupyterLab session](https://docs.access-hive.org.au/getting_started/are/) with access to the data project and the [ACCESS-NRI `analysis3` environment](https://docs.access-hive.org.au/getting_started/environments/).

The [illustrated Interactive Catalogue guide](https://docs.access-hive.org.au/model_evaluation/data/finding/interactive_catalogue/) shows the interface. **As of October 2026, CMIP7 entries are not yet available in the Interactive Data Catalogue**, so its current examples use other data products. Until the CMIP7 entries are indexed, use the Gadi filesystem for local files. The Python Intake catalogue remains the preferred way to load data once the relevant entries are available.

### Use the Gadi filesystem and CMIP7 DRS

If you know the CMIP7 **Data Reference Syntax (DRS)**, you can use it to navigate directly to files. DRS is the standard directory and filename structure that identifies a dataset by facets such as activity, institution, model, experiment, ensemble member, variable, grid and version. This route is useful for scripts that already work with paths or while a dataset is not indexed in a catalogue.

The two local collection roots are:

```text
/g/data/im55/publications/MIP-DRS7/CMIP7/   # ACCESS Consortium publications
/g/data/ib12/MIP-DRS7/CMIP7/                # selected international replicas
```

For example, under either root a directory follows this pattern:

```text
<activity_id>/<institution_id>/<source_id>/<experiment_id>/<variant_label>/<region>/<frequency>/<variable_id>/<branding_suffix>/<grid_label>/<version>/
```

In a path, `mon` means monthly output, `r1i1p1f1` identifies an ensemble member and a `vYYYYMMDD` component identifies a dataset version. The [CMIP7 DRS and global attributes specification](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Global_Attributes/) defines the full structure. Check the filesystem for the current version and actual filenames before using a path in a script.

## Access data from ESGF

If the dataset is published internationally but unavailable on Gadi, use [MetaGrid](https://metagrid-ceda.east.esgf.io/search) to find its hosting node and download options. For larger scripted searches and downloads, [WCRP lists `intake-esgf` among its CMIP7 Python access tools](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_users/#1-accessing-cmip7-data). If the data are already on Gadi, use the local catalogue or filesystem to avoid a separate transfer.
