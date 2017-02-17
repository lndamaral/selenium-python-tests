### Setup

> This is an automation architecture for python language and before using it you need to install some modules and follow some steps.

1. Cloning the repository:

    ```shell
    git clone https://github.com/lndamaral/selenium_python_tests.git
    ```

2. Installing all the dependencies:

    ```shell
    cd path/to/selenium_python_tests

    pip install -r requirements.txt
    ```

3. Installing Chrome Driver:

    ```shell
    wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_mac64.zip -P ~/Downloads
    unzip ~/Downloads/chromedriver_mac64.zip -d ~/Downloads
    chmod +x ~/Downloads/chromedriver
    sudo mv -f ~/Downloads/chromedriver /usr/local/share/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
    sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
    ```