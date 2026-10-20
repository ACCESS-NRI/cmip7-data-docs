# Find and access CMIP7 data

## On Gadi

??? info "ACCESS-NRI Interactive Data Catalogue"

    ### ACCESS-NRI Interactive Data Catalogue

    The [ACCESS-NRI Interactive Data Catalogue](https://access-nri.github.io/interactive-data-catalogue/#/) is the easiest place to start looking for CMIP7 data on Gadi. It runs in your web browser, so you can search for data before logging in to Gadi or writing any code.

    In the catalogue you can:

    - search and filter datasets by attributes such as model, variable, frequency and realm
    - narrow your selection down to only the files you need
    - generate a Python code snippet that loads your selection

    To access the data you've found:

    1. Join the NCI projects shown in the catalogue for your selection (see [Join CMIP7 projects](../../get-set-up-nci/join-projects/)).
    2. Copy the code snippet from the catalogue.
    3. Run the snippet in an [ARE JupyterLab session](../../get-set-up-nci/set-up-jupyterlab/) on Gadi to load your data.

    You can browse the catalogue without an NCI account, but to load the data you'll need to have an NCI account.

    !!! note "Under development"
        The Interactive Data Catalogue is still being developed, so some features may change.

??? info "Browse the Gadi filesystem directly"

    ### Browse the Gadi filesystem directly

    These paths are mainly useful if you prefer to manage files directly. The [ACCESS-NRI Intake catalogue](https://docs.access-hive.org.au/model_evaluation/data/finding/access_nri_intake/) can discover and load indexed datasets in Python without you managing paths.

    CMIP7 replicas are stored in NCI project `ib12`. ACCESS Consortium publications are stored in project `im55`, under `/g/data/im55/publications`. You need to [join the relevant NCI projects](../../get-set-up-nci/join-projects/) to read the files.

    The following complete paths **illustrate** the CMIP7 [Data Reference Syntax](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Global_Attributes/) under each collection root. They are not confirmed live files; check the catalogue or filesystem for the current path and version.

    International replica (`ib12`):

    ```text
    /g/data/ib12/MIP-DRS7/CMIP7/CMIP/CCCma/CanESM6-0-MR/historical/r2i1p1f1/glb/mon/tas/tavg-h2m-hxy-u/g121/v20250622/tas_tavg-h2m-hxy-u_mon_glb_g121_CanESM6-0-MR_historical_r2i1p1f1_190001-190912.nc
    ```

    ACCESS Consortium publication (`im55`):

    ```text
    /g/data/im55/publications/MIP-DRS7/CMIP7/CMIP/ACCESS-Consortium/ACCESS-ESM1-6/historical/r1i1p1f1/glb/mon/tas/tavg-h2m-hxy-u/gn/v20260819/tas_tavg-h2m-hxy-u_mon_glb_gn_ACCESS-ESM1-6_historical_r1i1p1f1_185001-185912.nc
    ```

    Here, `mon` means monthly output, `r1i1p1f1` identifies an ensemble member, `v20260819` identifies a dataset version, and the filename ends with its time span.


## Data available internationally


