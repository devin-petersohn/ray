import pandas as pd
import numpy as np
import ray

ray.register_custom_serializer(pd.DataFrame, use_pickle=True)
ray.register_custom_serializer(pd.core.indexes.base.Index, use_pickle=True)

class DataFrame:
    def __init__(self, df, columns):
        """
        Distributed DataFrame object backed by Pandas dataframes.

        Args:
            df ([ObjectID]): The list of ObjectIDs that contain the dataframe
                partitions.
            columns ([str]): The list of column names for this dataframe.
        """
        assert(len(df) > 0)

        self.df = df
        self.columns = columns

    def __str__(self):
        return str(pd.concat(ray.get(self.df)))

    def __repr__(self):
        return str(pd.concat(ray.get(self.df)))

    @property
    def index(self):
        """
        Get the index for this DataFrame.

        Returns:
            The union of all indexes across the partitions.
        """
        indices = ray.get(self.map_partitions(lambda df: df.index).df)
        return indices[0].append(indices[1:])

    @property
    def size(self):
        """
        Get the number of elements in the DataFrame.

        Returns:
            The number of elements in the DataFrame.
        """
        sizes = ray.get(self.map_partitions(lambda df: df.size).df)
        return sum(sizes)

    @property
    def ndim(self):
        """
        Get the number of dimensions for this DataFrame.

        Returns:
            The number of dimensions for this DataFrame.
        """
        # The number of dimensions is common across all partitions.
        # The first partition will be enough.
        return ray.get(_deploy_func.remote(lambda df: df.ndim, self.df[0]))

    @property
    def ftypes(self):
        """
        Get the ftypes for this DataFrame.

        Returns:
            The ftypes for this DataFrame.
        """
        # The ftypes are common across all partitions.
        # The first partition will be enough.
        return ray.get(_deploy_func.remote(lambda df: df.ftypes, self.df[0]))

    @property
    def dtypes(self):
        """
        Get the dtypes for this DataFrame.

        Returns:
            The dtypes for this DataFrame.
        """
        # The dtypes are common across all partitions.
        # The first partition will be enough.
        return ray.get(_deploy_func.remote(lambda df: df.dtypes, self.df[0]))

    @property
    def empty(self):
        """
        Determines if the DataFrame is empty.

        Returns:
            True if the DataFrame is empty.
            False otherwise.
        """
        return False not in ray.get(self.map_partitions(lambda df: df.empty).df)

    @property
    def values(self):
        """
        Create a numpy array with the values from this DataFrame.

        Returns:
            The numpy representation of this DataFrame.
        """
        return np.concatenate(
            ray.get(self.map_partitions(lambda df: df.values).df))

    @property
    def axes(self):
        """
        Get the axes for the DataFrame.

        Returns:
            The axes for the DataFrame.
        """
        return [self.index, self.columns]

    @property
    def shape(self):
        """
        Get the size of each of the dimensions in the DataFrame.

        Returns:
            A tuple with the size of each dimension as they appear in axes().
        """
        return (len(self.index), len(self.columns))

    def map_partitions(self, func, *args):
        """
        Apply a function on each partition.

        Args:
            func (callable): The function to Apply.

        Returns:
            A new DataFrame containing the result of the function.
        """
        assert(callable(func))
        new_df = [_deploy_func.remote(func, partition) for partition in self.df]
        
        return DataFrame(new_df, self.columns)

    def add_prefix(self, prefix):
        """
        Add a prefix to each of the column names.

        Returns:
            A new DataFrame containing the new column names.
        """
        new_dfs = self.map_partitions(lambda df: df.add_prefix(prefix))
        new_cols = columns.map(lambda x: str(prefix) + str(x))
        return DataFrame(new_dfs, new_cols)

    def add_suffix(self, suffix):
        """
        Add a suffix to each of the column names.

        Returns:
            A new DataFrame containing the new column names.
        """
        new_dfs = self.map_partitions(lambda df: df.add_suffix(suffix))
        new_cols = columns.map(lambda x: str(x) + str(suffix))
        return DataFrame(new_dfs, new_cols)

    def applymap(self, func):
        """
        Apply a function to a DataFrame elementwise.

        Args:
            func (callable): The function to apply.
        """
        assert(callable(func))
        return self.map_partitions(lambda df: df.applymap(lambda x: func(x)))

    def copy(self):
        """
        Creates a shallow copy of the DataFrame.

        Returns:
            A new DataFrame pointing to the same partitions as this one.
        """
        return DataFrame(self.df, self.columns)

    def groupby(self, by=None, axis=0, level=None, as_index=True, group_keys=True, squeeze=False):
        """
        Apply a groupby to this DataFrame. See _groupby() remote task.

        Args:
            by
            axis
            level
            as_index
            group_keys
            squeeze

        Returns:
            A new DataFrame resulting from the groupby.
        """
        return DataFrame(ray.get(_groupby.remote(self)), self.columns)

    def reduce_by_index(self, func):
        """
        Perform a reduction based on the row index and perform a predicate on
        the result.

        Args:
            func (callable): The function to call on the partition
                after the reduction.

        Returns:
            A new DataFrame with the result of the reduction.
        """
        return DataFrame(ray.get(_reduce_by_index.remote(self, func)), self.columns)

    def sum(self, axis=None, skipna=True):
        """
        Perform a sum across the DataFrame.

        Args:
            axis ()
            skipna ()

        Returns:
            The sum of the DataFrame.
        """
        return self.map_partitions(lambda df: df.sum(axis=axis, skipna=skipna)
            ).reduce_by_index(lambda df: df.sum(axis=axis, skipna=skipna))

    def abs(self):
        """
        Apply an absolute value function to all numberic columns.

        Returns:
            A new DataFrame with the applied absolute value.
        """
        return self.map_partitions(lambda df: df.abs())

    def isin(self, values):
        """
        Create a DataFrame filled with booleans representing whether or not the
        cell is contained in values.

        Args:
            values (iterable, DataFrame, Series, or dict): The values to find.

        Returns:
            A new DataFrame with booleans representing whether or not a cell is in values.
            True: cell is contained in values.
            False: otherwise
        """
        return self.map_partitions(lambda df: df.isin(values))

    def isna(self):
        """
        Create a DataFrame filled with booleans representing whether or not the
        cell contains NA.

        Returns:
            A new DataFrame with booleans representing whether or not a cell is NA.
            True: cell contains NA.
            False: otherwise.
        """
        return self.map_partitions(lambda df: df.isna())

    def isnull(self):
        """
        Create a DataFrame filled with booleans representing whether or not the
        cell contains a null value.

        Returns:
            A new DataFrame with booleans representing whether or not a cell
                is null.
            True: cell contains null.
            False: otherwise.
        """
        return self.map_partitions(lambda df: df.isnull)

    def keys(self):
        """
        Get the info axis for the DataFrame.

        Returns:
            A pandas Index for this DataFrame.
        """
        # Each partition should have the same index, so we'll use 0's
        return ray.get(_deploy_func.remote(lambda df: df.keys(), self.df[0]))

    def transpose(self, *args, **kwargs):
        """
        Transpose columns and rows for the DataFrame. Triggers a shuffle.

        Returns:
            A new DataFrame transposed from this DataFrame.
        """
        return self.map_partitions(lambda df: df.transpose(*args, **kwargs)
            ).reduce_by_index(lambda df: df.sum())

    T = property(transpose)

    def dropna(self, axis, how, thresh=None, subset=[], inplace=False):
        """
        Create a new DataFrame from the removed NA values from this one.

        Args:
            axis (int, tuple, or list): The axis to apply the drop.
            how (str): How to drop the NA values.
                'all': drop the label if all values are NA.
                'any': drop the label if any values are NA.
            thresh (int): The minimum number of NAs to require.
            subset ([label]): Labels to consider from other axis.
            inplace (bool): Change this DataFrame or return a new DataFrame.
                True: Modify the data for this DataFrame, return None.
                False: Create a new DataFrame and return it.

        Returns:
            If inplace is set to True, returns None, otherwise returns a new
            DataFrame with the dropna applied.
        """
        raise NotImplementedError("Not yet")
        if how != 'any' and how != 'all':
            raise ValueError("<how> not correctly set.")

@ray.remote
def _reduce_by_index(ray_df, func):
    """
    Perform a groupby and a function on the result.

    Args:
        ray_df (ray.DataFrame): The DataFrame to apply to.
        func (callable): The function to apply after the groupby.

    Returns:
        A list of partitions, each containing a pandas DataFrame with the
        result of the groupby and function provided.
    """
    return [_deploy_func.remote(func, partition) for partition in ray.get(_groupby.remote(ray_df))]

@ray.remote
def _groupby(ray_df):
    """
    Group by the index (in current implementation) and return a list of
    partitions. The groupby triggers a shuffle to ensure correctness.

    Args:
        ray_df (ray.DataFrame): The DataFrame to groupby.

    Returns:
        A list of partitions, each containing a pandas DataFrame with the
        result of the groupby.
    """
    indices = list(set([index for df in ray.get(ray_df.df) for index in list(df.index)]))

    chunksize = int(len(indices) / len(ray_df.df))
    partitions = []
    
    indices_copy = indices
    for df in ray_df.df:
        partitions.append(_shuffle.remote(df, indices, chunksize))
    
    partitions = ray.get(partitions)
    
    # Transpose the list of dataframes
    # TODO find a better way
    new_partitions = []
    for i in range(len(partitions[0])):
        new_partitions.append([])
        for j in range(len(partitions)):
            new_partitions[i].append(partitions[j][i])
    
    return [_local_groupby.remote(partition) for partition in new_partitions]

@ray.remote
def _shuffle(df, indices, chunksize):
    """
    Sends data in blocks defined by the chunksize provided to the Ray object
    store. This serves as the shuffle function.

    Args:
        df (pd.DataFrame): The pandas DataFrame to shuffle.
        indices ([any]): The list of indices for the DataFrame.
        chunksize (int): The number of indices to send.

    Returns:
        The list of pd.DataFrame objects in order of their assignment. This
        order is important because it determines which task will get the data.
    """
    i = 0
    partition = []
    while len(indices) > chunksize:
        oids = df.reindex(indices[:chunksize]).dropna()
        partition.append(oids)
        indices = indices[chunksize:]
        i += 1
    else:
        oids = df.reindex(indices).dropna()
        partition.append(oids)
    return partition

@ray.remote
def _local_groupby(df_rows):
    """
    Apply a groupby on this partition for the blocks sent to it.

    Args:
        df_rows ([pd.DataFrame]): A list of dataframes for this partition. Goes
            through the Ray object store.

    Returns:
        A DataFrameGroupBy object from the resulting groupby.
    """
    concat_df = pd.concat(df_rows)
    return concat_df.groupby(concat_df.index)

@ray.remote
def _deploy_func(func, dataframe, *args):
    """
    Deploys a function for the map_partitions call.

    Args:
        dataframe (pandas.DataFrame): The pandas DataFrame for this partition.

    Returns:
        A futures object representing the return value of the function
        provided.
    """
    if len(args) == 0:
        return func(dataframe)
    else:
        return func(dataframe, *args)

def from_pandas(df, npartitions=None, chunksize=None, sort=True):
    """
    Converts a pandas DataFrame to a Ray DataFrame. It splits the DataFrame
    across the Ray Object Store.

    Args:
        df (pandas.DataFrame): The pandas DataFrame to convert.
        npartitions (int): The number of partitions to split the DataFrame
            into. Has priority over chunksize.
        chunksize (int): The number of rows to put in each partition.
        sort (bool): Whether or not to sort the df as it is being converted.

    Returns:
        A new Ray DataFrame object.
    """
    if sort and not df.index.is_monotonic_increasing:
        df = df.sort_index(ascending=True)
    
    if npartitions is not None:
        chunksize = int(len(df) / npartitions)
    elif chunksize is None:
        raise ValueError("The number of partitions or chunksize must be set.")
    
    #TODO stop reassigning df
    dataframes = []
    while len(df) > chunksize:
        top = ray.put(data[:chunksize])
        dataframes.append(top)
        df = df[chunksize:]
    else:
        dataframes.append(ray.put(df))

    return DataFrame(dataframes, list(df.columns))

def to_pandas(df):
    """
    Converts a Ray DataFrame to a pandas DataFrame.

    Args:
        df (ray.DataFrame): The Ray DataFrame to convert.

    Returns:
        A new pandas DataFrame.
    """
    return pd.concat(ray.get(df.df))

data = pd.DataFrame(data={'col1': [1, 2, 3, 4], 'col2': [3, 4, 5, 6]})
ray.init()
ray_df = from_pandas(data, 2)
sums = ray_df.map_partitions(lambda df: df.sum()).reduce_by_index(lambda df: df.sum())
print(ray_df)
print(ray_df.T)
