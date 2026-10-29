# Find and access CMIP7 data

CMIP7 data for the Australian community can be accessed in two places:

1. **NCI**: stored in projects on the Gadi supercomputer in Australia, with options to access it with or without an NCI account.
2. **ESGF**: the global archive distributed through the Earth System Grid Federation.

This page helps you choose the right way to find and access the data you need, and points you to the guides for each option.

!!! info "Most CMIP7 data is currently being replicated to NCI"
    For now, all published monthly CMIP7 data is being replicated to NCI, so the data you need is likely available on NCI. See [What CMIP7 data is available?](data-available.md) for the latest status.

??? tip "If you have access to NCI, start with data held there"
    - Search available data in the [Interactive Data Catalogue](#access-nri-interactive-data-catalogue). Use the quick links at the top of the page to search for CMIP7-related datasets.
    - Be sure to [join the relevant projects](../get-set-up-nci/join-projects.md).

## Which option is right for me?

??? info "Compare the options"

    ```mermaid
    flowchart TD
        A[Do you have an NCI account?] -->|Yes| B[Is your data on Gadi?]
        A -->|No| C[Is your data on Gadi?]
        B -->|Yes| D[Find: Interactive Data Catalogue - start here]
        B -->|No| E[ESGF Python tools, run on Gadi]
        D --> F[Do you work in Python?]
        F -->|Yes| G[Access: run the generated code in ARE JupyterLab, or use the Intake catalogue]
        F -->|No: shell scripts or batch jobs| H[Access: Gadi file paths]
        C -->|Yes, small amounts| I[NCI THREDDS]
        C -->|No, not sure, or large amounts| J[ESGF MetaGrid or Python tools]
    ```

    | Option | Find or access? | NCI account needed? |
    |---|---|---|
    | [ACCESS-NRI Interactive Data Catalogue](#access-nri-interactive-data-catalogue) **(start here)** | Find, with code to access | No to browse; yes to open the data |
    | [ACCESS-NRI Intake catalogue](#access-nri-intake-catalogue) | Find and access | Yes |
    | [Gadi file system](#advanced-fallback-nci-file-system) | Access | Yes |
    | [NCI THREDDS](#nci-thredds) | Access | No |
    | [ESGF MetaGrid](#esgf-metagrid) | Find and access | No |
    | [ESGF Python tools](#esgf-python-tools) | Find and access | No |

## Find and access data to work on NCI

If you have or are eligible for an NCI account, we recommend using NCI's Gadi to work with CMIP7 data. A lot of CMIP7 data is already there, so you can analyse it in place without downloading anything.

!!! tip "Before you start"
    Make sure you've [joined the CMIP7 projects](../get-set-up-nci/join-projects.md) (`ib12`, the CMIP7 replica project; `im55`, the Australian CMIP7 project; and `xp65`) and know how to [start a JupyterLab session with the CMIP7 settings](../get-set-up-nci/set-up-jupyterlab.md#are-settings-for-cmip7). Project approval can take 1–2 business days.

??? info "ACCESS-NRI Interactive Data Catalogue"

    #### ACCESS-NRI Interactive Data Catalogue

    [<i class="fa-solid fa-magnifying-glass"></i> Open the Interactive Data Catalogue](https://access-nri.github.io/interactive-data-catalogue/){ .home-btn-small .home-btn-small--inline }

    The ACCESS-NRI Interactive Data Catalogue is the recommended way to find CMIP7 data on Gadi. This web-based catalogue runs in your browser and lets you filter the data by model, experiment, variable, frequency, and several other options. Once you've found what you need, it gives you ready-to-run Python code to load it: paste the code into an [ARE JupyterLab session](../get-set-up-nci/set-up-jupyterlab.md) (with the correct projects in the storage field) and you're ready to analyse!

    Anyone can browse the catalogue, but running the code needs an NCI account and project membership.

    !!! note
        The Interactive Data Catalogue is a community resource. If something doesn't work or you have any other feedback, click the green *Give us feedback* button at the top of the page.

??? info "ACCESS-NRI Intake catalogue"

    #### ACCESS-NRI Intake catalogue

    If you'd rather search for data in Python, you can use the ACCESS-NRI Intake catalogue. It's the tool the Interactive Data Catalogue's code is built on: you search by attributes and load the results into Xarray without needing to know where the files are. Its [quickstart tutorial](https://access-nri-intake-catalog.readthedocs.io/en/latest/usage/quickstart.html) shows how to filter by model, variable and frequency, then open matching files.

    See the [ACCESS-NRI Intake catalogue documentation](https://access-nri-intake-catalog.readthedocs.io/en/latest/) to get started.

??? info "Advanced fallback: NCI file system"

    #### Advanced fallback: NCI file system

    If you work with shell scripts, batch jobs or tools that need file paths, you can read the CMIP7 files directly from NCI's storage via a terminal. This method is best for accessing data that you already know exists, rather than searching for what data is available on NCI.

    The local collection root paths are:

    ```text
    /g/data/im55/publications/MIP-DRS7/CMIP7/   # ACCESS model CMIP7 publications
    /g/data/ib12/MIP-DRS7/CMIP7/                # selected international replicas
    ```

    Under either root, a directory follows this pattern:

    ```text
    <activity_id>/<institution_id>/<source_id>/<experiment_id>/<variant_label>/<region>/<frequency>/<variable_id>/<branding_suffix>/<grid_label>/<version>/
    ```

    For example, `mon` means monthly output, `r1i1p1f1` identifies an ensemble member and a `vYYYYMMDD` component identifies a dataset version. The [CMIP7 DRS (Data Reference Syntax) specification](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Global_Attributes/) defines the full structure. Check the filesystem for actual filenames and the current version before using a path in a script.

    For logging in to Gadi and running batch jobs, see [NCI's user documentation](https://opus.nci.org.au/).

??? info "Can't find the CMIP7 data you want on NCI?"

    #### Can't find the CMIP7 data you want on NCI?

    If a dataset isn't on Gadi, you can download it from ESGF into your own project's storage by running the [ESGF Python tools](#esgf-python-tools) on Gadi. Check your storage quota first.

    !!! tip "Check if data is available on NCI before downloading from ESGF!"
        If you work on Gadi, check whether the exact model, experiment, variable, frequency and version you need are already available on NCI (e.g. via the [Interactive Data Catalogue](#access-nri-interactive-data-catalogue)) before downloading from ESGF. Broad CMIP7 selections can involve very large transfers and duplicate data that are already available locally. If there is no local copy, request that the data be replicated to NCI (note: this option is not available yet) or download only the files you need.

## Without an NCI account or to work on platforms other than NCI

### The global archive of CMIP7 data (ESGF)

The Earth System Grid Federation is the international network of data centres that hosts the official global CMIP7 archive. The [CMIP7 Guidance for Data Users](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_users/) webpage has a lot of useful information, some of which we outline below.

??? info "ESGF MetaGrid"

    #### ESGF MetaGrid

    [<i class="fa-solid fa-magnifying-glass"></i> Open MetaGrid](https://esgf.nci.org.au/search){ .home-btn-small .home-btn-small--inline }

    ESGF's web interface for searching the global archive and downloading files through your browser. Best for browsing and for downloading small amounts of data. More details about accessing the CMIP7 global data archive on the [CMIP7 Guidance for Data Users](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_users/#1-accessing-cmip7-data).

    
    

??? info "Other ways to access CMIP7 data without an NCI account"

    #### Python tools and other platforms

    A list of other CMIP7 data access methods via ESGF, including some Python tools, can be found on the [CMIP7 Guidance for Data Users](https://wcrp-cmip.github.io/cmip7-guidance/docs/CMIP7/Guidance_for_users/#1-accessing-cmip7-data).

### Download ACCESS model CMIP7 data directly from NCI

In addition to downloading straight from ESGF, you can download ACCESS model CMIP7 data directly from NCI. You can search for data via the [Interactive Data Catalogue](#access-nri-interactive-data-catalogue), for instance, and then use this method to download the data you need.

??? info "NCI THREDDS"

    #### NCI THREDDS

    NCI's web data server. You can download individual files, or use OPeNDAP to read just the part of a file you need (for example a region or time period) straight into Python. Best for small amounts of data.

    <!-- TODO: add the CMIP7 THREDDS catalogue link as a button, e.g.
    [<i class="fa-solid fa-magnifying-glass"></i> Open the CMIP7 THREDDS catalogue](URL){ .home-btn-small .home-btn-small--inline }
    -->

## Next steps

Once you have the data, see [Tools to analyse CMIP7 data](analysis-tools.md).
