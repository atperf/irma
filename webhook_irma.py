from flask import Flask, request
import subprocess
import hmac
import hashlib
import os

app = Flask(__name__)

GITHUB_SECRET = os.environ.get("a002bd876d1ea42865cd1c23484c8ae90c7b498b", "")  # optional
REPO_PATH = "irma"  # <-- change this to your actual repo path

def verify_signature(payload, signature):
    if not GITHUB_SECRET:
        return True

    mac = hmac.new(GITHUB_SECRET.encode(), msg=payload, digestmod=hashlib.sha256)
    expected = "sha256=" + mac.hexdigest()
    return hmac.compare_digest(expected, signature)

@app.route("/webhook", methods=["POST"])
def webhook():
    signature = request.headers.get("X-Hub-Signature-256")
    payload = request.data

    if not verify_signature(payload, signature):
        return "Invalid signature", 403

    try:
        subprocess.run(["git", "pull"], cwd=REPO_PATH, check=True)
        return "Updated successfully", 200
    except subprocess.CalledProcessError as e:
        return f"Git pull failed: {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
