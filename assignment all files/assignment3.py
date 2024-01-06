flow_1 = {
    "intent": "product_info",
    "entities": [
        {"entity": "product", "prompt": "can you please enter what are you searching ?"},
        {"entity": "location", "prompt": "Please enter your location ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}

flow_2 = {
    "intent": "ask_price",
    "entities": [
        {"entity": "product", "prompt": "can you please enter what are you searching ?"},
        {"entity": "location", "prompt": "Please enter your location ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}

flow_3 = {
    "intent": "ask_price",
    "entities": [
        {"entity": "order_id", "prompt": "Please enter your order id ?"}
    ],
    "api_data": {
        "url": "https://rasatest.free.beeceptor.com/"
    }
}

all_flows = [flow_1, flow_2, flow_3]
urls = []
for flow in all_flows:
    urls.append(flow["api_data"]["url"])
print("All URLs: ", urls)
new_entity = {"entity": "new_entity", "prompt": "new entity?"}
flow_3["entities"].append(new_entity)
print("\nFlow 3 with new entity:", flow_3)
new_url = input('enter url ')
for flow in all_flows:
    flow["api_data"]["url"] = new_url
print("\n Updated flows with new URL:", all_flows)
entity_to_delete = "product"
updated_entities = []
for entity in flow_1["entities"]:
    if entity["entity"] != entity_to_delete:
        updated_entities.append(entity)
flow_1["entities"] = updated_entities
print("\n Flow 1 after deleting entity:", flow_1)
