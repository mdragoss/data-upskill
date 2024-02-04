# Generate dummy data

> This project aims to up personal skills and personal knowledge about databases, recommendation engine using Python and SQL Server. It will leverage personal skills and abilities, this project was internally only and GitHub was as a platform for sharing general things, on repository is used general data and information, other requirements and task was executed in Azure Data Studio using Sql Scripting.

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

To help maintain a good quality exists precommit command runs some linting and other stuff.


Dependency for Linux is [odbc driver install from microsoft](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=alpine18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline).

> For Arch can be found on Aur.

---
**NOTE**

If you use in your tables `text` and `ntext` turn **off**
`.fast_executemany = False`.

---
