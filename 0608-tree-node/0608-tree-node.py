import pandas as pd
import numpy as np

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    parents = tree.p_id.unique()
    def tree_type(x):
        if pd.isna(x.p_id): return "Root"
        if x.id not in parents: return "Leaf"
        return "Inner"
    tree["type"] = tree.apply(tree_type, axis = 1)
    return tree[["id", "type"]]