# Explore and evaluate CMIP7 data

Browse existing plots in the hosted REF dashboard, work with data in a Jupyter notebook, or run a reusable evaluation with ESMValTool or ILAMB. The [Find and access CMIP7 data](../find-and-access-data/) page explains where to find the data on Gadi.

## Browse hosted REF results

??? info "Rapid Evaluation Framework (REF) — view existing CMIP7 evaluations"

    The international [CMIP REF effort](https://www.wcrp-cmip.org/cmip-phases/cmip7/rapid-evaluation-framework/) runs diagnostics through providers including ESMValTool and ILAMB. To browse precomputed results, open the [CMIP7 diagnostics catalogue](https://dashboard.climate-ref.org/diagnostics?mip_era=CMIP7&view=cards), choose a diagnostic, and select its **Figures** tab. For a first example, view the [global mean near-surface air temperature figures](https://dashboard.climate-ref.org/diagnostics/esmvaltool/global-mean-timeseries/figures).

    The hosted dashboard lets you inspect plots and other results without Gadi access. To use precomputed REF results in your own Python workflow, follow the [Jupyter notebook example for the REF API](https://climate-ref.readthedocs.io/en/latest/how-to-guides/using-pre-computed-results/).

## Explore data in a Jupyter notebook on Gadi

Join `xp65` for the software and the NCI project holding your data (`im55` for the example below). When starting an [ARE JupyterLab session](https://docs.access-hive.org.au/getting_started/are/), select the [`conda/analysis3` environment](https://docs.access-hive.org.au/getting_started/environments/) to run either notebook example.

A Jupyter notebook is where you run Python code. Intake, Xarray, ESMValCore, and Iris are tools you can use inside it. The [Interactive Data Catalogue](https://access-nri.github.io/interactive-data-catalogue/#/datastore/cmip7_australian) can generate code for either approach:

- **Intake and Xarray:** Intake finds the catalogue entries; Xarray opens the data as a *Dataset* with variables and coordinates.
- **ESMValCore and Iris:** ESMValCore finds and prepares data; its `load()` method returns an Iris *cube*, another Python object for data and coordinates.

Both approaches let you explore data in Jupyter. Choose the Python tools you prefer. If you plan to turn the work into a repeatable [ESMValTool recipe](#run-evaluations-in-gadi-pbs-jobs) for ensembles or multiple models, ESMValCore offers a direct path from selected datasets into a recipe.

Try the [filtered catalogue example](https://access-nri.github.io/interactive-data-catalogue/#/datastore/cmip7_australian?source_id_filter=ACCESS-ESM1-6&variable_id_filter=tas&frequency_filter=mon&experiment_id_filter=historical&variant_label_filter=r1i1p1f1): `ACCESS-ESM1-6`, `historical`, monthly near-surface air temperature (`tas`), and ensemble `r1i1p1f1`. Apply the same filters for either option. Narrow the selection before loading data; this example can still match several datasets.

??? info "Intake and Xarray — explore data in a Jupyter notebook"

    In **Quick Start**, choose **Xarray Dataset**, then select **Copy Code**. The code generated for the example filters follows this pattern:

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
    ds["tas"].isel(time=0).plot()
    ```

    This plots one time step. The [Xarray plotting guide](https://docs.xarray.dev/en/stable/user-guide/plotting.html) shows how to make other plots.

??? info "ESMValCore and Iris — explore data in a Jupyter notebook"

    In **Quick Start**, open **Alternative quick start: ESMValCore**, then select **Copy ESMValCore code**. The generated code searches for the example dataset like this:

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

    ESMValCore uses some different names for the catalogue's search fields; the [facet mapping](https://docs.esmvaltool.org/projects/ESMValCore/en/latest/reference/facets.html) explains them. When you are ready to build a recipe, the [Composing recipes notebook](https://docs.esmvaltool.org/projects/ESMValCore/en/latest/notebooks/composing-recipes.html) shows how to turn selected ESMValCore datasets into a recipe's dataset section. Its example uses CMIP6 and ESGF; use your CMIP7 selection and Gadi environment here.

??? info "ACCESS-ENSO recipes — interactive ENSO diagnostics"

    The [ACCESS-ENSO recipes](https://github.com/ACCESS-NRI/ACCESS-ENSO-recipes) are notebooks for exploring El Niño–Southern Oscillation (ENSO) metrics with ESMValCore. Use them to inspect or adapt an ENSO diagnostic. The [ACCESS-NRI recipes guide](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/recipes/) explains how to run them in ARE with `conda/analysis3`.

## Run evaluations in Gadi PBS jobs

Run ESMValTool recipes and ILAMB evaluations as PBS jobs with access to `xp65` and the relevant NCI data projects. Load `conda/analysis3` in your PBS script:

```bash
module use /g/data/xp65/public/modules
module load conda/analysis3
```

You can inspect the results in ARE afterward. See the [ACCESS-NRI Gadi guide](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/esmvaltool_workflow/) for a complete PBS job example.

??? info "ESMValTool — reusable diagnostics"

    An [ESMValTool](https://docs.esmvaltool.org/) *recipe* records the input datasets, preprocessing, and diagnostic to run. Starting with ESMValCore in a notebook makes it easier to carry your dataset selection into a recipe. The recipe can then apply the same method across many ensemble members or models in a PBS job. This supports repeatable, standardised analyses that others can inspect and reuse. ESMValTool is maintained by a broad community and is one of the [diagnostic providers used by REF](https://climate-ref.readthedocs.io/en/latest/diagnostics/esmvaltool/).

    The [recipes index](https://docs.esmvaltool.org/en/latest/recipes/index.html) describes available recipes and shows example plots. The recipe definitions are YAML files in [`esmvaltool/recipes/`](https://github.com/ESMValGroup/ESMValTool/tree/main/esmvaltool/recipes); the Python diagnostic scripts they call are in [`esmvaltool/diag_scripts/`](https://github.com/ESMValGroup/ESMValTool/tree/main/esmvaltool/diag_scripts).

    For example, the notebook's monthly historical `tas` selection for ACCESS-ESM1.6 would appear in a recipe like this:

    ```yaml
    datasets:
      - project: CMIP7
        dataset: ACCESS-ESM1-6
        institute: ACCESS-Consortium
        exp: historical
        ensemble: r1i1p1f1
        grid: g115
        region: glb

    diagnostics:
      example:
        variables:
          tas:
            mip: atmos
            frequency: mon
            branding_suffix: tavg-h2m-hxy-u
        # Add the recipe's preprocessor and diagnostic script here.
    ```

    This is a selection fragment, not a complete recipe. For a CMIP7-specific full recipe, inspect [`ref/recipe_ref_ecs.yml`](https://github.com/ESMValGroup/ESMValTool/blob/main/esmvaltool/recipes/ref/recipe_ref_ecs.yml), which calculates equilibrium climate sensitivity. Replace its `DUMMY-MODEL` dataset entries and check the required experiments and time ranges before running it. In `conda/analysis3`, use `esmvaltool recipes list` to see installed recipes, `esmvaltool recipes show ref/recipe_ref_ecs.yml` to inspect one, and `esmvaltool recipes get ref/recipe_ref_ecs.yml` to copy it for editing. Follow the [ACCESS-NRI guide for using ESMValTool on Gadi](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/esmvaltool_workflow/) to run the adapted recipe as a PBS job.

??? info "ILAMB — land-process benchmarking"

    [ILAMB](https://www.ilamb.org/) compares modelled land processes with observations and produces scores and plots, including for the carbon and water cycles. Use it for land-model benchmarking. Run it as a PBS job, following the [ACCESS-NRI ILAMB workflow](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/ilamb_workflow/) and [PBS example](https://ilamb-workflow.readthedocs.io/en/latest/source/ILAMB.html#submitting-a-pbs-job).
