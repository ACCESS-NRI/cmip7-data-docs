# Tools to analyze CMIP7 data

Published CMIP data is already CMORised and can be used directly with evaluation tools. On Gadi, you need access to the NCI project holding the data. ACCESS-NRI provides Gadi workflows for ESMValTool and ILAMB through the `xp65` [`conda/analysis3` environment](https://docs.access-hive.org.au/getting_started/environments/).

## ESMValTool

[ESMValTool](https://docs.esmvaltool.org/) evaluates climate models using reusable *recipes*. A recipe selects datasets, defines preprocessing, and runs diagnostics to produce plots or statistics—for example, comparing several models with observations. The [ACCESS-NRI Gadi guide](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/esmvaltool_workflow/) covers running recipes in PBS jobs and using ESMValCore interactively in ARE notebooks.

## ILAMB

[ILAMB](https://www.ilamb.org/) focuses on land processes. It compares model variables with observational datasets and produces quantitative scores and plots, making it useful for evaluating processes such as the carbon and water cycles. The [ACCESS-NRI ILAMB workflow](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/ilamb_workflow/) provides the software, observational data, and instructions for running comparisons on Gadi.

## Rapid Evaluation Framework (REF)

The [REF](https://climate-ref.readthedocs.io/en/latest/concepts/) coordinates evaluation for the CMIP7 Assessment Fast Track. It determines which diagnostics need to run, delegates the calculations to providers including ESMValTool and ILAMB, and tracks their results. It can evaluate local CMORised data before publication; the [modelling-centre guide](https://climate-ref.readthedocs.io/en/latest/getting-started/modelling-centres/) and [Gadi PBS example](https://climate-ref.readthedocs.io/en/latest/how-to-guides/hpc_executor/) explain that workflow.

## ACCESS-ENSO recipes

The [ACCESS-ENSO recipes](https://github.com/ACCESS-NRI/ACCESS-ENSO-recipes) are notebooks for exploring ENSO metrics, using ESMValCore to find and preprocess model data. They offer an interactive starting point for developing diagnostics, which can also be run as ESMValTool recipes. The [ACCESS-NRI evaluation recipes guide](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/recipes/) explains how to use them on Gadi.

## Preparing raw ACCESS output

[ACCESS-MOPPy](https://access-moppy.readthedocs.io/en/latest/howto/esmvaltool_integration.html) converts raw ACCESS output into CMORised files. Its ESMValTool integration identifies the variables a recipe needs and prepares them in a local cache before the recipe runs. Users working with published CMIP files can skip this step because those files are already CMORised.

The [ACCESS-NRI Intake Catalogue](https://docs.access-hive.org.au/model_evaluation/data/finding/access_nri_intake/) can help find and load datasets covered by the catalogue.
