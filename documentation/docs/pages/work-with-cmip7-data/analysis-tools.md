# Tools to analyze CMIP7 data

The [Find and access CMIP7 data](../find-and-access-data/) page shows how to discover files with the interactive or [Intake catalogue](https://docs.access-hive.org.au/model_evaluation/data/finding/access_nri_intake/) and open them as Xarray datasets in ARE JupyterLab. You can explore those datasets directly in your notebook. For larger evaluations, use the same model, experiment and variable selection in a recipe or configuration; the evaluation tool will reopen the CMORised source files.

**Where to start:** Explore existing CMIP7 evaluations on the [REF dashboard](https://dashboard.climate-ref.org/), or browse [ESMValTool's recipes](https://docs.esmvaltool.org/en/latest/quickstart/running.html) to run a diagnostic yourself. ILAMB focuses on land processes and ACCESS-ENSO recipes on ENSO.

## Hosted REF results

??? info "Rapid Evaluation Framework (REF) — automated CMIP7 evaluation"

    #### Rapid Evaluation Framework (REF)

    The international [CMIP REF effort](https://www.wcrp-cmip.org/cmip-phases/cmip7/rapid-evaluation-framework/) uses [REF software](https://climate-ref.readthedocs.io/) to automate evaluation: it identifies needed diagnostics, runs them through providers such as ESMValTool and ILAMB, and tracks results across models. To analyse existing results, use the [dashboard](https://dashboard.climate-ref.org/) or follow the [API notebook example](https://climate-ref.readthedocs.io/en/latest/how-to-guides/using-pre-computed-results/) and [API reference](https://api.climate-ref.org/docs). These hosted results require neither Gadi access nor a local REF installation.

## Interactive analysis in ARE JupyterLab

Use `xp65` [`conda/analysis3`](https://docs.access-hive.org.au/getting_started/environments/) and join the NCI project holding your data.

??? info "ESMValCore — find and preprocess data in a notebook"

    #### ESMValCore

    [ESMValCore](https://docs.esmvaltool.org/projects/ESMValCore/en/latest/) is the Python library behind ESMValTool's file selection and preprocessing. The [ACCESS-NRI Gadi guide](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/esmvaltool_workflow/) shows how to use it in an ARE notebook. It loads selected files as Iris cubes, so an Xarray dataset already opened through Intake is a separate notebook workflow.

??? info "ACCESS-ENSO recipes — interactive ENSO diagnostics"

    #### ACCESS-ENSO recipes

    The [ACCESS-ENSO recipes](https://github.com/ACCESS-NRI/ACCESS-ENSO-recipes) are notebooks for exploring ENSO metrics with ESMValCore. Use them to inspect or adapt an ENSO diagnostic. The [ACCESS-NRI recipes guide](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/recipes/) explains how to run them in ARE with `conda/analysis3`.

## Evaluation in Gadi PBS jobs

Run ESMValTool recipes and ILAMB evaluations as PBS jobs, rather than inside ARE JupyterLab. Both use `xp65` [`conda/analysis3`](https://docs.access-hive.org.au/getting_started/environments/) and access to the relevant NCI data projects. You can inspect their results in ARE afterward.

??? info "ESMValTool — reusable diagnostics"

    #### ESMValTool

    [ESMValTool](https://docs.esmvaltool.org/) evaluates climate models with reusable *recipes* that select data, preprocess it and produce diagnostics. Select a recipe and set its dataset details to match the files you found. Run it as a PBS job, following the [ACCESS-NRI Gadi guide](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/esmvaltool_workflow/).

??? info "ILAMB — land-process benchmarking"

    #### ILAMB

    [ILAMB](https://www.ilamb.org/) compares modelled land processes with observations and produces scores and plots, including for the carbon and water cycles. Use it for land-model benchmarking. Run it as a PBS job, following the [ACCESS-NRI ILAMB workflow](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/ilamb_workflow/) and [PBS example](https://ilamb-workflow.readthedocs.io/en/latest/source/ILAMB.html#submitting-a-pbs-job).
