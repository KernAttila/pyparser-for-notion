from notion_parser import parse_property
    
# Parse pages coming from a Notion database
# This example assumes the database has the following properties:
# - Alias (text)
# - Canonical Name (text)
# - Origin (text)
# - Destination (text)
# - Address (place)
# - Entry Type (select with options: transfer, account, place, category)

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
    else:
        return entry_type, {"alias": alias}

# Loop over input items and add a new field called 'my_new_field' to the JSON of each one
database_entries = {}
for item in _items:
    cache_type, info = parse_account_cache(item["json"]["properties"])
    database_entries.setdefault(cache_type, []).append(info)

return {"json":{"database_entries":database_entries}}