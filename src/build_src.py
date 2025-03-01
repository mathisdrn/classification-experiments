from pathlib import Path
from get_dataset import dataset_loaders
from papermill import execute_notebook
import nbformat as nbf

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
        execute_notebook(TEMPLATE, output_path, parameters={"dataset": dataset}, prepare_only=True)
        
        # Load the notebook
        nb = nbf.read(output_path, as_version=4)
        
        # Create a new markdown cell with the frontmatter
        frontmatter = f"---\ntitle: {dataset}\n---"
        md_cell = nbf.v4.new_markdown_cell(frontmatter)
        
        # Insert the markdown cell at the top of the notebook
        nb.cells.insert(0, md_cell)
        
        # Write the notebook back to the file
        nbf.write(nb, output_path)

if __name__ == "__main__":
    build_src()