from my_project import app #noqa: F401

if __name__ == "__main__":
    app.rung(host="0.0.0.0", port=5000, debug=True)