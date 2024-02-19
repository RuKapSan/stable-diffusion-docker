from huggingface_hub import snapshot_download
import os

print("Downloading models from huggingface_hub")
snapshot_download(repo_id="rkpsturbologo/models", local_dir='/sd-models/', local_dir_use_symlinks=True, token=os.getenv("HUGGINGFACE_TOKEN"))
