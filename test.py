import json
import pprint
cache_db = "\\\\Andromeda\\docker\\n8n\\n8n-data\\cache_database.json"
from notion_parser import parse_property
    
def parse_account_cache(properties):
    alias = parse_property(properties["Alias"])
    canonical = parse_property(properties["Canonical Name"])
    origin = parse_property(properties["Origin"])
    destination = parse_property(properties["Destination"])
    address = parse_property(properties["Address"])
    entry_type = parse_property(properties["Entry Type"])
    if entry_type == "transfer":
        return entry_type, {"alias": alias, "origin": origin, "destination": destination}
    elif entry_type == "account":
        return entry_type, {"alias": alias, "canonical": canonical, "origin": origin}
    elif entry_type == "place":
        return entry_type, {"alias": alias, "canonical": canonical, "address": address}
    elif entry_type == "category":
        return entry_type, {"alias": alias, "canonical": canonical}
    elif entry_type is None:
        return "error - no type", {"alias": alias}
    else:
        return entry_type, {"alias": alias}

with open(cache_db, 'r', encoding='utf-8') as f:
    _items = json.load(f)
# Loop over input items and add a new field called 'my_new_field' to the JSON of each one
test = {}
for item in _items:
    if "json" in item:
        cache_type, info = parse_account_cache(item["json"]["properties"])
    else:
        cache_type, info = parse_account_cache(item["properties"])
    test.setdefault(cache_type, []).append(info)

pprint.pprint({"json":{"test":test}})

"🥪Takeout"