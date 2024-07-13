import json

import pandas as pd
import bar_chart_race as bcr


def main():
    with open('results.json', 'r') as f:
        data = json.loads(f.read())
    results = {}
    for team_name, stage in data.items():
        ds = stage['ds']
        points = stage['scores']
        key = f"{team_name} ({ds})"
        results[key] = points
    df = pd.DataFrame(results)
    print(df)
    df = df.cumsum()
    print(df)
    bcr.bar_chart_race(df=df, filename='dvelo.mp4', orientation='h', sort='desc', period_length=3000, steps_per_period=25)


if __name__ == '__main__':
    main()
