"""Pricing Matrix API"""
from io import StringIO
import pandas as pd
import requests

from flask import Flask, Response, request, Blueprint
from bs4 import BeautifulSoup

from constants import AtlasSheets, HANGGROUP_URL

api = Blueprint('api', __name__, url_prefix='/api')

def new_phone_data() -> None:
    """Return pricing for new phones"""
    response = requests.get(HANGGROUP_URL)
    soup = BeautifulSoup(response.content, features='lxml')
    
    for item in soup.find_all('table'):
        df = pd.read_xml(StringIO(str(item)))
        print(df)
        input('continue')
    return

def used_phone_data() -> pd.DataFrame:
    """Return a dataframe with what we need about used phones"""
    used_phone_url = AtlasSheets.IPHONE_USED.csv_url
    df = pd.read_csv(used_phone_url)

    df['model_name'] = df.iloc[:, 1].astype(str)
    df['model_name'] = df['model_name'].str.lower().str.strip()

    df = df[df['model_name'].str.startswith('iphone')]

    grades = ['swap', 'a', 'b', 'c', 'd', 'doa']
    rename_pattern = {f'Unnamed: {x}': y for x, y in zip(range(2, 8), grades)}
    df = df.rename(columns=rename_pattern)

    df = df.loc[:, ~df.columns.str.startswith('Unnamed')]
    return df


@api.route('/iphone-used/<model>')
def iphone_used(model: str) -> Response:
    """Returns used phone prices"""
    data = used_phone_data()

    is_unlocked = request.args.get("unlocked", False)
    grade = request.args.get('grade', "b")
    storage = request.args.get('storage', '256gb')

    unlocked = 'unlocked' if is_unlocked else 'carrier locked'
    model = f"{model.lower()} {storage} {unlocked}"

    try:
        result = data.loc[data['model_name'] == model, grade]
    except KeyError:
        response = f"Invalid Grade \
                     available grades are: {", ".join(list(data.columns))}"
        return Response(status=500, response=response)

    if len(result) == 1:
        return Response(status=200, response=result.iloc[0])
    return Response(
        status=422,
        response=f"Got {len(result)} results for {model} with grade {grade}"
        )


app = Flask(__name__)
app.register_blueprint(api)

if __name__ == "__main__":
    new_phone_data()
