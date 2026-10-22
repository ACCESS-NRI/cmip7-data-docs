# CMIP7 data standards and structure

CMIP7 data follows shared rules so output from different modelling centres can be found and compared. This page explains those rules; see [Find and access CMIP7 data](../../work-with-cmip7-data/find-and-access-data/) for file locations on Gadi.

## Requirements

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
