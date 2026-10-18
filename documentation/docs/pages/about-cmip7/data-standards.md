# CMIP7 data standards and structure

This page is for users who prefer to work with files directly on Gadi. For datasets indexed in the [ACCESS-NRI Intake catalogue](https://access-nri-intake-catalog.readthedocs.io/en/latest/usage/), you can discover and load data in Python without managing file paths yourself.

CMIP7 output is stored in NetCDF (`.nc`) files. Its [Data Reference Syntax (DRS)](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Global_Attributes/) uses standard metadata to organise directories and filenames by model, experiment, ensemble member, variable, grid and dataset version.

## On Gadi

International replicas are held in project `ib12`, while ACCESS Consortium publications are held in project `im55`, under `/g/data/im55/publications`. You need [access to the relevant NCI project](https://docs.access-hive.org.au/getting_started/set_up_nci_account/#join-relevant-nci-projects) to read its files.

These complete paths **illustrate the CMIP7 format** under the two Gadi collection roots, using examples from the WCRP guidance and [ACCESS-MOPPy](https://access-moppy.readthedocs.io/en/latest/howto/cmorise_ilamb_workflow.html). They are not confirmed live file locations; check the collection for the current directory and version.

```text
/g/data/ib12/MIP-DRS7/CMIP7/CMIP/CCCma/CanESM6-0-MR/historical/r2i1p1f1/glb/mon/tas/tavg-h2m-hxy-u/g121/v20250622/tas_tavg-h2m-hxy-u_mon_glb_g121_CanESM6-0-MR_historical_r2i1p1f1_190001-190912.nc
```

```text
/g/data/im55/publications/MIP-DRS7/CMIP7/CMIP/ACCESS-Consortium/ACCESS-ESM1-6/historical/r1i1p1f1/glb/mon/tas/tavg-h2m-hxy-u/gn/v20260819/tas_tavg-h2m-hxy-u_mon_glb_gn_ACCESS-ESM1-6_historical_r1i1p1f1_185001-185912.nc
```

Here, `mon` means monthly output, `r1i1p1f1` identifies an ensemble member, `v20260819` identifies a dataset version, and the final part of each filename gives its time span. The [official CMIP7 guidance](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Global_Attributes/) explains the full structure and changes from CMIP6, including branded variable names and the new region field.
