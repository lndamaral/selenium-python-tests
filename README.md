## Selenium Python Tests

### Setup

This is a automation framework for python language and before using it you need to install some modules.

 1. Cloning the repository:

    ```shell
    git clone https://github.com/lndamaral/selenium_python_tests.git
    ```

2. Installing all the dependencies:

    ```shell
    cd path/to/selenium_python_tests

    pip install -r requirements.txt
    ```

### Python Naming Conventions

    http://visualgit.readthedocs.io/en/latest/pages/naming_convention.html

### Architecture

    /framework:

        base/
            basepageelement.py          #Super class to our actual Page Objects and get all the asserts that come with a TestCase
            basepageobject.py           #Consists of useful wrappers for common Selenium operations

        factory/
            driverfactory.py            #Used to generate de WebDriver driver.
            pagefactory.py              #Used to manage page objects.

        page/                           #Folder where classes that implement Pages mapping according to PageObjects.
            ...page.py
            ...page.py
            ...page.py

        report/                         #Folder where log files are created after each execution.
            log/
            htmltestrunner.py

        step/                           #Folder where classes that implement Steps according to PageObjects.
            ...step.py
            ...step.py
            ...step.py

        tests/                              #Folder where test suites and test cases will be kept.
            ...test.py
            ...test.py
            ...test.py

        runner.py                       #File that references all test suites and testcases. This is our "main" file.
