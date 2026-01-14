from databricks.bundles.core import Bundle, job_mutator, pipeline_mutator
from databricks.bundles.jobs import Job
from databricks.bundles.pipelines import Pipeline
from brickops.dab.mutators.job_mutators import brickops_job_params
from brickops.dab.mutators.pipeline_mutators import brickops_pipeline_params


import logging

logging.info("This is an info message")


@job_mutator
def job_brickops(bundle: Bundle, job: Job) -> Job:
    return brickops_job_params(bundle, job)


@pipeline_mutator
def pipeline_brickops(bundle: Bundle, pipeline: Pipeline) -> Pipeline:
    return brickops_pipeline_params(bundle, pipeline)
