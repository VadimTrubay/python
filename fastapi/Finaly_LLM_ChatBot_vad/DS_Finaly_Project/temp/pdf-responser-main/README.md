# pdf-responser
Study project. Application Large Language Model for PDF documents.

[![MIT License](https://img.shields.io/badge/license-MIT-green)](https://github.com/DenysTantsiura/pdf-responser/blob/main/LICENSE.md)
![Version](https://img.shields.io/badge/version-v0.1.0-green)
--

....

## Prerequisites
Before you begin, ensure that you have the following prerequisites installed on your system:

- Python 3.10 or higher
- Poetry

## Installation
1. Clone the project repository:
```
git clone <repository_url>
```

2. Navigate to the project directory:
```
cd <project_directory>
```
3. Install the project dependencies using Poetry:
```
poetry install
```
Poetry will create a virtual environment and install the required packages specified in the pyproject.toml file.

## Launching
To launch the development server and start the FastAPI project, follow these steps:

1. Activate the project's virtual environment:
```
poetry shell
```
2. Run the following command to start the development server:
```
uvicorn main:app --reload
```
- ```main``` refers to the name of the main file where your FastAPI app instance is created.
- ```--reload``` enables auto-reloading of the server whenever code changes are detected (useful during development).
3. Once the server has started, you should see output similar to the following:

```
INFO: Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
```
Open your web browser and navigate to http://0.0.0.0:8000 to access the API.

4. Swager documentation could be found here: http://0.0.0.0:8000/docs
...
```See The End of main.py```

## Application features

...


### Used technologies
- Python (programming language)
- FastAPI (web framework)
- Uvicorn (ASGI server)
......


### Developers - Fast Rabbit Team
- [Andrii Kylymnyk](https://github.com/theneonwhale)
- [Anton Holovin](https://github.com/Unfeir)
- [Denys Tantsiura](https://github.com/DenysTantsiura)

#### License
This project is licensed under the MIT License.

