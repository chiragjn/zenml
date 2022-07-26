---
description: How to orchestrate ML pipelines
---

The orchestrator is an essential component in any MLOps stack as 
it is responsible for running your machine learning pipelines.
To do so, the orchestrator provides an environment which is set up
to execute the steps of your pipeline. It also makes sure that
the steps of your pipeline only get executed once all their inputs
(which are outputs of previous steps of your pipeline) are available.

{% hint style="info" %}
Many of ZenML's remote orchestrators build [Docker](https://www.docker.com/)
images in order to transport and execute your pipeline code. If you want to 
learn more  about how Docker images are built by ZenML, check out
[this guide](../../developer-guide/advanced-usage/docker.md).
{% endhint %}

## When to use it

The orchestrator is a mandatory component in the ZenML stack. It is used
to store all artifacts produced by pipeline runs and you are required to
configure it in all of your stacks.

## Orchestrator Flavors

Out of the box, ZenML comes with a `local` orchestrator already part of the
default stack that runs pipelines locally. Additional orchestrators
are provided by integrations:

| Orchestrator         | Flavor    | Integration    | Notes |
|----------------------------|-----------|----------------|-------------|
| [LocalOrchestrator](./local.md)   | `local`   | _built-in_     | Runs your pipelines locally. |
| [KubernetesOrchestrator](./kubernetes.md) | `kubernetes` | `kubernetes`     | Runs your pipelines in Kubernetes clusters. |
| [KubeflowOrchestrator](./kubeflow.md)       | `kubeflow`       | `kubeflow`    | Runs your pipelines using Kubeflow. |
| [VertexOrchestrator](./gcloud-vertexai.md)     | `vertex`     | `gcp`     | Runs your pipelines in Vertex AI. |
| [AirflowOrchestrator](./airflow.md)    | `airflow`    | `airflow`     | Runs your pipelines locally using Airflow. |
| [GitHubActionsOrchestrator](./github-actions.md)    | `github`    | `github`     | Runs your pipelines using GitHub Actions. |

If you would like to see the available flavors of orchestrators, you can 
use the command:

```shell
zenml orchestrator flavor list
```

## How to use it

You don't need to directly interact with any ZenML orchestrator in your code.
As long as the orchestrator that you want to use is part of your active 
[ZenML stack](../../developer-guide/stacks-profiles-repositories/stack.md),
using the orchestrator is as simple as executing a python file which 
[runs a ZenML pipeline](../../developer-guide/steps-pipelines/steps-and-pipelines.md#instantiate-and-run-your-pipeline):

```shell
python file_that_runs_a_zenml_pipeline.py
```
