def yaml_list_from_dirs(source_path: str, dst_file: str) -> str:
    import os

    if not os.path.exists(source_path):
        raise ValueError(f"Could not find path: {source_path}")

    files = os.listdir(source_path)
    folders = list(filter(lambda x: os.path.isdir(os.path.join(source_path, x)), files))

    import yaml
    output = yaml.dump(folders, indent=len(folders))

    with open(dst_file, mode="w+") as file:
        file.write(output)

    return output
