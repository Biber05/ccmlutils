from typing import Dict

from tensorflow.keras.models import load_model, Model

from ccmlutils.utilities.experimentdata import ExperimentData

from ccmlutils.utilities.predictionutils import Predictions, prediction_factory


def defaulttest(test_set, experiment: ExperimentData) -> Predictions:
    model_path = experiment.get_model_path()
    model: Model = load_model(model_path)
    pred_output = model.predict(test_set)
    filenames = test_set.filenames
    class_indices = test_set.class_indices
    classes = test_set.classes
    predictions: Predictions = prediction_factory(
        pred_output, filenames, classes, class_indices
    )

    return predictions


def defaulttest_node(test_set, experiment: ExperimentData) -> Dict[str, Predictions]:
    return dict(predictions=defaulttest(test_set, experiment))
