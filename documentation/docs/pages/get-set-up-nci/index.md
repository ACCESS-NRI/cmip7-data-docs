# Get set up on NCI

Most Australian researchers work with CMIP7 data at the National Computational Infrastructure (NCI), Australia's national research computing facility. This section explains why and how to get set up.

## Why use NCI for CMIP7?

??? info "Why use NCI for CMIP7?"

    CMIP7 data is produced by modelling centres around the world and shared through the Earth System Grid Federation (ESGF), a global network of data nodes. Anyone can search ESGF and download data, but CMIP7 datasets are very large, so downloading enough for most analyses is slow and needs a lot of storage.

    NCI is Australia's node in this network. It keeps a copy of a selection of international CMIP7 data, and Australian modelling groups publish their CMIP7 data to NCI too. This means you can:

    - **Skip the download.** The data sits right next to NCI's Gadi supercomputer, so you can analyse it where it is.
    - **Use ready-made tools.** A maintained Python environment with common climate analysis packages is already set up.


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