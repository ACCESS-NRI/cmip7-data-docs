# What CMIP7 data is available?

CMIP7 data are published internationally through the Earth System Grid Federation (ESGF). NCI Gadi holds the ACCESS Consortium's published contribution and a selected set of replicas from other modelling centres. **Finding a dataset on ESGF does not mean it has been copied to Gadi.**

## Published internationally on ESGF

ESGF is a distributed archive: modelling and data centres publish datasets on nodes around the world, and ESGF indexes let you search across them. The [Climate Resource CMIP7 availability dashboard](https://www.climate-resource.com/tools/esm-model/cmip7-availability) is a quick way to see which models, experiments and variables have been published. Use [ESGF MetaGrid](https://metagrid-ceda.east.esgf.io/search) to search individual datasets and find access options. See [Find and access CMIP7 data](find-and-access-data.md#discover-published-data-worldwide) for the steps and other tools.

The archive is still growing. On **20 October 2026**, the Climate Resource dashboard reported about **724 TB** of CMIP7 data indexed on ESGF. This is a snapshot of data published so far, not an estimate of the eventual total. Check the live dashboard for the current size.

## Available on NCI Gadi

| NCI project | What it holds | Coverage |
| --- | --- | --- |
| `im55` | ACCESS Consortium CMIP7 publications | The complete ACCESS Consortium submission published through NCI, under `/g/data/im55/publications`. |
| `ib12` | Replicas of CMIP7 data from other modelling centres | A selected collection, not a complete copy of ESGF. |

The `ib12` selection is guided by ACCESS community research priorities, including the variables and output frequencies most useful to local users. Replicating the entire growing ESGF archive on Gadi is not practical. To check whether the specific model, experiment, variable, frequency and version you need are local, follow the [Gadi discovery steps](find-and-access-data.md#find-data-already-on-gadi).

If an international dataset is on ESGF but absent from `ib12`, you can [request additional data for Gadi](#request-additional-international-data-on-gadi) or use an [international access route](find-and-access-data.md#access-data-from-esgf).

## Request additional international data on Gadi

Contact the [ACCESS-NRI data team](https://docs.access-hive.org.au/model_evaluation/data/sharing/#how-to-request-support) with a link to the ESGF dataset and the model, experiment, variable, frequency, ensemble member and version you need. Explain your research use and expected storage volume if known. Requests help inform which additional replicas are prioritised; submission does not guarantee that a dataset will be copied.
