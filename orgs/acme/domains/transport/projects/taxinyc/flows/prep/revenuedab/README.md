# Deploy pipeline with brickops as DAB

## Example commands for running on local machine

Plan:

```
uv run databricks --profile training-iprod bundle plan --target=dev --debug
```

Deploy:

```
uv run databricks --profile training-iprod bundle deploy --target=dev --debug
```

Run:

```
uv run databricks --profile training-iprod bundle run --target=dev --debug
```

