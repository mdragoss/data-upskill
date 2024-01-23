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
