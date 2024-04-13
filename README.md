# Overview

## Installation

### Requirements:

- Set up a virtual environment:
  ```bash
  python -m venv ./venv
  source .venv/bin/activate
  ```

- Install the necessary dependencies:
  ```bash
  pip install -r requirements.txt
  ```

- Run the API:
  ```bash
  python api.py
  ```

## Example

Flask will run on http://127.0.0.1:5000/.

- To get a list of months:
  ```bash
  curl 127.0.0.1:5000/
    months = [
        {"id": 1, "name": "January"},
        {"id": 2, "name": "February"},
        {"id": 3, "name": "March"},
        {"id": 4, "name": "April"},
        {"id": 5, "name": "May"},
        {"id": 6, "name": "June"},
        {"id": 7, "name": "July"},
        {"id": 8, "name": "August"},
        {"id": 9, "name": "September"},
        {"id": 10, "name": "October"},
        {"id": 11, "name": "November"},
        {"id": 12, "name": "December"},
    ]
  ```


- Months will also accept a POST message:
  ```bash
  curl -X POST 127.0.0.1:5000/
  {"success":true}
  ```

