from rocrate.rocrate import ROCrate
import json
from pathlib import Path
import pandas as pd
from humanize import naturalsize
import re

def get_create_action(crate, datafile):
    actions = crate.get_by_type("CreateAction")
    for action in actions:
        props = action.properties()
        for result in props["result"]:
            if result["@id"] == datafile:
                return action

crate = ROCrate("./")
root = crate.get("./").properties()
gw_section = crate.get(root["mainEntityOfPage"]["@id"])
code_repo = crate.get(root["isBasedOn"]["@id"])
md = f"# {root['name']}\n\n"
md += f"*{root['description']}*\n\n"
md += f"These datasets were generated using notebooks in the [{code_repo['name']}]({code_repo['url']}) repository.\n\n"
md += f"For more information and documentation see the [{gw_section['name']}]({gw_section['url']}) section of the [GLAM Workbench](https://glam-workbench.net)."
md += "\n\n## Dataset summary\n"
details = "\n\n## Dataset details"

for datafile in crate.get_by_type(["File", "Dataset"]):
    md += f"- [{datafile['name']}]({datafile['url']}) ({naturalsize(datafile['contentSize'])}, {datafile['encodingFormat']})\n"
    details += f"\n\n### [{datafile['name']}]({datafile['url']})\n\n"
    action = get_create_action(crate, datafile["@id"])
    nb = crate.get(action["instrument"]["@id"])
    stats = {
        "date harvested": datafile["dateModified"],
        "file size": naturalsize(datafile["contentSize"]),
        "format": datafile['encodingFormat'],
        "created by": f"<a href='{nb['url']}'>{nb['name']}</a>"
    }
    if rows := datafile.get("size"):
        stats["number of rows"] = rows
    details += pd.DataFrame([stats]).T.style.format(thousands=",").hide(axis=1).to_html() + "\n\n"
    if "conformsTo" in datafile:
        details += "### Columns\n\n"
        with Path(datafile["conformsTo"]["@id"]).open() as json_file:
            df = pd.json_normalize(json.load(json_file), record_path="fields")
        df["name"] = df["name"].apply(lambda x: f"`{x}`")
        details += df.to_markdown(index=False)

md += details

md += "\n\n----\nCreated by [Tim Sherratt](https://timsherratt.au) for the [GLAM Workbench](https://glam-workbench.net)"

md = re.sub(r'<style type="text/css">\s*</style>', '', md)
Path("README.md").write_text(md)
