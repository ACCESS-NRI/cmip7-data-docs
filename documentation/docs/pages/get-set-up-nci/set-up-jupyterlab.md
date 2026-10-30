---
page_nav: true
---

# Set up JupyterLab (ARE) for CMIP7

One way to analyse CMIP7 data on Gadi is in a JupyterLab session, which you can run in your web browser through NCI's [Australian Research Environment (ARE)](https://are.nci.org.au). The ACCESS-Hive Docs [ARE guide](https://docs.access-hive.org.au/getting_started/are/) explains how to launch a session. This page lists the settings you need to work with CMIP7 data.

??? info "What exactly is the ARE?"
    ARE (short for Australian Research Environment) is a web-based graphical interface for performing your computational research. It combines the familiarity of your regular desktop/laptop with the power of NCI's world-class research HPC capabilities. ARE gives you access to NCI's Gadi supercomputer and data collections, all from a simple, graphical interface. ARE consists of a number of applications that support your research such as Virtual Desktop, JupyterLab, Terminal, etc.

## ARE settings for CMIP7

??? info "Set up an ARE JupyterLab session for CMIP7 data analysis"
    Use your NCI account to log in to the [Australian Research Environment (ARE)](https://are.nci.org.au) website. Select JupyterLab and enter the following to launch a JupyterLab session with the CMIP7 projects and the `conda/analysis3` Python environment.

    | Setting | Value |
    |---|---|
    | Walltime | The amount of time you'd like the JupyterLab session to run (typically 1-8 hours) |
    | Queue | If you're not sure, `normalbw` is a good default. See [NCI's Queue Structure](https://opus.nci.org.au/spaces/Help/pages/90308824/Queue+Structure) for more details |
    | Compute Size | Choose the amount of resources (CPUs, memory) appropriate for your analysis (click the arrow on the right of the box to view the options) |
    | Project | Your compute project (see [Set up an NCI account](set-up-account.md#2-compute-project)) |
    | Storage | `gdata/xp65+gdata/ib12+gdata/im55` |
    | Module directories (under *Show advanced settings*) | `/g/data/xp65/public/modules` |
    | Modules (under *Show advanced settings*) | `conda/analysis3` |

    Leave all other fields blank.

    !!! note
        You need to insert all project folders you plan to use for storage locations. For example, add `+gdata/[your compute project]` or `+scratch/[your compute project]` to the storage setting if you want to save outputs there, or `+gdata/oi10+gdata/fs38` if you're also using CMIP6 data.

## Where to work

??? info "Where to analyse and save your outputs"
    - **Read CMIP7 data directly on NCI.** It's already on NCI, so there's no need to copy it anywhere. Copying wastes your storage allocation and can leave you with outdated versions.
    - **Save outputs to your own project.** You can't write to the CMIP7 data projects. Use your compute project's `/scratch` area for temporary files (files there are deleted automatically after 90 days if left unused) and its `/g/data` area for anything you want to keep.

    For everything else, including logging in via SSH, running batch jobs and checking your storage and compute usage, see [NCI's user documentation](https://opus.nci.org.au).

## Next steps

[Work with CMIP7 data](../work-with-cmip7-data/index.md).
