import subprocess

def ask_llm(prompt):
    process = subprocess.Popen(
        ["ollama", "run", "phi3"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    stdout, _ = process.communicate(prompt.encode("utf-8"))

    return stdout.decode("utf-8", errors="ignore")
