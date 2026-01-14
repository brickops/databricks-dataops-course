from databricks.bundles.core import Bundle, job_mutator
from databricks.bundles.jobs import Job
from brickops.dab.mutators.job_mutators import brickops_job_params


@job_mutator
def job_brickops(bundle: Bundle, job: Job) -> Job:
    return brickops_job_params(bundle, job)
