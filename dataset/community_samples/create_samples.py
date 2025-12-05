import pandas as pd
import os

communities = ['fm', 'mlb', 'pp']
topics = ['정권 교체', '통합 정치', '단일화(윤석열-안철수)',
          '부동산, 세금 등 경제문제', '여성가족부 폐지',
          '후보(또는 가족)의 비리', '대장동 의혹']

for community in communities:
    all_data = []
    for topic in topics:
        filepath = f'../original/{community}_{topic}.csv'
        if os.path.exists(filepath):
            df = pd.read_excel(filepath)
            all_data.append(df)
            print(f"Loaded {filepath}: {len(df)} rows")

    if all_data:
        combined = pd.concat(all_data, ignore_index=True)
        print(f"\nCombined {community} data: {len(combined)} total rows")

        sample_size = min(50000, len(combined))
        sampled = combined.sample(n=sample_size, random_state=42)

        output_path = f'{community}_sample_50000.csv'
        sampled.to_csv(output_path, index=False, encoding='utf-8-sig')

        print(f"Created {output_path} with {len(sampled)} rows\n")
    else:
        print(f"No data found for {community}\n")
