from zenml.integrations.label_studio.label_config_generators import (
    generate_image_classification_label_config,
)
from zenml.integrations.label_studio.steps import (
    LabelStudioDatasetSyncParameters,
    sync_new_data_to_label_studio,
)

IMAGE_REGEX_FILTER = ".*(jpe?g|png)"


_, label_config_type = generate_image_classification_label_config(
    ["aria", "not_aria"]
)


# AZURE
zenml_azure_artifact_store_sync_params = LabelStudioDatasetSyncParameters(
    storage_type="azure",
    label_config_type=label_config_type,
    regex_filter=IMAGE_REGEX_FILTER,
)
azure_data_sync = sync_new_data_to_label_studio(
    params=zenml_azure_artifact_store_sync_params,
)

# GCLOUD
zenml_gcs_artifact_store_sync_params = LabelStudioDatasetSyncParameters(
    storage_type="gcs",
    label_config_type=label_config_type,
    regex_filter=IMAGE_REGEX_FILTER,
)
gcs_data_sync = sync_new_data_to_label_studio(
    params=zenml_gcs_artifact_store_sync_params,
)

# AWS
zenml_s3_artifact_store_sync_params = LabelStudioDatasetSyncParameters(
    storage_type="s3",
    label_config_type=label_config_type,
    regex_filter=IMAGE_REGEX_FILTER,
    s3_region_name="eu-west-1",  # change this to your closest region
)
s3_data_sync = sync_new_data_to_label_studio(
    params=zenml_s3_artifact_store_sync_params,
)
