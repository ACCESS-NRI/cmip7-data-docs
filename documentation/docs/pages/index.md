<!-- # MODIFY -->
# CMIP7 Data in Australia

The Coupled Model Intercomparison Project Phase 7 (CMIP7) is an international climate modelling initiative that brings together simulations from modelling centres around the world to support climate research, projections and assessment. This site is a guide to CMIP7 data for the Australian community: what is CMIP7, Australia's contribution, and how to find, access and analyse Australian and international CMIP7 data on NCI's Gadi supercomputer.

??? tip "Already worked with CMIP data on NCI? Your quick route through this site"
    These pages cover the main differences for CMIP7:

    1. **[Join CMIP7 projects](get-set-up-nci/join-projects.md#cmip7-projects)**: 
        - [`ib12`](https://my.nci.org.au/mancini/project/ib12/join): CMIP7 international replicas on NCI
        - [`im55`](https://my.nci.org.au/mancini/project/im55/join): CMIP7 ACCESS model data
    2. **[What's changed in CMIP7](about-cmip7/experiments-data-standards.md#whats-changed-in-cmip7)**: a quick summary of the new variable names, file paths and experiments.
    3. **[What CMIP7 data is available?](find-cmip7-data/data-available.md)**: CMIP7 data is still being published, so check what's there so far.
    4. **[ACCESS-NRI Interactive Data Catalogue](find-cmip7-data/find-and-access-data.md#access-nri-interactive-data-catalogue)**: try this new tool to search the data on NCI and get code to load it.

<div class="home-btn-container">
  <a href="about-cmip7/" class="home-btn home-btn--orange">
    <div class="home-btn__title">New to CMIP7</div>
    <ul class="home-btn__list">
      <li>What is CMIP7?</li>
      <li>Australia's role in CMIP7</li>
      <li>CMIP7 experiments and data standards</li>
    </ul>
  </a>
  <a href="find-cmip7-data/" class="home-btn home-btn--blue">
    <div class="home-btn__title">Find CMIP7 data</div>
    <ul class="home-btn__list">
      <li>What CMIP7 data is available?</li>
      <li>Find and access CMIP7 data</li>
    </ul>
  </a>
  <a href="get-set-up-nci/" class="home-btn home-btn--orange">
    <div class="home-btn__title">Get set up on NCI</div>
    <div class="home-btn__note">
      <div><i class="fa-solid fa-database"></i> A lot of CMIP7 data is available on NCI.</div>
      <div><i class="fa-solid fa-unlock"></i> You don't need an NCI account for every access method.</div>
</div>
    <ul class="home-btn__list">
      <li>NCI's role in CMIP7</li>
      <li>Set up an NCI account, join projects, and set up JupyterLab (ARE)</li>
    </ul>
  </a>
  <a href="work-with-cmip7-data/" class="home-btn home-btn--blue">
    <div class="home-btn__title">Work with CMIP7 data</div>
    <ul class="home-btn__list">
      <li>Explore and evaluate CMIP7 data</li>
      <li>Citing requirements and errata</li>
    </ul>
  </a>
</div>

<div class="home-btn-container home-btn-container--small">
  <div class="home-btn-small home-btn-small--disabled">
    <i class="fa-solid fa-upload"></i>
    For data producers: Publish CMIP7 data to ESGF (in development)
  </div>
  <a href="help/" class="home-btn-small">
    <i class="fa-solid fa-circle-question"></i>
    Need help?
  </a>
</div>

??? question "Feeling a bit lost?"
    **If anything is unclear, just reach out.** We're happy to clarify anything related to CMIP (or point you in the right direction)!

    [<i class="fa-solid fa-circle-question"></i> Get help](help.md){ .home-btn-small .home-btn-small--inline }
    { .text-center }
    
    CMIP7 is a **huge international collaboration** with lots of moving parts. It can be a lot to take in, especially when you're just starting out.

    

## Who's behind this site

This site is a collaboration between NCI and ACCESS-NRI:

- **[NCI](https://nci.org.au/)** (National Computational Infrastructure) hosts Australia’s Earth System Grid Federation (ESGF) node, where it publishes and replicates CMIP7 data. NCI provides the high-performance computing and data infrastructure that researchers use to access and analyse CMIP7 data, along with guidance and support for using its platform.
- **[ACCESS-NRI](https://www.access-nri.org.au/)** (Australia’s Climate Simulator) works with the research community to develop and support the ACCESS models and standardise model outputs for sharing and reuse. ACCESS-NRI also provides tools, documentation and support to help researchers work with CMIP7 data.

## CMIP7 data delivery

As part of the 2025 [National Collaborative Research Infrastructure Strategy (NCRIS)](https://www.education.gov.au/ncris) funding round, ACCESS-NRI and NCI have secured new Australian Government support for CMIP7 data publication and access in Australia. The funding also supports the upgrade of [NCI's ESGF node](https://esgf.nci.org.au/search), which shares climate model data with the international research community.

This work forms part of the broader Australia's Next-Generation Earth System Model activity, led by ACCESS-NRI in partnership with NCI, the [Terrestrial Ecosystem Research Network (TERN)](https://www.tern.org.au/), [CSIRO](https://www.csiro.au/en/) and the [University of New South Wales (UNSW)](https://www.unsw.edu.au/). It supports the development of Australia's next generation of climate and Earth system modelling capability.

For more information, see [NCRIS funding rounds for ACCESS-NRI projects announced](https://www.access-nri.org.au/ncris-funding-rounds-for-access-nri-projects-announced/) on the ACCESS-NRI website.

## Australia's CMIP7 Assessment Fast Track submission

Model development for Australia's contribution to the CMIP7 Assessment Fast Track, ACCESS-ESM1.6, was supported by Australian Government funding through the National Environmental Science Program (NESP) and the 2023 National Collaborative Research Infrastructure Strategy (NCRIS) funding round. The submission is led by CSIRO in partnership with the Bureau of Meteorology, Monash University, University of Melbourne and ACCESS-NRI.

For more information, see:

- [ACCESS development and delivery to CMIP7](https://nesp2climate.com.au/research/access-development-and-delivery-to-cmip7/) on the NESP Climate Systems Hub website
- [2023 NCRIS Funding Round for ACCESS modelling announced](https://www.access-nri.org.au/2023-research-infrastructure-investment-plan-funding-for-access-modelling-announced/) on the ACCESS-NRI website

See [Australia's role in CMIP7](about-cmip7/australia-in-cmip7.md) for more about ACCESS, ACCESS-ESM1.6, who's involved and how to get involved.

*Note: Information on this website about data availability, access and user guidance will be updated as the work progresses.*