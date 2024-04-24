import pandas as pd 

import textwrap
import numpy as np
import pandas as pd

import google.generativeai as genai
import google.ai.generativelanguage as glm

from IPython.display import Markdown

API_KEY = "Your_API_Key_Here"

genai.configure(api_key=API_KEY)

#print the models which we have
for m in genai.list_models():
  if 'embedContent' in m.supported_generation_methods:
    print(m.name)

model = 'models/embedding-001'
# Get the embeddings of each text and add to an embeddings column in the dataframe
def embed_fn(title, text):
  print(text)
  return genai.embed_content(model=model,
                             content=text,
                             task_type="classification",
  )['embedding']

data = pd.read_csv('/Users/akshada/Desktop/akshada/LLM-GNN/LLMGNN/data/processed.csv')
data = data[0:50000]
print(data.columns)

data["Embeddings"] = data.apply(lambda row: embed_fn(row['title'], row['abstract']), axis=1)
print(data)
data.to_csv("embeddings_generated.csv", index = False)
# df['Embeddings'] = df.apply(lambda row: embed_fn(row['Title'], row['Text']), axis=1)
# df