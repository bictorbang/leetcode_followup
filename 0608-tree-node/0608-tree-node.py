import pandas as pd
import numpy as np

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    tree.loc[tree['id'].isin(tree['p_id']), "type"] = "Inner" 
    tree.loc[tree['p_id'].isna(), "type"] = "Root" ###
    tree.loc[tree['type'].isna(), "type"] = "Leaf" 
    return (tree[['id', 'type']])