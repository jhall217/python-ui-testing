# Python + Selenium / Page Object Model

This project demonstrates how to use Python and Selenium with the Page Object Model (POM) design pattern. The Page Object Model helps in reducing code duplication and improving code maintainability, especially when working with multiple web pages in automated tests.

## Project Structure

### pages/base

This directory contains base classes that provide common functionalities to be used or overridden by specific search engine pages.

- **base_page.py**: Contains basic functions that are common to all pages.
- **base_search.py**: Contains default search functions that can be customized by specific search engine pages.

### pages/duckduckgo

This directory contains the page object classes that are specific to the DuckDuckGo search engine.

### pages/google

This directory contains the page object classes that are specific to the Google search engine.

## Installation

To get started with this project, you need to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

Ensure you have `selenium`, `pytest`, and other dependencies specified in the `requirements.txt` file installed.

## Running Tests

You can run the tests using `pytest`, this also supports parallel testing. Navigate to the root directory of the project and execute:

```bash
pytest
```

To execute tests in parallel include the `-n {tests}` as an argument
```bash
pytest -n 2
```


## Contributing

If you would like to contribute to this project, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.