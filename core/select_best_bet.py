def calculate_true_spread(row):
    if row['draw_option']:
        if row['odds_a'] and row['odds_b']:
            fav = min(row['odds_a'], row['odds_b'])
            dog = max(row['odds_a'], row['odds_b'])
            return (dog - fav) / 3 if fav >= 1.53 else None
    else:
        if row['odds_a'] and row['odds_b']:
            fav = min(row['odds_a'], row['odds_b'])
            dog = max(row['odds_a'], row['odds_b'])
            return (dog - fav) if fav >= 1.44 else None
    return None

def select_best_bet(df):
    df['true_spread'] = df.apply(calculate_true_spread, axis=1)
    df.dropna(subset=['true_spread'], inplace=True)
    return df.loc[df['true_spread'].idxmax()] if not df.empty else None
