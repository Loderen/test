import logging
import random  
from typing import List, Optional

import pandas as pd
from IPython.display import display
from pandas.io.formats.style import Styler
from pybatfish.client.session import Session 
from pybatfish.datamodel import Edge, Interface
from pybatfish.datamodel.answer import TableAnswer
from pybatfish.datamodel.flow import HeaderConstraints, PathConstraints  
from pybatfish.datamodel.route import BgpRoute 
from pybatfish.util import get_html

logging.getLogger("pybatfish").setLevel(logging.WARN)

pd.set_option("display.max_colwidth", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.html.use_mathjax", False)

_STYLE_UUID = "pybfstyle"

class MyStyler(Styler):
    def __repr__(self):
        return repr(self.data)


def show(df):
    if isinstance(df, TableAnswer):
        df = df.frame()
    if not isinstance(df, pd.DataFrame) or df.size == 0:
        display(df)
        return
    display(
        MyStyler(df)
        .set_uuid(_STYLE_UUID)
        .format(get_html)
        .set_properties(**{"text-align": "left", "vertical-align": "top"})
    )