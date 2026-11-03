---
page_nav: true
---

# Explore and evaluate CMIP7 data

Browse existing plots in the hosted REF dashboard, work with data in a Jupyter notebook, or run a reusable evaluation with ESMValTool or ILAMB. The [Find and access CMIP7 data](../find-cmip7-data/find-and-access-data.md) page explains where to find the data on Gadi.

## Browse hosted REF results

??? info "Rapid Evaluation Framework (REF) — view existing CMIP7 evaluations"

    The international [CMIP REF effort](https://www.wcrp-cmip.org/cmip-phases/cmip7/rapid-evaluation-framework/) runs diagnostics through providers including ESMValTool and ILAMB. To browse precomputed results, open the [CMIP7 diagnostics catalogue](https://dashboard.climate-ref.org/diagnostics?mip_era=CMIP7&view=cards), choose a diagnostic, and select its **Figures** tab. For a first example, view the [global mean near-surface air temperature figures](https://dashboard.climate-ref.org/diagnostics/esmvaltool/global-mean-timeseries/figures).

    The hosted dashboard lets you inspect plots and other results without Gadi access. To use precomputed REF results in your own Python workflow, follow the [Jupyter notebook example for the REF API](https://climate-ref.readthedocs.io/en/latest/how-to-guides/using-pre-computed-results/).

## Explore data in a Jupyter notebook on Gadi

Join `xp65` for the software and the [NCI project holding your data](../get-set-up-nci/join-projects.md#cmip7-projects) (`im55` for the example below). When starting an [ARE JupyterLab session](../get-set-up-nci/set-up-jupyterlab.md), select the [`conda/analysis3` environment](../get-set-up-nci/set-up-jupyterlab.md#are-settings-for-cmip7) to run either notebook example.

A Jupyter notebook is where you run Python code. Xarray, ESMValCore, and Iris are tools you can use inside it. The [Interactive Data Catalogue](https://access-nri.github.io/interactive-data-catalogue/#/datastore/cmip7_australian) gives you what you need to load the data for either approach:

- **Xarray:** Load datasets by copying the Python code that the Interactive Data Catalogue generates, or by opening the file paths that the Interactive Data Catalogue lists based on your search filters. 
- **ESMValCore and Iris:** ESMValCore finds and prepares data; its `load()` method returns an Iris *cube*, another Python object for data and coordinates.

Both approaches let you explore data in Jupyter. Choose the Python tools you prefer. For a repeatable evaluation across ensembles or models, the catalogue can also generate an [ESMValTool recipe starter](#run-evaluations-in-gadi-pbs-jobs) from your filters. A recipe runs from a Gadi shell or PBS job; it does not need a notebook.

Try the [filtered catalogue example](https://access-nri.github.io/interactive-data-catalogue/#/datastore/cmip7_australian?source_id_filter=ACCESS-ESM1-6&variable_id_filter=tas&frequency_filter=mon&experiment_id_filter=historical&variant_label_filter=r1i1p1f1): `ACCESS-ESM1-6`, `historical`, monthly near-surface air temperature (`tas`), and ensemble `r1i1p1f1`. Apply the same filters for either option. Narrow the selection before loading data; this example can still match several datasets.

??? info "Xarray — explore data in a Jupyter notebook"

    There are two ways to load the data you find in the catalogue into Xarray. Both give you an Xarray Dataset to explore.

    **Option 1: copy the generated code**

    In **Quick Start**, choose **Xarray Dataset**, then select **Copy Code**. The code uses the [ACCESS-NRI Intake catalogue](../find-cmip7-data/find-and-access-data.md#access-nri-intake-catalogue) behind the scenes, but you don't need to know Intake to run it. The code generated for the example filters follows this pattern:

    ```python
    import intake
    from dask.distributed import Client

    client = Client(threads_per_worker=1)
    datastore = intake.cat.access_nri["cmip7_australian"]
    datastore = datastore.search(
        source_id="ACCESS-ESM1-6",
        experiment_id="historical",
        variable_id="tas",
        frequency="mon",
        variant_label="r1i1p1f1",
    )
    datasets = datastore.to_dataset_dict()
    print(list(datasets))
    ```

    `datasets` is a dictionary of Xarray Datasets. Inspect the printed keys, then replace `<dataset key>` below with the one you want to explore:

    ```python
    ds = datasets["<dataset key>"]
    ```

    **Option 2: copy the NCI file paths**

    Copy the file path for your dataset from the catalogue's results and open all the files in that folder with Xarray. For the example filters, the path looks like this (replace `vYYYYMMDD` with the version shown in the catalogue):

    ```python
    import xarray as xr

    path = "/g/data/im55/publications/MIP-DRS7/CMIP7/CMIP/ACCESS-Consortium/ACCESS-ESM1-6/historical/r1i1p1f1/glb/mon/tas/tavg-h2m-hxy-u/g115/vYYYYMMDD/"
    ds = xr.open_mfdataset(path + "*.nc")
    ```

    Long runs are split into several files by time period; `open_mfdataset` combines them into one Dataset. See [NCI file paths](../find-cmip7-data/find-and-access-data.md#nci-file-paths) for how the folders are organised.

    **Plot the data**

    With either option, you can now explore `ds`. For example:

    ```python
    ds["tas"].isel(time=0).plot()
    ```

    This plots one time step. The [Xarray plotting guide](https://docs.xarray.dev/en/stable/user-guide/plotting.html) shows how to make other plots.

??? info "ESMValCore and Iris — explore data in a Jupyter notebook"

    In **Quick Start**, open **Alternative quick start: ESMValCore / ESMValTool**, choose **ESMValCore (Python)**, then select **Copy ESMValCore code**. The generated code searches for the example dataset like this:

    ```python
    from itertools import islice
    from esmvalcore.dataset import Dataset

    query = Dataset(
        project="CMIP7",
        drs_specs="*",
        short_name="tas",
        branding_suffix="*",
        dataset="ACCESS-ESM1-6",
        exp="historical",
        ensemble="r1i1p1f1",
        institute="*",
        activity="*",
        grid="*",
        frequency="mon",
        realm="*",
        region="*",
    )
    matches = list(islice(query.from_files(), 5))
    for match in matches:
        print(match.facets)
    if len(matches) == 1:
        cube = matches[0].load()
        print(cube)
    ```

    This prints the matches and loads an Iris cube only if the search finds one dataset. The catalogue's full generated code gives clearer messages for zero or multiple matches. If you see several matches, add filters such as grid or branded variable and copy the updated code.

    ESMValCore uses some different names for the catalogue's search fields; the [facet mapping](https://docs.esmvaltool.org/projects/ESMValCore/en/latest/reference/facets.html) explains them. To build a recipe from notebook work, the [Composing recipes notebook](https://docs.esmvaltool.org/projects/ESMValCore/en/latest/notebooks/composing-recipes.html) shows how to turn selected ESMValCore datasets into a recipe's dataset section. Its example uses CMIP6 and ESGF; use your CMIP7 selection and Gadi environment here. You can also generate a recipe starter directly in the catalogue, as shown below.

    !!! tip

        **ESMValCore in practice: [ACCESS-ENSO recipes](https://github.com/ACCESS-NRI/ACCESS-ENSO-recipes)**

        These Jupyter notebooks explore El Niño–Southern Oscillation (ENSO) metrics with ESMValCore. Browse them for examples of loading data and developing an ENSO diagnostic. The [ACCESS-NRI recipes guide](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/recipes/) explains how to run them in ARE with `conda/analysis3`.

## Run evaluations in Gadi PBS jobs

Run ESMValTool recipes and ILAMB evaluations as PBS jobs with access to `xp65` and the relevant NCI data projects. Load `conda/analysis3` in your PBS script:

```bash
module use /g/data/xp65/public/modules
module load conda/analysis3
```

You can inspect the results in ARE afterward. See the [ACCESS-NRI Gadi guide](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/esmvaltool_workflow/) for a complete PBS job example.

??? info "ESMValTool — reusable diagnostics"

    An [ESMValTool](https://docs.esmvaltool.org/) *recipe* is a YAML file that records the input datasets, preprocessing, and any diagnostic to run. The catalogue can generate a recipe starter directly from your filters. You can then adapt it to apply the same method across many ensemble members or models in a PBS job. This supports repeatable, standardised analyses that others can inspect and reuse. ESMValTool is maintained by a broad community and is one of the [diagnostic providers used by REF](https://climate-ref.readthedocs.io/en/latest/diagnostics/esmvaltool/).

    The [recipes index](https://docs.esmvaltool.org/en/latest/recipes/index.html) describes available recipes and shows example plots. The recipe definitions are YAML files in [`esmvaltool/recipes/`](https://github.com/ESMValGroup/ESMValTool/tree/main/esmvaltool/recipes); the Python diagnostic scripts they call are in [`esmvaltool/diag_scripts/`](https://github.com/ESMValGroup/ESMValTool/tree/main/esmvaltool/diag_scripts).

    For example, open this [filtered recipe example](https://access-nri.github.io/interactive-data-catalogue/#/datastore/cmip7_australian?source_id_filter=ACCESS-ESM1-6&variable_id_filter=tas&frequency_filter=mon&experiment_id_filter=historical&variant_label_filter=r1i1p1f1&realm_filter=atmos&branded_variable_filter=tas_tavg-h2m-hxy-u&grid_label_filter=g115). It adds **Realm** `atmos`, **Branded Variable** `tas_tavg-h2m-hxy-u`, and **Grid Label** `g115` to the notebook selection above. In **Quick Start**, open **Alternative quick start: ESMValCore / ESMValTool**, choose **ESMValTool recipe (.yml)**, then select **Copy recipe (.yml)**. The generated starter for these filters is:

    ```yaml
    # Save as recipe_catalogue.yml.
    # Run: esmvaltool run --remove_preproc_dir=False recipe_catalogue.yml
    # This starter preprocesses data only; add a diagnostic script for analysis.
    # Review combinations when more than one value is selected in a filter.
    # For CMIP7, mip is the selected Realm; branding_suffix comes from Branded Variable.
    datasets:
      - project: "CMIP7"
        dataset: "ACCESS-ESM1-6"
        exp: "historical"
        ensemble: "r1i1p1f1"
        grid: "g115"
        frequency: "mon"

    diagnostics:
      catalogue_selection:
        description: Preprocess CMIP data selected in the ACCESS catalogue.
        variables:
          "tas_tavg-h2m-hxy-u":
            short_name: "tas"
            mip: "atmos"
            branding_suffix: "tavg-h2m-hxy-u"
        scripts: null
    ```

    Save this as `recipe_catalogue.yml`. With `scripts: null`, it preprocesses the selected data but does not calculate or plot a diagnostic. Run `esmvaltool run --remove_preproc_dir=False recipe_catalogue.yml` to keep the preprocessed output. Check any values the generator marks for replacement and any filters it says were not included. To create a full evaluation, add a diagnostic script and any needed preprocessing, or adapt an existing recipe.

    For a CMIP7-specific full recipe, inspect [`ref/recipe_ref_ecs.yml`](https://github.com/ESMValGroup/ESMValTool/blob/main/esmvaltool/recipes/ref/recipe_ref_ecs.yml), which calculates equilibrium climate sensitivity. Replace its `DUMMY-MODEL` dataset entries and check the required experiments and time ranges before running it. In `conda/analysis3`, use `esmvaltool recipes list` to see installed recipes, `esmvaltool recipes show ref/recipe_ref_ecs.yml` to inspect one, and `esmvaltool recipes get ref/recipe_ref_ecs.yml` to copy it for editing. Follow the [ACCESS-NRI guide for using ESMValTool on Gadi](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/esmvaltool_workflow/) to run the adapted recipe as a PBS job.

??? info "ILAMB — land-process benchmarking"

    [ILAMB](https://www.ilamb.org/) compares modelled land processes with observations and produces scores and plots, including for the carbon and water cycles. Use it for land-model benchmarking. Run it as a PBS job, following the [ACCESS-NRI ILAMB workflow](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/ilamb_workflow/) and [PBS example](https://ilamb-workflow.readthedocs.io/en/latest/source/ILAMB.html#submitting-a-pbs-job).
