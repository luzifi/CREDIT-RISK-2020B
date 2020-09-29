# Getting Started

This is a simple homework used to test your git & github configuration.

## Instructions

Follow these steps:

1. Configure your repository using the videos on CANVAS.
2. Update your master branch!
3. Create a branch for this homework named: `HW-GETTING-STARTED`
4. Create a `main.py` file with the content on the **CODE: main.py** section.
    * Replace the `MY_STUDENT_ID` variable with your info.
4. Create a `__main__.py` file with the content on the **CODE: __main\__.py** section.
5. Add, Commit & Push your changes into the `HW-GETTING-STARTED` branch.
6. Create a PR from the `HW-GETTING-STARTED` branch into the `SOLUTIONS` branch.

## Execution

Activate your virtualenv on the base of the `CREDIT-RISK-2020B`:
* Windows: `source venv/Scripts/activate`
* Mac / Linux: `source venv/bin/activate`

Change into the `homework` directory:

```commandline
$ cd src/homework
```

Execute the python application:

```commandline
$ python -m getting-started hello
```

## Code: main.py

```python

MY_STUDENT_ID = ""


class Hello:

    @staticmethod
    def hello():
        return f"This is a greeting message from {MY_STUDENT_ID}."

```

## Code: __main\__.py

```python
import fire

from .main import Hello


if __name__ == "__main__":
    fire.Fire(Hello)

```

