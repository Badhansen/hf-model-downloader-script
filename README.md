# Hugging Face Model Downloader

This script provides a command-line interface (CLI) for securely downloading Hugging Face models with retry logic. It handles authentication, manages downloads, and resumes interrupted processes.

## Features

-   Securely downloads models from the Hugging Face Hub.
-   Uses a Hugging Face token for authentication.
-   Includes retry logic to handle network interruptions.
-   Resumes interrupted downloads.
-   Provides a command-line interface for easy use.

## Prerequisites

-   Python 3.8+
-   [uv](https://github.com/astral-sh/uv) package manager
-   Hugging Face account and API token, You can find this at: https://huggingface.co/settings/tokens

## Installation

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd hf-model-downloader-script
    ```

2.  **Create a virtual environment (recommended) & Install the dependencies using uv:**

    ```bash
    uv sync
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

## Configuration

1.  **Set up your Hugging Face token:**

    -   Create a `.env` file in the project root.
    -   Add your Hugging Face token to the `.env` file:

        ```
        HF_TOKEN=your_hugging_face_token
        ```

## Usage

1.  **Run the script from the command line:**

    ```bash
    uv run llm_downloader.py <repo_id> --save_path <save_path>
    ```

    -   `<repo_id>`: The Hugging Face repository ID (e.g., `meta-llama/Llama-3.2-1B`).
    -   `--save_path`: (Optional) The directory to save the model. Defaults to `models/`.

    **Example:**

    ```bash
    uv run python llm_downloader.py meta-llama/Llama-3.2-1B --save_path models/
    ```

    This command will download the `meta-llama/Llama-3.2-1B` model to the `models/` directory.

## Help

To see all available options, run:

```bash
    python llm_downloader.py --help
```

## Error Handling

-   If the `HF_TOKEN` is not found, the script will raise a `ValueError`. Ensure that you have set the `HF_TOKEN` in your `.env` file or as an environment variable.
-   The script includes retry logic to handle potential network issues during the download. If the download fails after multiple attempts, a `ValueError` will be raised.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests.

## License

[MIT License](LICENSE)
