
## Environment

Please set up your Python version to `3.10`

- `
python3 --version
`

Create your `.env` file.

- `cd <project-directory>`
```bash
    $ touch .env
```
```bash
    $ EMAIL=<your_mail_adress@mail.com>
    $ PASSWORD=<your_password>
```

## Setting Development Environment
- Create virtual environment
```bash
    $ python -m venv <venv-name>
```
- Activate the virtual environment
```bash
    $ source <venv-name>/bin/activate
```
- Install libraries
```bash
    $ pip install -r requirements.txt
```