# CMIP7 experiments and data standards

This page covers two things you'll need to understand CMIP7 data: the experiments that models run, with a focus on Australia's ACCESS-ESM1.6 contribution, and the shared data standards that make output from different modelling centres consistent and comparable. To find where the files are stored on Gadi, see [Find and access CMIP7 data](../../work-with-cmip7-data/find-and-access-data/).

## Baseline experiments

The core set of CMIP baseline experiments is called the DECK: Diagnostic, Evaluation and Characterisation of Klima (Climate). These experiments *diagnose* how a model behaves, *evaluate* it against observations, and *characterise* model properties such as sensitivity to changes in atmospheric CO~2~.

??? info "ACCESS-ESM1.6 baseline experiments"
    The following ACCESS-ESM1.6 experiments are available or in production:

    | Experiment | What it does |
    |---|---|
    | `piControl` | A long run with pre-industrial conditions that prescribe CO~2~ |
    | `esm-piControl` | Same as `piControl` except CO~2~ is calculated by the model's carbon-cycle |
    | `abrupt-4xCO2` | Starting from the pre-industrial climate, CO~2~ is abruptly quadrupled and held there to measure the model's response |
    | `1pctCO2` | Starting from the pre-industrial climate, CO~2~ is steadily increased at 1% per year. Two additional experiments separate out the effect of the carbon-cycle (`1pctCO2-bgc`) from the effect of warming (`1pctCO2-rad`) |
    | `esm-flat10` | CO~2~ emissions are held constant at 10 billion tonnes of carbon per year. `esm-flat10-zec` and `esm-flat10-cdr` branch from `esm-flat10` to measure the response to a zero emissions commitment, and carbon dioxide removal, respectively |
    | `historical` (ensemble of 10 runs) | The model is run with historical observations 1850-2021 of CO~2~ levels plus other drivers such as aerosols, solar radiation, and land-use |
    | `esm-historical` (ensemble of 30 runs) | Historical experiment with CO~2~ levels calculated from emissions rather than prescribed |
    | `amip` | An atmosphere plus land model test with prescribed ocean and sea-ice |

## Future scenarios

Future scenario experiments project how the climate may change under different emissions pathways.

??? info "ACCESS-ESM1.6 future scenarios"
    | Experiment | What it does |
    |---|---|
    | `scen7-h` and `scen7-vl` (ensembles of 10 runs each) | Projections 2022-2100 with prescribed CO~2~, branching from each of the 10 historical runs for high (h) and very low (vl) emissions scenarios |
    | `esm-scen7-h` and `esm-scen7-vl` (ensembles of 30 runs each) | Projections 2022-2100 with CO~2~ levels calculated from emissions, branching from each of the 30 `esm-historical` runs for high (h) and very low (vl) emissions scenarios |

    Extension runs are also planned to continue projections beyond 2100.

For the full setup of every CMIP7 experiment, see [CMIP7 experiment setup and forcings](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/).

## Requirements

CMIP7 data follows shared rules so output from different modelling centres can be found and compared.

??? info "CMIP7 and CF conventions"

    #### CMIP7 and CF conventions

    The [CMIP7 global-attribute rules](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Global_Attributes/) require consistent metadata for the model, experiment, ensemble member and other dataset properties, using controlled vocabularies. The [CF conventions](https://cfconventions.org/Data/cf-conventions/cf-conventions-1.13/cf-conventions.html) define how NetCDF data describes coordinates, standard names, units and related information.

??? info "CMIP7 Data Request"

    #### CMIP7 Data Request

    The [Data Request](https://www.wcrp-cmip.org/cmip-phases/cmip7/cmip7-data-request/) specifies which variables are requested for CMIP7 experiments and how they should be reported, including frequency and region. Browse the [requested variables](https://cmip-data-request.github.io/cmip7-dreq-webview/latest/variables.html) or see the [CMIP7 branded-variable guide](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Branded_Variables/) for the new variable names.

## Output files

??? info "CMORised NetCDF and file structure"

    #### CMORised NetCDF and file structure

    Published CMIP7 output is written as NetCDF (`.nc`), generally with one variable per file. *CMORised* means it follows the CMIP output conventions; the files need not have been produced by the CMOR software itself. The [Data Reference Syntax (DRS)](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Global_Attributes/) builds filenames and directory paths from metadata such as model, experiment, ensemble member, variable, grid and version.

## ACCESS Consortium processing

??? info "ACCESS-MOPPy"

    #### ACCESS-MOPPy

    The ACCESS Consortium uses [ACCESS-MOPPy](https://access-moppy.readthedocs.io/en/latest/) to turn native ACCESS atmosphere, land, ocean and sea-ice output into CMIP7 NetCDF files, mapping model variables to requested variables and writing the required metadata and DRS layout. MOPPy uses Xarray and Dask rather than the CMOR library.

    It checks units, missing or non-finite values, and broad physical ranges; range excursions prompt review rather than automatically rejecting a file. Publication workflows can also run [CF and CMIP compliance checks and diagnostic plots](https://access-moppy.readthedocs.io/en/latest/howto/qc_validation.html).
