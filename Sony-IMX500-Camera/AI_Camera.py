import subprocess

def run_inference():
    # Run the camera with your model
    result = subprocess.run([
        "rpicam-hello",
        "-t", "0s",
        "--post-process-file", "/path/to/model_config.json",
        "--model", "/path/to/model_rpk"
    ], capture_output=True, text=True)
    print(result.stdout)

if __name__ == "__main__":
    run_inference()
