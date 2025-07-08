import requests
import pandas as pd
from betting_config import ODDS_API_KEY, SPORTS, REGION, MARKET

def fetch_odds(sport):
    url = f'https://api.the-odds-api.com/v4/sports/{sport}/odds/?regions={REGION}&markets={MARKET}&apiKey={ODDS_API_KEY}'
    response = requests.get(url)
    return response.json() if response.status_code == 200 else []

def parse_odds(data, draw_option):
    rows = []
    for match in data:
        teams = match['teams']
        outcomes = match['bookmakers'][0]['markets'][0]['outcomes']
        odds = {o['name']: o['price'] for o in outcomes}
        rows.append({
            'match_id': match['id'],
            'date': match['commence_time'],
            'sport': match['sport_key'],
            'team_a': teams[0],
            'team_b': teams[1],
            'draw_option': draw_option,
            'odds_a': odds.get(teams[0]),
            'odds_b': odds.get(teams[1]),
            'odds_draw': odds.get('Draw')
        })
    return pd.DataFrame(rows)

def get_combined_odds():
    all_data = []
    for sport in SPORTS:
        data = fetch_odds(sport)
        draw_option = 'soccer' in sport
        df = parse_odds(data, draw_option)
        all_data.append(df)
    return pd.concat(all_data, ignore_index=True)
