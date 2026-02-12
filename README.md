# CART498-A4

Minimal Flask app that calls the OpenAI API for:

- text generation (`chat.completions.create`)
- image generation (`images.generate`)

## Entry Point

The app entry point is `app.py`.

Running `python app.py` starts the Flask development server on `http://127.0.0.1:5000`.

## Project Structure

- `app.py`: Flask app, routes, and OpenAI API calls.
- `templates/index.html`: Main page template.
- `static/style.css`: App styling.
- `static/JungBG.mp4`: Background media.

## Prerequisites

- Python 3.10+
- An OpenAI API key

## Setup

1. Create a virtual environment:

```bash
python -m venv venv
```

2. Activate it:

Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install flask openai python-dotenv
```

4. Create a `.env` file in the project root with:

```env
OPENAI_API_KEY=your_api_key_here
```

## Run the App

From the project root:

```bash
python app.py
```

Then open `http://127.0.0.1:5000` in your browser.

## Tests

There are currently no automated tests in this repository.

If you add tests (recommended), use `pytest`:

1. Install:

```bash
pip install pytest
```

2. Add a test file, for example `tests/test_app.py`.

3. Run:

```bash
pytest
on3 app.py
py app.py
```
