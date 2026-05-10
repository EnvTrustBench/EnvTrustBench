import os
import sys
from pathlib import Path

from huggingface_hub import HfApi


DEFAULT_REPO_ID = "EnvTrustBench/envtrustbench-results"
ROOT = Path(__file__).resolve().parents[1]
DATASET_DIR = ROOT / "hf-dataset"


def main() -> int:
    repo_id = os.environ.get("HF_DATASET_REPO_ID", DEFAULT_REPO_ID)
    token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGINGFACE_HUB_TOKEN")
    if not token:
        print("Missing HF_TOKEN or HUGGINGFACE_HUB_TOKEN.", file=sys.stderr)
        print("Create a Hugging Face token with write access, then rerun.", file=sys.stderr)
        return 2

    api = HfApi(token=token)
    api.create_repo(repo_id=repo_id, repo_type="dataset", exist_ok=True, private=False)
    api.upload_folder(
        repo_id=repo_id,
        repo_type="dataset",
        folder_path=str(DATASET_DIR),
        commit_message="Add EnvTrustBench aggregate results",
    )
    print(f"https://huggingface.co/datasets/{repo_id}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
