import pandas as pd


def load_bit_data(file_path):
    df = pd.read_csv(file_path, index_col=False, on_bad_lines='skip', skipfooter=5, engine='python')
    df.columns = [col.strip() for col in df.columns]
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    # amount to number
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')

    return df


def main():
    df = load_bit_data('bit_transactions_2025.csv')

    my_name = "אור אלקובי"
    received_payments = df[(df['Status'] == 'Done') & (df['Credit/Debit'] == 'Credit') & (df['From/To'] != my_name)]

    payers_ranking = received_payments.groupby('From/To')['Amount'].sum().sort_values(ascending=False)

    top_payer = payers_ranking.index[0]
    total_amount = payers_ranking.iloc[0]

    print(f"The top payer for 2025 is{top_payer}, with a total of {total_amount}NIS")


if __name__ == '__main__':
    main()
