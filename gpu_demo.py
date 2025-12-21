import modal
app=modal.App("gpu-demo")
@app.function(gpu=["A10G"])
def check_gpu():
    import subprocess
    try:
        subprocess.run(["nvidia-smi","--list-gpus"])
    except Exception:
        print("no gpus")

    