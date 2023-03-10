from Regex_Test import *
import pandas as pd
import re

params = "14o04dsyat|da2z3jfdx3d|d2l072rynmf|dztqn3bkuwh|dfmb6iq56n5|d7xs85pykcu|dvqk0dkd51b|d90hjr4el8l|dbd171yzas4|dvvk2r9v353|de5m4c82vod|dx9866ycpch|d5ddll7nteq|d2srky66y97|dvd8udw1jqe|dvzi5fpwsq0|diz8r4lp07j|d8oqbcgxhj0|dtma0oq0ats|d1ehw5b9die|dycnajocapo|ddil37ploig|d7u1uvgihyw|d1833s85ts2|d4mc93567gb|dqfyrpst1bz|d4pyjk1z1w1|djjckmwy5pi|dxbqzrhhdc9|dd6onnun705|dm3oommazg8|dslh1tsjdj6|ddpa2x3w3wj|dw596qixgpz|dr52bcy810p|d5g974q5j16|dza0y29y5eh|dd56hr0q4df|dw74i50a4wt|dhs21thyr70|dzpf4amz64m|d6actylcgfa|d44ej9j7l47|db8xu9shxm7|d6q30kb7stc|dbsylp97lg7|dl6xwkkba1h|d1vh6svslg2|dj2x0sl776i|d2duc9h7l38|dwdht98vi78|dh9bl9zks10|dclz8y1bxzk|d8tvnc0ncc2|d5z3415l8ln|dievz48ix8q|d3ielvetr2k|dslqoio5hb8|d99qflczbxl|d20l7n61550|d21gjfeyqir|di5te0hrcyt|dfl0bcxe45h|d2d78e09uxp|dg4r4ntotgc|d5v115zjlkg|dlf0m5ws7kj|dk96eccnuuk|d86sjit3cni|diugeorptgq|dos9gqysk6n|djwa19u3v76|dcjm86hyyug|d4tcd5ykm5w|dlbc113hg63|dntwm29hxky|d4d5ie2l90c|d4hozsoz5cm|djoxqbakjs3|djzrt98k1qq|dxk0qz2rg6h|dmqth8vpv6s|doqq53p272o|dumszb47v6w|d7g4h1lo9lq|derz1ui2h5x|d6k31roz7dm|d3ngzpqhom7|d34proc48v6|d7hpkskdjmj|d2g8dshl4qz|d2gcivc2mjk|dbvcqv4j6pm|d4ugwv9refv|ditdszl7d4a|d3zto48butl|dh3fo3hyv6n|dkol4ethwnv|d8daz828zlq|d48qxdgtd0n|ddepi2rihqa|devewllmaxs|ddee9cxe1ur|d1s3rtsk3t4|d33bjw9gt2t|dor7mz5dez8|dyd7mwc6e6x|dw8ais74p2x|dxwgf3l0m9h|dqiwqrk0oxv|dcdt03k5k6h|d119znctkln|dnwtknv0k5k|dwsl5synb95|dvoetk0dry6|d6ke5m5pgwx|dmt4ijnhl4l|d2gik0gj847|dfpfpc95b1f|d60m1q9yfqp|dnyg1j4h2ha|dp2pubxsf20|d1rvd7przsn|dqxay7a31us|dyfnzj8jxpu|d4r7ow01c7f|dm5l9orqdxr|d8ge8xhxg84|dcj4hxa5ezj|d3h7vnsbh5i|dpar2g7e9u0|d8hc9ehlo48|dvccsf8t91l|d1atfyrwnh5|dve6uvx4dtd|dv1vhjjenyo|d65xy103w8i|dlbeiq96137|d6xm6w7t6za|d33wf5xyeqw|djp0h836h80|dw4bvzdivot|dgr0kbqaywb|df2ttaqn16w|dxhb0npgj29|d4p7hwo32q6|dn0em1r64yz|dq7zj7miobx|dm8tmi994db|d5334zl9jhl|dcksi8jk3dk|dfc6vuk7tkj"


df = pd.read_csv("C://Users//rafael_fagundes//OneDrive - Dell Technologies//Documents//1153793_Untitled_Report_20230309_160522_4048829742.csv", on_bad_lines='skip', skiprows=10)

pd.set_option('display.max_columns', None)

df_filtered = df[df["Placement"].str.contains(params)]
df_filtered = df_filtered.reset_index()

df_filtered["Audience ID"] = ""

for index, row in df_filtered.iterrows():
    df_filtered.at[index,"Audience ID"] = getAudienceID(row["Placement"])

df_filtered.to_csv("C://Users//rafael_fagundes//OneDrive - Dell Technologies//Desktop//filtered.csv")

