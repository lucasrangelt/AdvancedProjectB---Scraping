import great_expectations as gx
import sys

def func():
    context = gx.get_context()
    try:
        checkpoint = context.checkpoints.get("gx_data_quality_checkpoint")
    except KeyError:
        print("ERROR: Run setup_gx.py first.")
        sys.exit(1)
    result = checkpoint.run()
    if not result.success:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    func()