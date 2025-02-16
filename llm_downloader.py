from huggingface_hub import snapshot_download, login
from dotenv import load_dotenv
import argparse
import time
import os


class HuggingFaceModelDownloader:
    """Securely download Hugging Face models with retries."""
    
    def __init__(self, token_env_var: str = "HF_TOKEN"):
        """Initialize with Hugging Face API token."""
        load_dotenv()
        self.hf_token = os.getenv(token_env_var)
        
        if not self.hf_token:
            raise ValueError("HF_TOKEN not found! Set it in .env or environment variables.")
        
        # Login to avoid permission issues
        login(token=self.hf_token)

    def download_model(self, repo_id: str, save_path: str = "models/", retries: int = 3):
        """Download a model with retry logic."""
        model_path = os.path.join(save_path, repo_id.split("/")[-1])
        
        print(f"Downloading: {repo_id} into {model_path}...")

        for attempt in range(1, retries + 1):
            try:
                snapshot_download(
                    repo_id=repo_id,
                    local_dir=model_path,
                    token=self.hf_token,
                    resume_download=True,  # Resume instead of forcing a new download
                    force_download=False   # Avoid unnecessary force download
                )
                print(f"Download complete: {model_path}")
                return model_path
            except Exception as e:
                print(f"Attempt {attempt} failed: {e}")
                if attempt < retries:
                    print("Retrying in 10 seconds...")
                    time.sleep(10)
                else:
                    raise ValueError("Model download failed after multiple attempts.")


def main():
    # Create argument parser
    parser = argparse.ArgumentParser(description='Download Hugging Face models')
    parser.add_argument('repo_id', type=str, 
                       help='The repository ID (e.g., "meta-llama/Llama-3.2-1B")')
    parser.add_argument('--save_path', type=str, default="models/",
                       help='Directory to save the model (default: models/)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Initialize downloader and download model
    downloader = HuggingFaceModelDownloader()
    model_path = downloader.download_model(
        repo_id=args.repo_id,
        save_path=args.save_path
    )
    print(f"Model downloaded to: {model_path}")


if __name__ == "__main__":
    main()