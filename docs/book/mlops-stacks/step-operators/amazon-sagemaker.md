---
description: How to execute individual steps in SageMaker
---

The SageMaker step operator is a [step operator](./step-operators.md) flavor provided with
the ZenML `aws` integration that uses [SageMaker](https://aws.amazon.com/sagemaker/)
to execute individual steps of ZenML pipelines.

## When to use it

You should use the SageMaker step operator if:
* one or more steps of your pipeline require computing resources (CPU, GPU, memory) that are
not provided by your orchestrator.
* you have access to SageMaker. If you're using a different cloud provider, take 
a look at the [Vertex](./gcloud-vertexai.md) or [AzureML](./azureml.md) step operators.

## How to deploy it

* Create a role in the IAM console that you want the jobs running in SageMaker to assume.
This role should at least have the `AmazonS3FullAccess` and `AmazonSageMakerFullAccess`
policies applied. Check [here](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html#sagemaker-roles-create-execution-role) for a guide on how to set up this role.

## How to use it

To use the SageMaker step operator, we need:
* The ZenML `aws` integration installed. If you haven't done so, run 
    ```shell
    zenml integration install aws
    ```
* [Docker](https://www.docker.com) installed and running.
* An IAM role with the correct permissions. See the [deployment section](#how-do-you-deploy-it)
for detailed instructions.
* An [AWS container registry](../container-registries/amazon-ecr.md) as part of our stack.
Take a look [here](../container-registries/amazon-ecr.md#how-to-deploy-it) for a guide on how to set that up.
* The `aws` cli set up and authenticated. Make sure you have the permissions to create 
and manage SageMaker runs.
* An instance type that we want to execute our steps on.
See [here](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-available-instance-types.html)
for a list of available instance types.
* (Optional) An experiment which is used to group SageMaker runs. Check [this guide](https://docs.aws.amazon.com/sagemaker/latest/dg/experiments-create.html) to see how to create an experiment.

We can then register the step operator and use it in our active stack:
```shell
zenml step-operator register <NAME> \
    --flavor=sagemaker \
    --role=<SAGEMAKER_ROLE> \
    --instance_type=<INSTANCE_TYPE> \
#   --experiment_name=<SEXPERIMENT_NAME> # optionally specify an experiment to assign this run to

# Add the step operator to the active stack
zenml stack update -s <NAME>
```

Once you added the step operator to your active stack, you can use it to
execute individual steps of your pipeline by specifying it in the `@step` decorator as follows:
```python
from zenml.steps import step

@step(custom_step_operator=<NAME>)
def trainer(...) -> ...:
    """Train a model."""
    # This step will be executed in SageMaker.
```

{% hint style="info" %}
ZenML will build a Docker image called `zenml-sagemaker` which includes your code and use it
to run your steps in SageMaker. Check out
[this page](../../developer-guide/advanced-usage/docker.md)
if you want to learn more about how ZenML builds these images and
how you can customize them.

If you decide you need the full flexibility of having a
[custom base image](../../developer-guide/advanced-usage/docker.md#using-a-custom-base-image),
you can update your existing step operator
```shell
zenml step-operator update <NAME> \
--base_image=<IMAGE_NAME>
```
or set it when registering a new SageMaker step operator:
```shell
zenml step-operator register <NAME> \
--flavor=sagemaker \
--base_image=<IMAGE_NAME>
...
```
{% endhint %}


A concrete example of using the SageMaker step operator can be found 
[here](https://github.com/zenml-io/zenml/tree/main/examples/step_operator_remote_training).

For more information and a full list of configurable attributes of the SageMaker step operator, check out the 
[API Docs](https://apidocs.zenml.io/latest/api_docs/integrations/#zenml.integrations.aws.step_operators.sagemaker_step_operator.SagemakerStepOperator).
