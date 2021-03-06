from os.path import join

from tensorflow.python.keras.callbacks import ModelCheckpoint, CSVLogger

from ccmlutils.callbacks.ccmlprojectcallback import CCMLProjectCallback
from ccmlutils.callbacks.gitversioncallback import GitVersionCallback
from ccmlutils.utilities.factoryutils import subs_path_and_create_folder


def model_callback_factory(exp_path: str, model_subfolder: str, *args, **kwargs):
    filepath = join(exp_path, model_subfolder)
    filepath = subs_path_and_create_folder(filepath)
    return ModelCheckpoint(filepath=filepath, *args, **kwargs)


def logging_callback_output(filename: str, *args, **kwargs):
    filename = subs_path_and_create_folder(filename)
    return CSVLogger(filename=filename, *args, **kwargs)


def git_callback_factory(filepath: str, *args, **kwargs):
    filepath = subs_path_and_create_folder(filepath)
    return GitVersionCallback(filepath, *args, **kwargs)


def ccmlproject_callback_factory(filepath: str, *args, **kwargs):
    filepath = subs_path_and_create_folder(filepath)
    return CCMLProjectCallback(filepath, *args, **kwargs)
