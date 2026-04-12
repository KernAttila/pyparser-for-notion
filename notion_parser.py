

def get_parse_method(item_type):
    if item_type == "property":
        return parse_property
    elif item_type == "text":
        return parse_text
    elif item_type == "rich_text":
        return parse_rich_text
    elif item_type == "title":
        return parse_rich_text
    elif item_type == "mention":
        return parse_mention
    elif item_type == "select":
        return parse_select
    elif item_type == "multi_select":
        return parse_multi_select
    elif item_type == "place":
        return parse_place
    else:
        return do_nothing
    
def do_nothing(item):
    print(f"Unknown type: {item['type']}")
    return None

def parse_mention(item_mention):
    mention = item_mention["mention"]
    if mention["type"] == "user":
        return mention["user"]["name"]
    elif mention["type"] == "page":
        return mention["page"]["id"]
    elif mention["type"] == "database":
        return mention["database"]["id"]
    else:
        return None

def parse_property(property):
    parse_method = get_parse_method(property["type"])
    return parse_method(property[property["type"]])

def parse_text(text):
    return text["plain_text"]

def parse_rich_text(item_text):
    text = ""
    for _text in item_text:
        parse_method = get_parse_method(_text["type"])
        text += str(parse_method(_text)).strip()
    return text

def parse_select(item_select):
    if item_select is None:
        return None
    return item_select["name"]

def parse_multi_select(item_multi_select):
    if item_multi_select is None:
        return None
    return [select["name"] for select in item_multi_select]

def parse_place(item_place):
    if item_place is None:
        return None
    return item_place
    # address = item_place["address"]
    # latitude = item_place["lat"]
    # longitude = item_place["lon"]
    # return f"{address} (lat: {latitude}, lon: {longitude})"
