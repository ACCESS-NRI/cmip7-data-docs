---
page_nav: true
---

# CMIP7 experiments and data standards

This page covers two things you'll need to understand CMIP7 data: the experiments that models run, with a focus on Australia's ACCESS-ESM1.6 contribution, and the shared data standards that make output from different modelling centres consistent and comparable. To find where the files are stored on Gadi, see [Find and access CMIP7 data](../find-cmip7-data/find-and-access-data.md).

When you search for and work with CMIP7 data, you'll come across a common set of labels that describe each dataset, such as model, experiment, ensemble member, variable and frequency. Most CMIP7 search tools use these labels as filters, including the [ACCESS-NRI Interactive Data Catalogue](../find-cmip7-data/find-and-access-data.md#access-nri-interactive-data-catalogue), the [ACCESS-NRI Intake catalogue](../find-cmip7-data/find-and-access-data.md#access-nri-intake-catalogue) and [ESGF MetaGrid](../find-cmip7-data/find-and-access-data.md#esgf-metagrid). The same labels also make up every CMIP7 filename and folder path.

This page is useful when you:

- **choose which experiments to use** and want to know what each one simulates. See [Experiments](#experiments).
- **want to know what a search filter or part of a filename means**. See [Labels used to search and name CMIP7 data](#labels-used-to-search-and-name-cmip7-data).
- **combine data from several models** and need to check that units and calendars match. See [Checking units, calendars and other details](#checking-units-calendars-and-other-details).
- **can't find a variable** and want to know whether it was ever requested. See [Can't find the variable you need?](#cant-find-the-variable-you-need).
- **use ACCESS data** and want to know how a variable was calculated or checked. See [How ACCESS data was prepared](#how-access-data-was-prepared).

If you're new to CMIP, the WCRP [Guidance for data users: New to CMIP?](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_users/#6-new-to-cmip) section links to tutorials, tools and a community Q&A forum.

## Experiments

Every CMIP7 model runs experiments from the same standard set, so an experiment's name and setup are the same for every model. For example, `historical` means the same thing for ACCESS-ESM1.6 as for any other model. Each modelling centre chooses which experiments to run, and how many runs of each, so not every experiment is available for every model. To see which experiments a model has run, filter by model in the [ACCESS-NRI Interactive Data Catalogue](../find-cmip7-data/find-and-access-data.md#access-nri-interactive-data-catalogue) or [ESGF MetaGrid](../find-cmip7-data/find-and-access-data.md#esgf-metagrid).

??? info "Reading experiment names and ensembles"

    #### Reading experiment names and ensembles

    These points apply to all the experiments on this page:

    - **Experiments starting with `esm-` are driven by emissions.** In most experiments, atmospheric CO~2~ levels are *prescribed*, meaning they're set in advance. In `esm-` experiments, the model is given CO~2~ emissions and calculates the resulting CO~2~ levels using its own carbon cycle. Results from `esm-` experiments usually vary more between models, because they also include differences in how each model's carbon cycle behaves.
    - **Some experiments are run several times.** Each run starts from slightly different conditions, and together the runs form an *ensemble*. Each run is an *ensemble member*, identified by a label such as `r1i1p1f1`. Using several members helps you separate a model's response from natural year-to-year variability. See [Source and Variant in the WCRP Guidance for data users](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_users/#31-source-and-variant) for what each part of the label means.
    - **Some experiments *branch* from another**, meaning they start from a point in another experiment's run. For example, each `scen7-h` run continues from the end of one `historical` run.
    - **In search tools and filenames, ACCESS-ESM1.6 appears as `ACCESS-ESM1-6`.**

### Baseline experiments (the DECK)

The core set of CMIP baseline experiments is called the DECK: Diagnostic, Evaluation and Characterisation of Klima (Climate). These experiments *diagnose* how a model behaves, *evaluate* it against observations, and *characterise* model properties such as sensitivity to changes in atmospheric CO~2~.

Every model is encouraged to run all eight DECK experiments. Two of them can be run in either of two forms, with CO~2~ levels prescribed or calculated from emissions: `piControl` or `esm-piControl`, and `historical` or `esm-hist`.

??? info "DECK experiments"

    #### DECK experiments

    The ACCESS-ESM1.6 column shows which experiments are available or in production for ACCESS-ESM1.6, and the number of runs where there is more than one.

    | Experiment | What it does | ACCESS-ESM1.6 |
    |---|---|---|
    | [`piControl`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/picontrol/) | A long run with pre-industrial conditions that prescribe CO~2~ | Yes |
    | [`esm-piControl`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/esm-picontrol/) | Same as `piControl` except CO~2~ is calculated by the model's carbon-cycle | Yes |
    | [`abrupt-4xCO2`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/abrupt-4xco2/) | Starting from the pre-industrial climate, CO~2~ is abruptly quadrupled and held there to measure the model's response | Yes |
    | [`1pctCO2`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/1pctco2/) | Starting from the pre-industrial climate, CO~2~ is steadily increased at 1% per year | Yes |
    | [`historical`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/historical/) | The model is run with historical observations 1850-2021 of CO~2~ levels plus other drivers such as aerosols, solar radiation, and land-use | Yes (10 runs) |
    | [`esm-hist`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/esm-hist/) | Historical experiment with CO~2~ levels calculated from emissions rather than prescribed | Yes (30 runs) |
    | [`amip`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/amip/) | An atmosphere plus land model test with prescribed ocean and sea-ice, 1979-2021 | Yes |
    | [`piClim-control`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/piclim-control/) | An atmosphere plus land run with pre-industrial conditions, using ocean and sea-ice conditions from the model's own `piControl`. The reference for the other `piClim` experiments | — |
    | [`piClim-anthro`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/piclim-anthro/) | Same as `piClim-control`, but with present-day levels of human influences such as greenhouse gases and aerosols. Compared with `piClim-control` to measure how strongly these influences warm or cool the climate | — |
    | [`piClim-4xCO2`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/piclim-4xco2/) | Same as `piClim-control`, but with CO~2~ quadrupled. Compared with `piClim-control` to measure how strongly the extra CO~2~ warms the climate | — |

    — : not currently available or in production for ACCESS-ESM1.6.

### Assessment Fast Track

Beyond the DECK, modelling centres are encouraged to run the *Assessment Fast Track* (AFT): a set of priority experiments chosen to support the IPCC's Seventh Assessment Report and other climate assessments. It includes the future scenarios below, experiments that separate out individual influences on past climate (for example, `hist-aer`, `hist-GHG` and `hist-nat`, which include only aerosol, greenhouse gas or natural changes), and a range of other experiments. See the [full list of Assessment Fast Track experiments](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_modellers/#2-experiment-design) in the WCRP CMIP7 guidance.

#### Future scenarios (`ScenarioMIP`)

[Future scenario experiments (ScenarioMIP)](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/#scenariomip) project how the climate may change under different emissions pathways. 

??? tip "Details about the ScenarioMIP"
    CMIP7 has seven scenarios, named by their emissions level, from [`scen7-vl`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/scen7-vl/) (very low) through [`scen7-ln`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/scen7-ln/) (low after a temporary overshoot), [`scen7-l`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/scen7-l/) (low), [`scen7-ml`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/scen7-ml/) (medium-low), [`scen7-m`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/scen7-m/) (medium) and [`scen7-hl`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/scen7-hl/) (high, then falling) to [`scen7-h`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/scen7-h/) (high). Each scenario runs from 2022 to 2100 and has two versions: one with prescribed CO~2~ (such as `scen7-h`) and one driven by emissions (such as `esm-scen7-h`). Extension runs (such as `scen7-h-ext`) continue beyond 2100. Select a scenario name for a fuller description.

??? info "ACCESS-ESM1.6 future scenarios"

    See the [ACCESS CMIP7 Dashboard](https://access-nri.github.io/cmip7-dashboard/) for the most up-to-date information about the status of ACCESS model runs for CMIP7.

    | Experiment | What it does |
    |---|---|
    | [`scen7-h`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/scen7-h/) and [`scen7-vl`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/scen7-vl/) (ensembles of 10 runs each) | Projections 2022-2100 with prescribed CO~2~, branching from each of the 10 historical runs for high (h) and very low (vl) emissions scenarios |
    | [`esm-scen7-h`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/esm-scen7-h/) and [`esm-scen7-vl`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/esm-scen7-vl/) (ensembles of 30 runs each) | Projections 2022-2100 with CO~2~ levels calculated from emissions, branching from each of the 30 `esm-hist` runs for high (h) and very low (vl) emissions scenarios |

    Extension runs are also planned to continue projections beyond 2100.

<!-- Carbon-cycle experiments section hidden for now

#### Carbon-cycle experiments (`C4MIP`)

The [Coupled climate carbon cycle model intercomparison project (C4MIP)](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/#c4mip) explores the response of the coupled carbon-climate system. 


??? info "ACCESS-ESM1.6 carbon-cycle experiments"

    See the [ACCESS CMIP7 Dashboard](https://access-nri.github.io/cmip7-dashboard/) for the most up-to-date information about the status of ACCESS model runs for CMIP7.

    | Experiment | What it does |
    |---|---|
    | [`1pctCO2-bgc`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/1pctco2-bgc/) and [`1pctCO2-rad`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/1pctco2-rad/) | Variations on `1pctCO2` that separate out the effect of the carbon-cycle (`1pctCO2-bgc`) from the effect of warming (`1pctCO2-rad`) |
    | [`esm-flat10`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/esm-flat10/) | CO~2~ emissions are held constant at 10 billion tonnes of carbon per year. [`esm-flat10-zec`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/esm-flat10-zec/) and [`esm-flat10-cdr`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/esm-flat10-cdr/) branch from `esm-flat10` to measure the response to a zero emissions commitment, and carbon dioxide removal, respectively |

-->



For the full setup of every CMIP7 experiment and links to the scientific papers describing them, see [CMIP7 experiment setup and forcings](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/).

## Working with CMIP7 files

CMIP7 data follows shared rules so output from different modelling centres can be found and compared.

??? info "Labels used to search and name CMIP7 data"

    #### Labels used to search and name CMIP7 data

    Every CMIP7 dataset is described by the same set of labels. Most search tools, including the ACCESS-NRI catalogues and ESGF, use these labels as filters, and they also make up each file's name and folder path.

    The example column shows the labels for one ACCESS-ESM1.6 dataset: monthly near-surface air temperature from the first run of the `historical` experiment. You can [open this dataset in the Interactive Data Catalogue](https://access-nri.github.io/interactive-data-catalogue/#/datastore/cmip7_australian?source_id_filter=ACCESS-ESM1-6&variable_id_filter=tas&frequency_filter=mon&experiment_id_filter=historical&variant_label_filter=r1i1p1f1).

    | Label | What it means | ACCESS-ESM1.6 example | Where you'll see it |
    |---|---|---|---|
    | `source_id` | The model | `ACCESS-ESM1-6` | Search filter, filename, folder path |
    | `experiment_id` | The experiment. See [Experiments](#experiments) | `historical` | Search filter, filename, folder path |
    | `variant_label` | The ensemble member (one run of an experiment) | `r1i1p1f1` | Search filter, filename, folder path |
    | `variable_id` | The physical quantity, using the same short names as CMIP6 | `tas` (near-surface air temperature) | Search filter, filename, folder path |
    | `branding_suffix` | How the variable was averaged and sampled in time and space. Together with `variable_id`, it makes the *branded variable* name. See [How CMIP7 variable names work](#how-cmip7-variable-names-work) | `tavg-h2m-hxy-u` (time average, at 2 m height, on a latitude–longitude grid, over all surface types) | Search filter, filename, folder path |
    | `frequency` | How often values are reported | `mon` (monthly) | Search filter, filename, folder path |
    | `region` | The area the data covers | `glb` (global) | Search filter, filename, folder path |
    | `grid_label` | The grid the data is on | `g115` (a regular 1.875° × 1.25° latitude–longitude grid) | Search filter, filename, folder path |
    | `activity_id` | The project that designed the experiment | `CMIP` | Search filter, folder path |
    | `institution_id` | The modelling centre or group that produced the data | `ACCESS-Consortium` | Folder path |
    | Version | When the dataset was published, as a date | `v` followed by a date (`vYYYYMMDD`) | Folder path |
    | Time range | The period covered by the file | Start and end month for monthly data (`YYYYMM-YYYYMM`) | Filename |
    | `mip_era` | The CMIP phase | `CMIP7` | Folder path |
    | `drs_specs` | The version of the naming rules | `MIP-DRS7` | Folder path |

    For a more complete version of this table, including a column showing what has chenged since CMIP6, see [this documentation on the Data Reference Syntax](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Global_Attributes/#table-1-list-of-cmip7-drs-elements).
    
    Search tools sometimes show these labels with more readable names. For example, the Interactive Data Catalogue shows **Grid Label** for `grid_label`, while the Python code it generates uses the label names directly (such as `source_id="ACCESS-ESM1-6"`). The catalogue also has a **Realm** filter (such as `atmos` or `ocean`), which groups variables by part of the climate system but isn't part of filenames or folder paths.

    Put together, files for this example dataset are named like this:

    `tas_tavg-h2m-hxy-u_mon_glb_g115_ACCESS-ESM1-6_historical_r1i1p1f1_YYYYMM-YYYYMM.nc`

    and stored in a folder like this:

    `MIP-DRS7/CMIP7/CMIP/ACCESS-Consortium/ACCESS-ESM1-6/historical/r1i1p1f1/glb/mon/tas/tavg-h2m-hxy-u/g115/vYYYYMMDD/`

    For more detail, see:

    - [CMIP7 list of labels](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Global_Attributes/#table-1-list-of-cmip7-drs-elements), including sample values from other models and changes since CMIP6 (WCRP CMIP7 guidance)
    - [CMIP7 facets in the WCRP Guidance for data users](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_users/#3-cmip7-facets-and-their-documentation), with links to the full lists of allowed models, experiments, variables, frequencies and grids
    - [The filename pattern](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Global_Attributes/#2-filenames) and [folder path pattern](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Global_Attributes/#3-directory-structure-template) (WCRP CMIP7 guidance)
    - [Where these folders are on Gadi](../find-cmip7-data/find-and-access-data.md#advanced-fallback-nci-file-system)

    Some practical points when working with CMIP7 files:

    - **Published CMIP7 output is written as NetCDF (`.nc`), generally with one variable per file.** Long runs are also split into several files by time period, so you'll usually need to open several files together, for example with Xarray's `open_mfdataset`. The catalogues do this for you.
    - **If a dataset has more than one version**, use the one with the most recent date unless you need to match an earlier analysis.
    - **CMIP6 scripts won't work as-is.** If your code reads information from CMIP6 filenames or paths, you'll need to update it, because the labels and their order have changed in CMIP7.

    You may see these labels called *facets*, and the naming system called the *Data Reference Syntax*.

??? info "Checking units, calendars and other details"

    #### Checking units, calendars and other details

    Each file also stores information about its data, such as units, coordinates, calendar, model and experiment. Tools like Xarray read this automatically, and you can see it by opening a file and printing the dataset.

    Before you combine data from different models, check:

    - **Calendar.** Models use different calendars, for example with or without leap years (`noleap`) or with 30-day months (`360_day`). This affects time averages and date matching. The [Frequency section of the WCRP Guidance for data users](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_users/#34-frequency) lists the common calendars and how to check which one a file uses. The [cftime](https://unidata.github.io/cftime/) library, which Xarray uses, handles these calendars.
    - **Units.** Variables follow standard units, but confirm them before comparing or converting. The [CF standard name table](https://cfconventions.org/Data/cf-standard-names/current/build/cf-standard-name-table.html) defines each quantity and its standard units.
    - **Grid.** Models use different grids, so you'll usually need to regrid before comparing them point by point. The [Grids section of the WCRP Guidance for data users](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_users/#35-grids) links to viewers showing each grid's resolution, and to the model documentation that lists which grids each model uses.

    The [CF conventions](https://cfconventions.org/Data/cf-conventions/cf-conventions-1.13/cf-conventions.html) define how NetCDF data describes coordinates, standard names, units and related information.

    You may see CMIP7 data described as *CMORised*. This means it follows the CMIP output conventions; the files need not have been produced by the CMOR software itself. See [CMIP7 data format in the WCRP Guidance for data users](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_users/#4-cmip7-data-format).

## Finding the right variable

??? info "Which variables exist in CMIP7?"

    #### Which variables exist in CMIP7?

    Before CMIP7 models were run, the CMIP community agreed on a list of variables that modelling centres were requested to produce for each experiment, including how often each variable should be reported (for example, monthly or daily) and for which region. This list is called the [CMIP7 Data Request](https://www.wcrp-cmip.org/cmip-phases/cmip7/cmip7-data-request/).

    To find which CMIP7 variables exist, you can search the [CMIP7 variables table](https://cmip-data-request.github.io/cmip7-dreq-webview/latest/variables.html), using either a CMIP7 or CMIP6 variable name.

??? info "How CMIP7 variable names work"

    #### How CMIP7 variable names work

    CMIP7 variable names are longer than in CMIP6, so you may need to look up a variable's new name in the [CMIP7 variables table](https://cmip-data-request.github.io/cmip7-dreq-webview/latest/variables.html) before you search for data.

    CMIP7 variable names have two parts. For example, in `tas_tavg-h2m-hxy-u`, the first part (`tas`, near-surface air temperature) is the familiar CMIP6 name. The second part describes how the variable was sampled: a time average (`tavg`), at 2 m above the ground (`h2m`), as a latitude–longitude field (`hxy`), over all surface types (`u`). These full names are called *branded variables*, and you can filter by them in the Interactive Data Catalogue using **Branded Variable**.

    - [Variable section of the WCRP Guidance for data users](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_users/#33-variable): how CMIP6 names such as `Amon.tas` map to CMIP7 names
    - [CMIP7 branding suffix reference](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Branded_Variables/#branding-suffixes): what each part of a branded variable name means

??? info "Can't find the variable you need?"

    #### Can't find the variable you need?

    Check the [CMIP7 variables table](https://cmip-data-request.github.io/cmip7-dreq-webview/latest/variables.html) first. If a variable isn't in the table, it wasn't requested, so it's unlikely that any model produced it for CMIP7.

    If it is in the table but you still can't find it, the model you want may not have produced it: modelling centres don't produce every requested variable for every experiment. To see what's actually available, search the [ACCESS-NRI Interactive Data Catalogue](../find-cmip7-data/find-and-access-data.md#access-nri-interactive-data-catalogue) or [ESGF MetaGrid](../find-cmip7-data/find-and-access-data.md#esgf-metagrid).


## ACCESS Consortium processing

??? info "How ACCESS data was prepared"

    #### How ACCESS data was prepared

    The ACCESS Consortium uses [ACCESS-MOPPy](https://access-moppy.readthedocs.io/en/latest/) to turn native ACCESS atmosphere, land, ocean and sea-ice output into CMIP7 NetCDF files, mapping model variables to requested variables and writing the required metadata, filenames and folder structure. Some requested variables aren't output directly by the model, so MOPPy calculates them from one or more model fields. See [how MOPPy calculates derived variables](https://access-moppy.readthedocs.io/en/latest/explanation/derived_variables.html).

    It checks units, missing or non-finite values, and broad physical ranges; range excursions prompt review rather than automatically rejecting a file. The [MOPPy physical range rules](https://access-moppy.readthedocs.io/en/latest/reference/qc_ranges.html) list the expected range for each variable. Publication workflows can also run [CF and CMIP compliance checks and diagnostic plots](https://access-moppy.readthedocs.io/en/latest/howto/qc_validation.html).

    You'll mostly need this if a variable looks unexpected or you need to describe how it was produced. If you think you've found an error, see [Find and report CMIP7 errata](../work-with-cmip7-data/citing-and-errata.md#errata).
