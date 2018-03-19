from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pytest
import pandas as pd
import ray.concat as rc
from ray.dataframe.utils import (
    to_pandas,
    from_pandas
)


@pytest.fixture
def ray_df_equals_pandas(ray_df, pandas_df):
    return to_pandas(ray_df).sort_index().equals(pandas_df.sort_index())


@pytest.fixture
def ray_df_equals(ray_df1, ray_df2):
    return to_pandas(ray_df1).sort_index().equals(
        to_pandas(ray_df2).sort_index()
    )


@pytest.fixture
def generate_dfs():
    df = pd.DataFrame({'col1': [0, 1, 2, 3],
                       'col2': [4, 5, 6, 7],
                       'col3': [8, 9, 10, 11],
                       'col4': [12, 13, 14, 15],
                       'col5': [0, 0, 0, 0]})

    df2 = pd.DataFrame({'col1': [0, 1, 2, 3],
                        'col2': [4, 5, 6, 7],
                        'col3': [8, 9, 10, 11],
                        'col6': [12, 13, 14, 15],
                        'col7': [0, 0, 0, 0]})
    return df, df2


@pytest.fixture
def test_df_concat():
    df, df2 = generate_dfs()

    assert(pd.concat([df, df2]) == rc.concat([df, df2]))


def test_ray_concat():
    df, df2 = generate_dfs()
    ray_df, ray_df2 = from_pandas(df, 2), from_pandas(df2, 2)

    assert(pd.concat([df, df2]) == rc.concat([ray_df, ray_df2]))


def test_mixed_concat():
    df, df2 = generate_dfs()
    df3 = df.copy()

    mixed_dfs = [from_pandas(df, 2), from_pandas(df2, 2), df3]

    assert(pd.concat([df, df2, df3]) == rc.concat(mixed_dfs))


def test_mixed_inner_concat():
    df, df2 = generate_dfs()
    df3 = df.copy()

    mixed_dfs = [from_pandas(df, 2), from_pandas(df2, 2), df3]

    assert(pd.concat([df, df2, df3], join="inner") ==
           rc.concat(mixed_dfs, join="inner"))
