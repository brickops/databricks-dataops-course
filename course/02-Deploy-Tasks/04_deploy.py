# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Deploy tasks
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Study: deployment.yml
# MAGIC
# MAGIC Look at `orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deployment.yml`.
# MAGIC It defines the job which will run the pipeline.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run dev deploy
# MAGIC
# MAGIC 1. Go to the notebook orgs/acme/domains/transport/projects/taxinyc/flows/prep/revenue/deploy
# MAGIC 2. Connect to serverless compute.
# MAGIC 3. Run the cells up to and including deploying and running the dev job.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Look for the job under Job Runs
# MAGIC
# MAGIC Job Runs are on the side menu

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: Run the job by pressing the run button in the UI

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Task: What is the difference between a job and a job run?

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC A job is script or collection of script that together forms a pipeline. A job run is a specific instance of this job / a specific run. 

# COMMAND ----------

# MAGIC %md
# MAGIC ## Task: How was the job name composed?
# MAGIC
# MAGIC Write answer in the empty cell below.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC Via the deployment.yml file
