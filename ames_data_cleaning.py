import click
import pandas as pd


@click.command()
@click.option(
    "--file-path",
    required=True,
    type=click.Path(exists=True),
    help="Path to Ames housing data file. File will be cleaned and overwritten.",
)
def clean_ames_data(file_path: str) -> None:
    df = pd.read_parquet(file_path)

    df.columns = [col.replace(".", "") for col in df.columns]

    df = df.drop(["Order", "PID"], axis="columns")
    df = df.loc[~df["Neighborhood"].isin(["GrnHill", "Landmrk"])]
    df = df.loc[df["GrLivArea"] <= 4000]

    replace_all_missing_values(df)
    df = encode_categorical_columns(df)

    df.to_parquet(file_path)


def replace_all_missing_values(df: pd.DataFrame) -> None:
    replace_na(df, "Alley", "None")
    replace_na(df, "BedroomAbvGr", 0)

    basement_cols = [
        "BsmtQual",
        "BsmtCond",
        "BsmtExposure",
        "BsmtFinType1",
        "BsmtFinType2",
    ]
    for col in basement_cols:
        replace_na(df, col, "No")

    numeric_zero_cols = [
        "BsmtFullBath",
        "BsmtHalfBath",
        "BsmtUnfSF",
        "GarageArea",
        "GarageCars",
        "HalfBath",
        "KitchenAbvGr",
        "LotFrontage",
        "MasVnrArea",
        "MiscVal",
        "OpenPorchSF",
        "PoolArea",
        "ScreenPorch",
        "TotRmsAbvGrd",
        "WoodDeckSF",
        "EnclosedPorch",
        "Fireplaces",
    ]
    for col in numeric_zero_cols:
        replace_na(df, col, 0)

    categorical_defaults = {
        "Condition1": "Norm",
        "Condition2": "Norm",
        "ExterCond": "TA",
        "ExterQual": "TA",
        "Fence": "No",
        "Functional": "Typ",
        "GarageType": "No",
        "GarageFinish": "No",
        "GarageQual": "No",
        "GarageCond": "No",
        "HeatingQC": "TA",
        "KitchenQual": "TA",
        "LotShape": "Reg",
        "MasVnrType": "None",
        "MiscFeature": "No",
        "PavedDrive": "N",
        "PoolQC": "No",
        "SaleCondition": "Normal",
        "Utilities": "AllPub",
        "CentralAir": "N",
        "FireplaceQu": "No",
        "Electrical": "SBrkr",
    }

    for col, value in categorical_defaults.items():
        replace_na(df, col, value)


def replace_na(df: pd.DataFrame, col: str, value) -> None:
    df[col] = df[col].fillna(value)


def encode_categorical_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.replace(
        {
            "MSSubClass": {
                20: "SC20",
                30: "SC30",
                40: "SC40",
                45: "SC45",
                50: "SC50",
                60: "SC60",
                70: "SC70",
                75: "SC75",
                80: "SC80",
                85: "SC85",
                90: "SC90",
                120: "SC120",
                150: "SC150",
                160: "SC160",
                180: "SC180",
                190: "SC190",
            },
            "MoSold": {
                1: "Jan",
                2: "Feb",
                3: "Mar",
                4: "Apr",
                5: "May",
                6: "Jun",
                7: "Jul",
                8: "Aug",
                9: "Sep",
                10: "Oct",
                11: "Nov",
                12: "Dec",
            },
        }
    )

    df = df.replace(
        {
            "Alley": {"None": 0, "Grvl": 1, "Pave": 2},
            "BsmtCond": {"No": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
            "BsmtExposure": {"No": 0, "Mn": 1, "Av": 2, "Gd": 3},
            "BsmtFinType1": {
                "No": 0,
                "Unf": 1,
                "LwQ": 2,
                "Rec": 3,
                "BLQ": 4,
                "ALQ": 5,
                "GLQ": 6,
            },
            "BsmtFinType2": {
                "No": 0,
                "Unf": 1,
                "LwQ": 2,
                "Rec": 3,
                "BLQ": 4,
                "ALQ": 5,
                "GLQ": 6,
            },
            "BsmtQual": {"No": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
            "ExterCond": {"Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
            "ExterQual": {"Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
            "FireplaceQu": {"No": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
            "Functional": {
                "Sal": 1,
                "Sev": 2,
                "Maj2": 3,
                "Maj1": 4,
                "Mod": 5,
                "Min2": 6,
                "Min1": 7,
                "Typ": 8,
            },
            "GarageCond": {"No": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
            "GarageQual": {"No": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
            "HeatingQC": {"Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
            "KitchenQual": {"Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5},
            "LandSlope": {"Sev": 1, "Mod": 2, "Gtl": 3},
            "LotShape": {"IR3": 1, "IR2": 2, "IR1": 3, "Reg": 4},
            "PavedDrive": {"N": 0, "P": 1, "Y": 2},
            "PoolQC": {"No": 0, "Fa": 1, "TA": 2, "Gd": 3, "Ex": 4},
            "Street": {"Grvl": 1, "Pave": 2},
            "Utilities": {"ELO": 1, "NoSeWa": 2, "NoSewr": 3, "AllPub": 4},
        }
    )

    return df


if __name__ == "__main__":
    clean_ames_data()
