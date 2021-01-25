def split_train_test_data(path: str, split_size: float = 0.7) -> tuple:
    """
    Splits a directory with images into test and train subsets ordered by class

    Args:
        path: path including all images
        split_size: ratio - 0.7 => 70% train and 30% test

    Returns:
        tuple of paths to train and test data set
    """
    labels = _read_label(path)
    _mkdir(path, labels)

    for label in labels:
        import os

        files = os.listdir(os.path.join(path, label))

        import random

        random.shuffle(files)
        split_idx = int(len(files) * split_size)
        train = files[0:split_idx]
        test = files[split_idx : len(files)]

        for img in train:
            _move_file(path, label, img, "train")

        for img in test:
            _move_file(path, label, img, "test")

    _rm_old_dirs(path, labels)

    return f"{path}/train/", f"{path}/test/"


def _move_file(path: str, label: str, img: str, data_set: str):
    """
    Moves an image to a subdirectory using dataset like "train" or "test"
    Args:
        path: absolute path
        label: class
        img: image file name
        data_set: train or test subset

    Returns:

    """
    import shutil

    shutil.move(f"{path}/{label}/{img}", f"{path}/{data_set}/{label}/{img}")


def _read_label(path: str) -> [str]:
    """
    read subdirectories from path
    Args:
        path: absolute path

    Returns:
        list of subdirectories
    """
    from pathlib import Path

    files = Path(path).iterdir()
    folders = list(map(lambda y: str(y.name), filter(lambda x: x.is_dir(), files)))
    return list(filter(lambda x: "train" not in x and "test" not in x, folders))


def _mkdir(path: str, labels: [str]):
    """
    creates subdirectories for test and train
    Args:
        path: dataset path

    Returns:

    """
    from pathlib import Path

    for label in labels:
        Path(path).joinpath("test").joinpath(label).mkdir(parents=True, exist_ok=True)
        Path(path).joinpath("train").joinpath(label).mkdir(parents=True, exist_ok=True)


def _rm_old_dirs(path: str, labels: [str]):
    """
    remove old image directories after moving into subsets
    Args:
        path: path to image dir
        labels: subdirectory of class labels

    Returns:

    """
    from pathlib import Path

    for label in labels:
        Path(path).joinpath(label).rmdir()
