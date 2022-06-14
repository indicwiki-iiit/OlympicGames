import sweetviz as sv
import pandas as pd

DF = pd.read_csv('./New_Athletes_With_Attributes.csv')

report = sv.analyze(DF)
report.show_html()
