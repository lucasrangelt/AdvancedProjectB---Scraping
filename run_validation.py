import great_expectations as gx
import sys
import os
from pathlib import Path

def func():
    project_path = Path(__file__).parent.resolve()
    context = gx.get_context(project_root_dir=str(project_path))
    try:
        checkpoint = context.checkpoints.get("gx_data_quality_checkpoint")
    except KeyError:
        print("CHECKPOINT NOT FOUND. Run setup_gx.py first.")
        sys.exit(1)
    result = checkpoint.run()
    context.build_data_docs()
    if not result.success:
        print("Data quality warning: validations not passed.")
        sys.exit(1)
    else:
        print("Data quality passed! Safe to trigger dbt.")
        sys.exit(0)

if __name__ == "__main__":
    func()