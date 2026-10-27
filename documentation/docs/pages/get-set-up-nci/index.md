# Get set up on NCI

Most Australian researchers access and analyse CMIP7 data through the **National Computational Infrastructure (NCI)**, Australia's national research computing facility. This section walks you through getting set up to work with CMIP7 data on NCI.

??? warning "Do you need an NCI account?"
    There are ways to search and access CMIP7 data with and without an NCI account. If you're eligible, we recommend working with CMIP7 data directly on NCI. If you're not, you can still access CMIP7 data through the ESGF. See the options on the [Find and access CMIP7 data](../work-with-cmip7-data/find-and-access-data.md) page to help you decide.

    **Who is eligible for an NCI account?** NCI accounts are intended for Australian-based researchers and staff at universities, government science agencies and other NCI collaborators. If you're not sure if you're eligible, talk with your employer.

## Why work with CMIP7 data on NCI?

CMIP7 data is produced by climate modelling centres around the world and distributed through the Earth System Grid Federation (ESGF), a global network of interconnected data nodes that enables international sharing of climate and Earth system science data. Anyone can search and download CMIP7 data directly from ESGF, but the datasets are often extremely large, making download, storage and management challenging for many research projects.

As Australia's ESGF node, NCI hosts CMIP7 data alongside its high-performance computing environment, so you can analyse data where it resides instead of transferring it.

??? info "What you get with NCI access"
    Researchers with access to NCI benefit from:

    - **Local access to CMIP7 datasets** hosted on NCI storage systems, including selected international model outputs and Australian CMIP7 datasets.
    - **High-performance analysis capabilities** through direct access to the Gadi supercomputer and associated data-intensive computing infrastructure.
    - **Ready-to-use scientific software environments**, including maintained Python environments with commonly used climate analysis packages and tools.
    - **Robust data management and stewardship**, with datasets managed according to ESGF standards for version control, metadata management, provenance tracking, and preservation.

??? info "More about NCI's role in CMIP7 and ESGF"
    NCI is Australia's only **ESGF** node and serves as the **Tier 1 ESGF node for the Australia and Oceania region**. It maintains high-capacity network connections with major ESGF nodes in North America, the United Kingdom, and Europe, enabling efficient international data exchange and replication.

    NCI has been a key component of the global climate data infrastructure since CMIP3, continuing through CMIP5, CMIP6, and now CMIP7. It hosts authoritative replicas of high-demand datasets from international modelling centres, and publishes ACCESS CMIP7 model outputs to the ESGF so they are discoverable and reusable by the international research community.

```mermaid
flowchart LR
    esgf["<b>ESGF</b><br/>CMIP7 data from modelling<br/>centres worldwide"]
    subgraph nci["NCI"]
        rep["Copies of<br/>international data"]
        aus["Australian-published<br/>data"]
    end
    gadi["<b>You</b><br/>analysing on Gadi"]
    esgf -->|selected datasets copied to NCI| rep
    aus -->|shared worldwide| esgf
    rep --> gadi
    aus --> gadi
```

To see exactly which data is available on NCI, see [What CMIP7 data is available?](../work-with-cmip7-data/data-available.md)

<div class="home-btn-container home-btn-container--three">
  <a href="set-up-account/" class="home-btn home-btn--orange home-btn--title-only">
    <div class="home-btn__title">Set up an NCI account</div>
  </a>
  <a href="join-projects/" class="home-btn home-btn--orange home-btn--title-only">
    <div class="home-btn__title">Join CMIP7 projects</div>
  </a>
  <a href="set-up-jupyterlab/" class="home-btn home-btn--orange home-btn--title-only">
    <div class="home-btn__title">Set up JupyterLab (ARE) for CMIP7</div>
  </a>
</div>
