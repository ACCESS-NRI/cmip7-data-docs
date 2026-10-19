# Tools to analyze CMIP7 data

The [Find and access CMIP7 data](../find-and-access-data/) page shows how to discover files with the interactive or [Intake catalogue](https://docs.access-hive.org.au/model_evaluation/data/finding/access_nri_intake/) and open them as Xarray datasets in ARE JupyterLab. You can explore those datasets directly in your notebook. For repeatable diagnostics, use the same model, experiment and variable selection with an evaluation tool below; these tools locate and load the source files themselves. On Gadi, you need access to the NCI project holding the data.

**Where to start:** Explore existing CMIP7 evaluations on the [REF dashboard](https://dashboard.climate-ref.org/), or browse [ESMValTool's recipes](https://docs.esmvaltool.org/en/latest/quickstart/running.html) to run a diagnostic yourself. ILAMB focuses on land processes and ACCESS-ENSO recipes on ENSO. ACCESS-MOPPy prepares raw ACCESS output; published CMIP data is already CMORised.

??? info "Rapid Evaluation Framework (REF) — automated CMIP7 evaluation"

    #### Rapid Evaluation Framework (REF)

    The international [CMIP REF effort](https://www.wcrp-cmip.org/cmip-phases/cmip7/rapid-evaluation-framework/) uses [REF software](https://climate-ref.readthedocs.io/) to automate evaluation: it identifies needed diagnostics, runs them through providers such as ESMValTool and ILAMB, and tracks results across models. To analyse existing results, use the [dashboard](https://dashboard.climate-ref.org/) or follow the [API notebook example](https://climate-ref.readthedocs.io/en/latest/how-to-guides/using-pre-computed-results/) and [API reference](https://api.climate-ref.org/docs). These use hosted results and need no local REF installation.

    **On Gadi:** REF is not part of ACCESS-NRI's [documented supported evaluation environments](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/). To evaluate local CMORised files yourself, set up REF separately using its [modelling-centre guide](https://climate-ref.readthedocs.io/en/latest/getting-started/modelling-centres/) and [Gadi PBS example](https://climate-ref.readthedocs.io/en/latest/how-to-guides/hpc_executor/).

??? info "ESMValTool — reusable diagnostics"

    #### ESMValTool

    [ESMValTool](https://docs.esmvaltool.org/) evaluates climate models with reusable *recipes* that select data, preprocess it and produce diagnostics. Select a recipe and set its dataset details to match the files you found. **On Gadi:** Run recipes as PBS jobs with `xp65` [`conda/analysis3`](https://docs.access-hive.org.au/getting_started/environments/), following the [ACCESS-NRI guide](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/esmvaltool_workflow/).

    **Using ARE:** [ESMValCore](https://docs.esmvaltool.org/projects/ESMValCore/en/latest/) is the library behind ESMValTool's file selection and preprocessing. The [Gadi guide](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/esmvaltool_workflow/) shows how to use it interactively in a notebook. It loads the selected files as Iris cubes, so an Xarray dataset already opened through Intake is a separate notebook workflow.

??? info "ILAMB — land-process benchmarking"

    #### ILAMB

    [ILAMB](https://www.ilamb.org/) compares modelled land processes with observations and produces scores and plots, including for the carbon and water cycles. Use it for land-model benchmarking. **On Gadi:** The [ACCESS-NRI ILAMB workflow](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/ilamb_workflow/) provides `conda/analysis3`, reference data and running instructions.

??? info "ACCESS-ENSO recipes — interactive ENSO diagnostics"

    #### ACCESS-ENSO recipes

    The [ACCESS-ENSO recipes](https://github.com/ACCESS-NRI/ACCESS-ENSO-recipes) are notebooks for exploring ENSO metrics with ESMValCore. Use them to inspect or adapt an ENSO diagnostic. **On Gadi:** The [ACCESS-NRI recipes guide](https://docs.access-hive.org.au/model_evaluation/evaluation_on_gadi/recipes/) explains how to run them in ARE with `conda/analysis3`.

??? info "ACCESS-MOPPy — prepare raw ACCESS output"

    #### ACCESS-MOPPy

    [ACCESS-MOPPy](https://access-moppy.readthedocs.io/en/latest/howto/esmvaltool_integration.html) prepares CMORised files from raw ACCESS model output. Modellers can use its ESMValTool integration to CMORise the variables needed by a recipe into a local cache on demand. Published CMIP files do not need this preparation. **On Gadi:** MOPPy is [available in `conda/analysis3`](https://access-moppy.readthedocs.io/en/latest/howto/installation.html).
