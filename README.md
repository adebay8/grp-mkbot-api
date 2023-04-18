
# Centre:MK Robot GraphQL API

This is a GraphQL-based backend API for the Centre:MK robot user interface.

## Installation

Install my-project with npm

Clone this repository: 

```bash
    git clone https://github.com/adeby8/grp-mkbot-api.git
```

Navigate to the project directory: 
```
    cd grp-mkbot-api
```

Create a virtual environment: 
```
    python -m venv venv
```
Activate the virtual environment:

On Windows: 
```
    venv\Scripts\activate
```
On Unix or Linux: 
```
    source venv/bin/activate
```

Install the dependencies: 
```
    pip install -r requirements.txt
```

Create the database: 
```
    python manage.py migrate
```
Start the development server: 
```
    python manage.py runserver
```
## Usage/Examples

The API is currently deployed live [here](https://mkbot-api.onrender.com/graphql)

## License

This project is licensed under the MIT License. See the [MIT](https://choosealicense.com/licenses/mit/) license for details

