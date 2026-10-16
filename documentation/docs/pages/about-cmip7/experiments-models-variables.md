# Experiments, models and variables

Every CMIP7 dataset is identified by a set of standard labels called **facets**: activity, institution, source (model), experiment, variant, realm, frequency, variable, grid and version. You'll use them to search for data, and you'll find them in each file's name and metadata.

This page explains the facets you'll use most. For the full reference, see [CMIP7 facets and their documentation](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_users/#3-cmip7-facets-and-their-documentation) in the WCRP CMIP7 Guidance for Data Users.

## Experiments

??? info "The DECK"

    #### The DECK

    Every model participating in CMIP7 runs the eight DECK experiments. Earth system models also run emissions-driven versions of two of them. Click an experiment name for its full setup.

    | Experiment | What it does |
    |---|---|
    | [`piControl`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/picontrol/) | Long control run under pre-industrial conditions |
    | [`historical`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/historical/) | Simulates 1850 to the recent past with observed forcings |
    | [`amip`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/amip/) | Atmosphere and land only, using observed sea surface temperatures and sea ice |
    | [`abrupt-4xCO2`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/abrupt-4xco2/) | CO2 instantly quadrupled from pre-industrial levels |
    | [`1pctCO2`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/1pctco2/) | CO2 increased by 1% per year |
    | [`piClim-control`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/piclim-control/), [`piClim-anthro`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/piclim-anthro/), [`piClim-4xCO2`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/piclim-4xco2/) | Fixed sea surface temperature runs used to measure radiative forcing |
    | [`esm-piControl`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/esm-picontrol/), [`esm-hist`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/esm-hist/) | Emissions-driven versions of `piControl` and `historical` (Earth system models only) |

??? info "The Assessment Fast Track and Community MIPs"

    #### The Assessment Fast Track and Community MIPs

    Beyond the DECK, modelling groups choose which [Community MIPs](https://wcrp-cmip.org/mips/) to contribute to. The **activity** facet tells you which MIP an experiment belongs to.

    The [Assessment Fast Track](https://wcrp-cmip.org/cmip-phases/cmip7/fast-track/) brings together around 58 priority experiments, including the DECK and future scenarios, selected from Community MIPs. Its page includes an experiment viewer showing each experiment and the MIP that proposed it.

    - [List of CMIP7 experiments](https://esgvoc.ipsl.fr/concept/experiment?projects=cmip7)
    - [Experiment setup and forcings](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Experiment_set_up_and_Forcings/)

## Models

??? info "Source, institution and variant"

    #### Source, institution and variant

    - **Source** is the model name (for example, `ACCESS-ESM1-6`). See the [list of CMIP7 models](https://esgvoc.ipsl.fr/concept/model?projects=cmip7).
    - **Institution** is the organisation that ran the model.
    - **Variant** identifies each member of an ensemble, such as `r1i1p1f1`. The letters stand for realisation (different starting conditions), initialisation method, physics version and forcing version.

    Models broadly fall into two types. **Coupled climate models** simulate the atmosphere, ocean, land and sea ice. **Earth system models** also simulate the carbon cycle, and can be driven by emissions rather than concentrations.

    To compare how models are built, see the [Essential Model Documentation](https://wcrp-cmip.github.io/Essential-Model-Documentation/docs/Model/). To see how they perform, see the [Rapid Evaluation Framework dashboard](https://dashboard.climate-ref.org).

## Variables

??? info "Branded variables"

    #### Branded variables

    CMIP7 introduces **branded variables**, which add a suffix to the short variable name describing how it is processed: time averaging, vertical level, horizontal and area type.

    For example, near-surface air temperature `tas` becomes `tas_tavg-h2m-hxy-u`: a time average (`tavg`), at 2 m height (`h2m`), on a horizontal grid (`hxy`), over all surface types (`u`).

    Frequency is now specified separately from the variable. CMIP6's `Amon.tas` (monthly atmospheric `tas`) is equivalent to the CMIP7 compound name `atmos.tas_tavg-h2m-hxy-u.mon.GLB`, which combines realm, branded variable, frequency and region.

    - [List of requested branded variables](https://cmip-data-request.github.io/cmip7-dreq-webview/latest/variables.html)
    - [Branded variable documentation](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Branded_Variables/)
    - [CMIP7 Data Request](https://bit.ly/CMIP7-DReq-latest)

??? info "Frequency, realm and grid"

    #### Frequency, realm and grid

    - **Frequency** is how often data is reported, such as `mon` (monthly) or `day` (daily). Check each dataset's calendar too, as models use different ones (for example, `noleap` or `360_day`).
    - **Realm** is the part of the climate system, such as `atmos`, `ocean` or `land`.
    - **Grid** identifies the model grid the data is on. Use the [horizontal](https://wcrp-cmip.github.io/Essential-Model-Documentation/docs/grid_viewer/horizontal/) and [vertical](https://wcrp-cmip.github.io/Essential-Model-Documentation/docs/grid_viewer/vertical/) grid viewers for details.
