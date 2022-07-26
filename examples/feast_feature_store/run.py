#  Copyright (c) ZenML GmbH 2022. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at:
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
#  or implied. See the License for the specific language governing
#  permissions and limitations under the License.

from pipeline import feast_pipeline
from steps.getter.get_features_step import get_features
from steps.printer.printer_step import print_historical_features

from zenml.logger import get_logger
from zenml.repository import Repository

logger = get_logger(__name__)


if __name__ == "__main__":
    pipeline = feast_pipeline(
        get_features=get_features,
        feature_printer=print_historical_features(),
    )

    pipeline.run()

    repo = Repository()
    pipeline = repo.get_pipeline("feast_pipeline")
    last_run = pipeline.runs[-1]
    historical_features_step = last_run.get_step(name="feature_printer")
    print("HISTORICAL FEATURES:")
    print(historical_features_step.output.read())
