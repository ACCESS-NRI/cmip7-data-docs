# Set up JupyterLab (ARE) for CMIP7

One way to analyse CMIP7 data on Gadi is in a JupyterLab session, which you can run in your web browser through NCI's [Australian Research Environment (ARE)](https://are.nci.org.au). The ACCESS-Hive Docs [ARE guide](https://docs.access-hive.org.au/getting_started/are/) explains how to launch a session. This page lists the settings you need to work with CMIP7 data.

## ARE settings for CMIP7

??? info "ARE settings for CMIP7"
    When launching a JupyterLab session, enter:

    | Setting | Value |
    |---|---|
    | Project | Your compute project (see [Set up an NCI account](set-up-account.md)) |
    | Storage | `gdata/xp65+gdata/[CMIP7 replica project]+gdata/[Australian CMIP7 project]` |
    | Module directories (under *Advanced options*) | `/g/data/xp65/public/modules` |
    | Modules (under *Advanced options*) | `conda/analysis3` |

    Add `+gdata/[your compute project]` to the storage setting if you want to save outputs there, and `+gdata/oi10+gdata/fs38` if you're also using CMIP6 data.

    !!! warning "Getting a 'No such file or directory' error?"
        Joining a project isn't enough on its own. Every project whose data you want to read must also be listed in the session's *Storage* setting. Check this first if you can't see data you expect to have access to.

## Where to work

??? info "Where to work"
    - **Read CMIP7 data where it is.** It's already on NCI, so there's no need to copy it. Copying wastes your storage allocation and can leave you with outdated versions.
    - **Save outputs to your own project.** You can't write to the CMIP7 data projects. Use your compute project's `/scratch` area for temporary files (files there are deleted automatically if left unused) and its `/g/data` area for anything you want to keep.

    For everything else, including logging in via SSH, running batch jobs and checking your storage and compute usage, see [NCI's user documentation](https://opus.nci.org.au).

## Next steps

[Find the CMIP7 data you need](../work-with-cmip7-data/find-and-access-data.md) and [analyse it](../work-with-cmip7-data/analysis-tools.md).
