from pathlib import Path
from get_dataset import dataset_loaders
# Parametrize and execute notebooks to build source code
from papermill import execute_notebook

DESTINATION_FOLDER = Path("src_built/")
print(f"Working directory: {Path.cwd()}")
TEMPLATE = Path("src/template.ipynb")

def build_src():
    datasets = list(dataset_loaders.keys())
    print(f"Building source code for {len(datasets)} datasets")
    
    if not DESTINATION_FOLDER.exists():
        DESTINATION_FOLDER.mkdir()
        
    for i, dataset in enumerate(datasets):
        output_path = DESTINATION_FOLDER / f"{i} - {dataset}.ipynb"
        execute_notebook(TEMPLATE, output_path, parameters={"dataset": dataset})
    pass

if __name__ == "__main__":
    build_src()