# Explore and evaluate CMIP7 data

Choose a workflow for what you want to do: browse existing evaluation plots in the hosted REF dashboard, explore local data in an Xarray notebook, or run a diagnostic with ESMValTool or ILAMB. The [Find and access CMIP7 data](../find-and-access-data/) page explains where to find the data on Gadi. On Gadi, the ACCESS-NRI ESMValCore and ESMValTool configuration can find CMIP7 files directly from dataset metadata; neither tool requires an Intake catalogue search first.

## Browse hosted REF results

??? info "Rapid Evaluation Framework (REF) — view existing CMIP7 evaluations"

    The international [CMIP REF effort](https://www.wcrp-cmip.org/cmip-phases/cmip7/rapid-evaluation-framework/) runs diagnostics through providers including ESMValTool and ILAMB. To browse precomputed results, open the [CMIP7 diagnostics catalogue](https://dashboard.climate-ref.org/diagnostics?mip_era=CMIP7&view=cards), choose a diagnostic, and select its **Figures** tab. For a first example, view the [global mean near-surface air temperature figures](https://dashboard.climate-ref.org/diagnostics/esmvaltool/global-mean-timeseries/figures).

    The hosted dashboard lets you inspect plots and other results without Gadi access. To use precomputed REF results in your own Python workflow, follow the [Jupyter notebook example for the REF API](https://climate-ref.readthedocs.io/en/latest/how-to-guides/using-pre-computed-results/). For local dataset exploration, use the Xarray notebook workflow below.

## Explore data in ARE JupyterLab

Join the NCI project holding your data and `xp65`, then start an [ARE JupyterLab session](https://docs.access-hive.org.au/getting_started/are/) with [`conda/analysis3`](https://docs.access-hive.org.au/getting_started/environments/). The Australian CMIP7 datastore shown below requires `im55` and `xp65` access.

??? info "Xarray — explore a dataset in a notebook"

    Open the [CMIP7 Australian datastore in the Interactive Data Catalogue](https://access-nri.github.io/interactive-data-catalogue/#/datastore/cmip7_australian). In **Quick Start**, select **Xarray Dataset**, add filters, and copy the generated Python code into your ARE notebook. Narrow the search before opening data: an unfiltered catalogue search can include thousands of datasets.

    For example, selecting `ACCESS-ESM1-6`, `historical`, monthly `tas`, and ensemble `r1i1p1f1` generates Intake search code like this:

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
    datastore.keys_info()
    ```

    The catalogue's **Xarray Dataset** code offers `to_dataset_dict()`. This example can still return several dataset keys, so inspect the table above and select the key for the dataset you want. Replace `<dataset key>` with one of the displayed keys:

    ```python
    ds = datastore["<dataset key>"].to_dask()
    ds["tas"].isel(time=0).plot()
    ```

    `ds` is an Xarray Dataset. Start with one time step before expanding the analysis. The [Intake-ESM guide to dataset keys](https://intake-esm.readthedocs.io/en/stable/how-to/understand-keys-and-how-to-change-them.html) explains `keys_info()` and `to_dask()`; the [Xarray plotting guide](https://docs.xarray.dev/en/stable/user-guide/plotting.html) shows further plots.

??? info "ESMValCore — find and preprocess data in a notebook"

    [ESMValCore](https://docs.esmvaltool.org/projects/ESMValCore/en/latest/) provides ESMValTool's file selection and preprocessing functions. In `conda/analysis3` on Gadi, search the configured CMIP7 file collections by facets without opening Intake. For example, the [ACCESS-NRI notebook guide](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/esmvaltool_workflow/) uses `Dataset.from_files()`; this CMIP7 selection uses the `tas` metadata shown in the Interactive Data Catalogue:

    ```python
    from esmvalcore.dataset import Dataset

    search = Dataset(
        project="CMIP7",
        dataset="ACCESS-ESM1-6",
        institute="ACCESS-Consortium",
        exp="historical",
        ensemble="r1i1p1f1",
        grid="g115",
        region="glb",
        frequency="mon",
        mip="atmos",
        short_name="tas",
        branding_suffix="tavg-h2m-hxy-u",
    )
    matches = list(search.from_files())
    print(matches)
    ```

    Inspect the matches and their versions before using `.load()` to obtain Iris cubes. See the [ESMValCore CMIP7 facet mapping](https://docs.esmvaltool.org/projects/ESMValCore/en/latest/reference/facets.html) for the meaning of these fields.

    If your own notebook code needs Iris cubes from an Xarray dataset already opened through Intake, ESMValCore [documents a conversion helper](https://docs.esmvaltool.org/projects/ESMValCore/en/latest/api/esmvalcore.iris_helpers.html):

    ```python
    from esmvalcore.iris_helpers import dataset_to_iris

    cubes = dataset_to_iris(ds[["tas"]])
    ```

    This optional conversion is for notebook code that already uses Xarray. It is not a prerequisite for ESMValCore file discovery or for running an ESMValTool recipe.

??? info "ACCESS-ENSO recipes — interactive ENSO diagnostics"

    The [ACCESS-ENSO recipes](https://github.com/ACCESS-NRI/ACCESS-ENSO-recipes) are notebooks for exploring El Niño–Southern Oscillation (ENSO) metrics with ESMValCore. Use them to inspect or adapt an ENSO diagnostic. The [ACCESS-NRI recipes guide](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/recipes/) explains how to run them in ARE with `conda/analysis3`.

## Run evaluations in Gadi PBS jobs

Run ESMValTool recipes and ILAMB evaluations as PBS jobs. Both use `xp65` [`conda/analysis3`](https://docs.access-hive.org.au/getting_started/environments/) and access to the relevant NCI data projects. You can inspect their results in ARE afterward.

??? info "ESMValTool — reusable diagnostics"

    [ESMValTool](https://docs.esmvaltool.org/) evaluates climate models with reusable *recipes* that select data, preprocess it, and produce diagnostics. The [recipes index](https://docs.esmvaltool.org/en/latest/recipes/index.html) describes available recipes and shows example plots. Recipe definitions are YAML files in [`esmvaltool/recipes/`](https://github.com/ESMValGroup/ESMValTool/tree/main/esmvaltool/recipes); the Python diagnostic scripts they call are in [`esmvaltool/diag_scripts/`](https://github.com/ESMValGroup/ESMValTool/tree/main/esmvaltool/diag_scripts).

    A recipe specifies datasets by facets, and ESMValTool finds the corresponding CMIP7 files through the Gadi configuration without Intake. For example, a dataset selection for monthly historical `tas` from ACCESS-ESM1.6 is:

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
