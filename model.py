import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_URL = os.getenv("API_URL")
api_token = os.getenv("API_TOKEN")
headers = {"Authorization": f"Bearer {api_token}"}
def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
text = """**The Apple: A Fruit of Many Virtues**

The apple, a simple yet profound fruit, has been a part of human history for thousands of years. Its origins can be traced back to Central Asia, where wild apple trees still flourish today. Over time, the cultivation of apples spread across continents, and today, they are grown in over 100 countries worldwide.

Apples are not just popular for their sweet, tart taste but also for their nutritional benefits. They are rich in dietary fiber, vitamin C, and antioxidants. The old adage "An apple a day keeps the doctor away" holds some truth as regular consumption of apples can contribute to overall health and wellness.

The apple tree is a deciduous tree in the rose family best known for its sweet fruit, the apple. It is cultivated worldwide as a fruit tree and is the most widely grown species in the genus Malus. The tree originated in Central Asia, where its wild ancestor, Malus sieversii, is still found today.

Apples have been grown for thousands of years in Asia and Europe and were brought to North America by European colonists. Apples have religious and mythological significance in many cultures, including Norse, Greek, and European Christian tradition.

Apple trees are large if grown from seed. Generally, apple cultivars are propagated by grafting onto rootstocks, which control the size of the resulting tree. There are more than 7,500 known cultivars of apples, resulting in a range of desired characteristics. Different cultivars are bred for various tastes and use, including cooking, eating raw and cider production.

In the 2010s, genome sequencing of both wild apples and domesticated ones supports the idea that the first domesticated apple grew wild in Kazakhstan and that in 4,000 BCE people began to propagate it through grafting. This discovery was backed up by further genetic analysis in 2017.

In conclusion, the humble apple is much more than just a fruit. It's a symbol of health and vitality, a testament to the ingenuity of agricultural practices, and a staple food that has nourished countless generations. Whether enjoyed fresh off the tree or baked into a delicious pie, apples continue to delight our taste buds while providing essential nutrients.

"""
data = query({"inputs": text})
print(data[0]["summary_text"])