---
page_nav: true
---

# Set up an NCI account

To work with CMIP7 data **locally** on the **National Computational Infrastructure (NCI)**, you will need:

1. **An NCI user account**
2. **Membership of a compute project**, which provides access to computing resources, storage and service units (SUs)
3. **Membership of the CMIP7 data projects**, which provides access to CMIP7 datasets

This page covers setting up an NCI account and joining a compute project. Information on CMIP7 data-project membership is provided on the [Join CMIP7 projects](join-projects.md) page.

## 1. NCI user account

??? info "Create an NCI user account"
    If you are an Australian researcher and do not have an [NCI account](https://opus.nci.org.au/display/Help/How+to+create+an+NCI+user+account), [sign up here](https://my.nci.org.au/mancini/signup/0). For detailed instructions and troubleshooting advice, see [Setting up your NCI account](https://opus.nci.org.au/spaces/Help/pages/26282120/Setting+up+your+NCI+Account).

## 2. Compute project

??? info "Get access to an NCI compute project"
    In order to access data locally at NCI's high-performance computer, you must be a member of an NCI compute project that provides access to computing resources, storage, and service units (SUs). Most researchers access these resources by joining an existing project through their supervisor, research group, institution, or NCI Scheme Manager. 
    
    If your research requires additional computing resources, you can apply for an allocation through one of NCI's access schemes, including the **National Computational Merit Allocation Scheme (NCMAS)** and the **Adapter Allocation Scheme**. For information on available allocation schemes and application processes, see NCI's [**Access Schemes**](https://www.nci.org.au/users/how-access-nci#AccessSchemes) page.

## Access NCI systems

Once your account is active, you can access NCI resources either through:

- [SSH access to Gadi](https://opus.nci.org.au/spaces/Help/pages/230491359/Connecting+to+Gadi), for command-line use and batch computing.
- The [Australian Research Environment (ARE)](https://are.nci.org.au), NCI's web-based research platform.

For most CMIP7 users, **ARE's JupyterLab** is the recommended way to get started (see [Set up JupyterLab (ARE) for CMIP7](set-up-jupyterlab.md) and [Work with CMIP7 data](../work-with-cmip7-data/index.md) for more info).

??? info "More about the ARE"
    ARE provides browser-based access to NCI's computing and data resources through applications such as:

    - **JupyterLab** for interactive analysis
    - **Virtual Desktop** for graphical workflows
    - **Terminal** for command-line access

    Through ARE, you can work with CMIP7 data on Gadi without installing specialised software or establishing an SSH connection.

    
Additional guidance on using NCI systems and services can be found in [NCI's user documentation](https://opus.nci.org.au/spaces/Help/overview).

## Not eligible for an NCI account?

??? info "There are other ways to access CMIP7 data"
    See [Find and access CMIP7 data](../find-cmip7-data/find-and-access-data.md) for options that work without an NCI account.
