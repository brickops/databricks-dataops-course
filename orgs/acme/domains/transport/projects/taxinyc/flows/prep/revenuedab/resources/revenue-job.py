from databricks.bundles.jobs import (
    CronSchedule,
    Job,
    PerformanceTarget,
    Task,
    NotebookTask,
    TaskDependency,
)

job = Job(
    name="revenue",
    performance_target=PerformanceTarget.PERFORMANCE_OPTIMIZED,
    # parameters=[
    #     JobParameterDefinition()
    # ]
    # schedule=CronSchedule(
    #     quartz_cron_expression="0 0 8 ? * * *",
    #     timezone_id="UTC" # Every day at 8 clock in the morning.
    # ),
    parameters=[
        {"name": "my_job_id", "default": "silly_id"},
        {"name": "run_msg", "default": "default_run_msg"},
    ],
    tasks=[
        Task(
            task_key="revenue_by_borough",
            notebook_task=NotebookTask(notebook_path="src/revenue_by_borough.py"),
        ),
        Task(
            task_key="revenue_by_tripmonth",
            notebook_task=NotebookTask(notebook_path="src/revenue_by_tripmonth.py"),
        ),
        Task(
            task_key="borough_population",
            notebook_task=NotebookTask(notebook_path="src/borough_population.py"),
        ),
        Task(
            # NotebookTaskDict(
            task_key="revenue_per_inhabitant",
            notebook_task=NotebookTask(
                notebook_path="src/revenue_per_inhabitant.py",
            ),
            depends_on=[
                TaskDependency(task_key="revenue_by_borough"),
                TaskDependency(task_key="borough_population"),
            ],
        ),
    ],
)
