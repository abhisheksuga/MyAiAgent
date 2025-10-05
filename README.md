# My AI Agent

A simple, command-line AI agent built with Python that uses the Google Gemini API to perform various tasks. This project serves as a foundational example of integrating a large language model into an application.

---

## Features

- **Interactive Chat:** Ask questions and get responses directly from the Gemini model.
- **File Operations:** (Future feature) Will be able to read, write, and list files.
- **Code Execution:** (Future feature) Capable of running Python scripts in a sandboxed environment.

---

## Technologies Used

- **Python 3.11+**
- **Google Gemini API:** The core AI model.
- **uv:** An extremely fast Python package installer and resolver, written in Rust.
- **unittest:** For ensuring the reliability of the agent's internal logic.

---

## Setup and Installation

Follow these steps to get the project running on your local machine.

### 1. **Clone the repository**

```bash
git clone <https://github.com/abhisheksuga/MyAiAgent>
cd <myaiagent>

```
### 2. **Create a virtual environment using `uv`**


It's recommended to use a virtual environment to manage dependencies.

```bash
uv venv
source .venv/bin/activate

```
### 3. **Install dependencies using `uv`**

Install all required packages from your `pyproject.toml` or `requirements.txt` file.

```bash
uv pip install -r requirements.txt

```

### 4. **Set up your API Key**

Create a `.env` file in the root of the project and add your Gemini API key:


---

## Usage

To run the main application, execute the `main.py` script from your terminal:

```bash
uv run main.py "<YOUR PROMPT>"
