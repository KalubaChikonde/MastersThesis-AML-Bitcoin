import pandas as pd


def import_elliptic_data_from_csvs():
    df_classes = pd.read_csv("/Users/kalubachikonde/Documents/thesisProject/data/elliptic_txs_classes.csv")
    df_edgelist = pd.read_csv('/Users/kalubachikonde/Documents/thesisProject/data/elliptic_txs_edgelist.csv')
    df_features = pd.read_csv('/Users/kalubachikonde/Documents/thesisProject/data/elliptic_txs_features.csv', header=None)
    return df_classes, df_edgelist, df_features


df_classes, df_edgelist, df_features = import_elliptic_data_from_csvs()

print(df_classes.head())
print(df_edgelist.head())