# Python Package Exercise
[![Build Status](https://github.com/software-students-spring2025/3-python-package-gmjm/actions/workflows/build.yaml/badge.svg)](https://github.com/software-students-spring2025/3-python-package-gmjm/actions)

## Plain-language Description 

- PyRiddles is a fun and interactive python package for those who want to enjoy a few riddles! With a range of difficulty levels and hints to help you along the way, PyRiddles is perfect for anyone looking to exercise their brain and have a good time. Whether you're a seasoned puzzle solver or just looking for a fun way to pass the time, PyRiddles is the perfect package for you.

## [Link to Package on PyPi Website](https://pypi.org/project/pyriddles/0.0.2/)

## How to Import

1. Run the following command in terminal:
   ```bash
   pip install pyriddles
   ```
2. Confirm proper installation:
   ```bash
   pip show pyriddles
   ```
3. Next, import the desired functions (example usage below):
   ```python
   from pyriddles import arbitrary_riddle, get_answer, ...
   ```

## Example Usage of Key Functions:

- `arbitrary_riddle`: 
  - Parameters:
    - None 
  - Returns:
    - A random riddle_id to be used in other methods
  - Example: 
    - ```python
      # Demonstrate arbitrary_riddle
      riddle_id = arbitrary_riddle()
      print(f"Random riddle ID: {riddle_id}")
      ```

- `get_riddle_by_difficulty`: 
  - Parameters:
    - A difficulty (of 'easy', 'medium', or 'hard')
  - Returns:
    - A random riddle based on difficulty
  -  Example:
     -  ```python
        # Demonstrate proper usage of get_riddle_by_difficulty
        print(get_riddle_by_difficulty("easy"))

        # Demonstrate improper usage of get_riddle_by_difficulty
        print(get_riddle_by_difficulty("extra hard"))
        ```
- `list_difficulties`:
  - Parameters:
    - None
  - Returns:
    - A list of available difficulties
  - Example:
    - ```python
      #Demonstrate list_difficulties
      print(list_difficulties())
      ```


- `get_answer`: 
  - Parameters:
    - riddle_id : The id number for a riddle in `config.py`
  - Returns:
    - A boolean value depending on the verity of the user's answer
  - Example:
    - ```python
      #Demonstrate get_answer
      answer = get_answer(riddle_id)
      print(f"The answer to riddle {riddle_id} is: {answer}")
      ```


- `get_hint`:
  - Parameters:
    - riddle_id
    - hint_type (set to auto normally)
    - max_attempts : the maximum number of tries for a riddle
  - Returns: A singular (usually random) hint
  - Example:
    - ```python
      #Example usage of get_hint

      hint = get_hint(riddle_id, "soundsalad_hint")
      print("Generated hint (soundsalad_hint):", hint)

      hint_auto = get_hint(riddle_id, "auto")
      print("Generated hint (auto):", hint_auto)
      ```

- `get_hints`:
  - Parameters: 
    - riddle_id
    - hint_type : Usually randomly selected, but can be input manually for a specific type
    - limit : The total number of hints desired
  - Returns: 
    - Several hints
  - Example:
    ```python
    #Example usage of get_hints

    hints_list = get_hints(riddle_id, "auto", limit=5)
    print("Generated list of hints (auto):", hints_list)
    ```

- NOTE: For a program that uses all key functions, go [here](https://github.com/software-students-spring2025/3-python-package-gmjm/blob/main/pyriddles/example_usage.py)

## Team Members

- [Kahmeeah Obey](https://github.com/kahmeeah)
- [Gabriella Codrington](https://github.com/gabriella-codrington)
- [Jahleel Townsend](https://github.com/JahleelT)
- [Matthew Ortega](https://github.com/bruhcolate)

## For Developers

These instructions will guide you on how to configure and run this project.

### **Prerequisites**

Before you begin, ensure you have the following installed:

- **Python 3.9** or higher
- **pipenv** (for dependency and virtual environment management)

If you don’t have `pipenv`, install it with:

```sh
pip install pipenv
```

---

### **Setting Up the Development Environment**

1. Clone the repository

    ```sh
    git clone https://github.com/software-students-spring2025/3-python-package-gmjm.git
    cd 3-python-package-gmjm
    ```

2. Set up the virtual environment and install dependencies

    ```sh
    pipenv install
    ```

3. Activate the virtual environment:

    ```sh
    pipenv shell
    ```

---

### **Running the Package Locally**

To execute the package code locally, use:

```sh
python -m pyriddles
```

---

### **Running Tests**

To ensure that all functions work correctly, you can run the tests manually using:

```sh
pytest
```

---

### **Building the Package**

To manually build the package into distributable artifacts:

```sh
python -m build
```

---

### Importing the Package
To import the entire package for use in your code, add the following line to the top of your file

    import pyriddles

If you only want to import certain functions, add the following line to the top of your file:

    from pyriddles import func1, func2...

---

### Code Examples
For more information on how the functuons in this package should work, see this [code file](pyriddles\use_difficulty.py).

---

### **CI/CD with GitHub Actions**

Every time a pull request is created, GitHub Actions will:

- Run the test suite
- Build the package
- Ensure compatibility with multiple Python versions

You can check the latest test/build status via the badge at the top of this README.
