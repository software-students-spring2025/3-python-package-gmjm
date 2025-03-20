# Python Package Exercise

Replace the contents of the [README.md](./README.md) file with a beautifully-formatted Markdown file including

- a plain-language **description** of your project, including:
- a [badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge) at the top of the `README.md` file showing the result of the latest build/test workflow run.
- a link to your package's page on the PyPI website.
- how a developer who wants to import your project into their own code can do so - include documentation and code examples for all functions in your package and a link to an example Python program that uses each of them.
- how a developer who wants to contribute to your project can set up the virtual environment, install dependencies, and build and test your package for themselves.
- the names of all teammates as links to their GitHub profiles in the `README.md` file.
- instructions for how to configure and run all parts of your project for any developer on any platform - these instructions must work!
- instructions for how to set up any environment variables and import any starter data into the database, as necessary, for the system to operate correctly when run.
- if there are any "secret" configuration files, such as `.env` or similar files, that are not included in the version control repository, examples of these files, such as `env.example`, with dummy data must be included in the repository and exact instructions for how to create the proper configuration files and what their contents should be must be supplied to the course admins by the due date.


## Plain-language Description 

- PyRiddles is a simple and fun python package for those who want to enjoy a few riddles! Users of the package would make use of it by accessing four main functions of 

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
