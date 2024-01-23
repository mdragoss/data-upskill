# Generate dummy data

1. Create virtual env `python3 -m venv .venv` and activate it
2. Install pipenv `pip3 install pipenv` then install project dependencies `pipenv install --dev`
3. Copy `.env.example` into `.env` update variables accordingly
4. Run commands with pipenv (pipenv **loads .env** file this will work as expected `os.getenv()` will return  valid env variable)

Then use it for your up skill tables, generate and print custom data:

```sh
pipenv run script-name # to list all scripts write in terminal pipenv scripts
```
> If you don't want to use pipenv export variables with `.bashrc` | `.zshrc`.

## Development
Before push code into repo use `pipenv run init`.

Some commands runs on pre-commit, to help maintain a good quality.


Dependency for Linux is [odbc driver install from microsoft](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=alpine18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline).

> For Arch can be found on Aur.
