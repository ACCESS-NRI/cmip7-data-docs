# What CMIP7 data is available?

The ACCESS Consortium's complete CMIP7 submission published through NCI is available on Gadi in project `im55`. Project `ib12` brings together **selected replicas** from other modelling centres. Its variables and output frequencies are chosen around ACCESS community research priorities, so `ib12` is not a complete copy of data published internationally. If you have [access to Gadi](https://docs.access-hive.org.au/getting_started/set_up_nci_account/), [look for the data there first](find-and-access-data.md#find-and-use-data-held-on-nci-gadi), then use ESGF for anything that has not been replicated.

CMIP7 publication through the Earth System Grid Federation (ESGF) is ongoing. On **20 October 2026**, the [Climate Resource availability dashboard](https://www.climate-resource.com/tools/esm-model/cmip7-availability) reported about **724 TB** indexed on ESGF. This is a snapshot of published data. [WCRP forecasts 6–10 PB](https://www.wcrp-cmip.org/cmip7-task-teams/cdnot/) from the initial Assessment Fast Track and **more than 80 PB** over CMIP7's lifetime. These are projections, not current holdings. Replicating the whole growing archive on Gadi is not practical.

## Available on NCI Gadi

??? info "Gadi collections"

    | NCI project | What it holds | Coverage |
    | --- | --- | --- |
    | `im55` | ACCESS Consortium CMIP7 publications | The complete submission published through NCI, under `/g/data/im55/publications`. |
    | `ib12` | Replicas from other modelling centres | Selected models, experiments, variables and frequencies; not all ESGF data. |

    To check a particular model, experiment, variable, frequency and version, follow the [Gadi discovery steps](find-and-access-data.md#find-and-use-data-held-on-nci-gadi). An ESGF search result alone does not establish that a local replica exists.

## Published internationally on ESGF

??? info "Explore international publication"

    ESGF is a distributed archive: modelling and data centres host datasets on nodes around the world. The [Climate Resource CMIP7 availability dashboard](https://www.climate-resource.com/tools/esm-model/cmip7-availability) summarises published models, experiments and variables. [ESGF MetaGrid](https://metagrid-ceda.east.esgf.io/search) searches individual datasets and provides access options. See [Find and access CMIP7 data](find-and-access-data.md#worldwide-via-esgf) for the steps and other tools.

## Request additional international data on Gadi

If an international dataset is on ESGF but absent from `ib12`, contact the [ACCESS-NRI data team](https://docs.access-hive.org.au/model_evaluation/data/sharing/#how-to-request-support) with a link to the ESGF dataset and the model, experiment, variable, frequency, ensemble member and version you need. Explain your research use and expected storage volume if known. Requests help inform which additional replicas are prioritised; submission does not guarantee that a dataset will be copied.
