# Find and access CMIP7 data

CMIP7 data are published internationally through the Earth System Grid Federation (ESGF). You can explore what has been published worldwide, then check whether the data you need are already available on NCI Gadi.

**If you have access to Gadi, use the [Gadi route](#on-nci-gadi) first.** If you are new to NCI, [set up an account and join the relevant data projects](https://docs.access-hive.org.au/getting_started/set_up_nci_account/). The complete ACCESS Consortium CMIP7 submission published through NCI is in project `im55`. Project `ib12` holds selected replicas from other modelling centres, with variables and frequencies chosen around ACCESS community research priorities. It is not a complete copy of ESGF: a dataset you find internationally may not be on Gadi. You can [request an additional replica](data-available.md#request-additional-international-data-on-gadi) or [access it through ESGF](#worldwide-via-esgf).

As a guide to scale, the [Climate Resource availability dashboard](https://www.climate-resource.com/tools/esm-model/cmip7-availability) reported about **724 TB** of CMIP7 data indexed on ESGF on **20 October 2026**. This is the amount published so far, not a forecast of the final archive size; the collection is still growing.

## On NCI Gadi

??? info "Find and load data on Gadi"

    NCI provides collection-level Intake-ESM datastores for some data holdings, including `im55` and `ib12`. The [ACCESS-NRI Intake catalogue](https://access-nri-intake-catalog.readthedocs.io/en/latest/) brings indexed Gadi data products into a Python interface for discovery and loading. Its [quickstart tutorial](https://access-nri-intake-catalog.readthedocs.io/en/latest/usage/quickstart.html) shows how to filter by model, variable and frequency, then open matching files.

    #### Start with the interactive catalogue

    The [ACCESS-NRI Interactive Data Catalogue](https://access-nri.github.io/interactive-data-catalogue/#/) provides a browser interface to the ACCESS-NRI catalogue. You can explore indexed products without logging in to Gadi:

    1. Filter by model, experiment, variable and frequency.
    2. Inspect the matching product and required NCI project memberships.
    3. Narrow the selection to the files you need and copy the generated Python code.
    4. Run the code in an [ARE JupyterLab session](https://docs.access-hive.org.au/getting_started/are/) with access to the data project and the [ACCESS-NRI `analysis3` environment](https://docs.access-hive.org.au/getting_started/environments/).

    The [illustrated Interactive Catalogue guide](https://docs.access-hive.org.au/model_evaluation/data/finding/interactive_catalogue/) shows the interface. **As of October 2026, CMIP7 entries are not yet available in the Interactive Data Catalogue.** Until they are indexed, use the Gadi filesystem to find local CMIP7 files.

    #### Use the Gadi filesystem and CMIP7 DRS

    If you know the CMIP7 **Data Reference Syntax (DRS)**, you can navigate directly to files. DRS is the standard directory and filename structure based on facets such as activity, institution, model, experiment, ensemble member, variable, grid and version. This is useful for scripts that already use paths, or while a dataset is not indexed in a catalogue.

    The local collection roots are:

    ```text
    /g/data/im55/publications/MIP-DRS7/CMIP7/   # ACCESS Consortium publications
    /g/data/ib12/MIP-DRS7/CMIP7/                # selected international replicas
    ```

    Under either root, a directory follows this pattern:

    ```text
    <activity_id>/<institution_id>/<source_id>/<experiment_id>/<variant_label>/<region>/<frequency>/<variable_id>/<branding_suffix>/<grid_label>/<version>/
    ```

    For example, `mon` means monthly output, `r1i1p1f1` identifies an ensemble member and a `vYYYYMMDD` component identifies a dataset version. The [CMIP7 DRS specification](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Global_Attributes/) defines the full structure. Check the filesystem for actual filenames and the current version before using a path in a script.

## Worldwide via ESGF

??? info "Explore and access data worldwide through ESGF"

    1. Open the [Climate Resource CMIP7 availability dashboard](https://www.climate-resource.com/tools/esm-model/cmip7-availability) for an overview of models, experiments and variables published on ESGF. It does not show which files have been replicated on Gadi.
    2. Search [ESGF MetaGrid](https://metagrid-ceda.east.esgf.io/search) for a specific dataset, version or file. Its filters let you narrow the distributed ESGF catalogue and find download options from the hosting node.

    The [WCRP CMIP7 guidance for data users](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_users/) explains ESGF access routes and tool status. For larger scripted searches and downloads, WCRP lists [`intake-esgf`](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_users/#1-accessing-cmip7-data) among its CMIP7 Python tools. If the data are already on Gadi, use the local catalogue or filesystem to avoid a separate transfer.
