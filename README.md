## LLM-GNN

Learning representations of text-attributed graphs (TAGs) like citation networks (arxiv) has become crucial for node classification. 

The OGBN-arxiv dataset consists of scientific publications classified into multiple categories, derived from the Microsoft Academic Graph.

Traditionally, node features in the OGBN-arxiv dataset are generated through a skip-gram model trained on text data from the MAG corpus. While this method provides a baseline, it may not fully leverage the contextual depth needed for precise classification.

Data Collected from OGBN Archives:

Nodes: 169343,  Edges: 1166243

Original Graph - UniDirectional 

Process Graph: Convert it to bi-directional graph, add self-loops

Generate Text-Based Embeddings: 
- Using Gemini 
- Using Voyage 
- Using OpenAI 
- Using T5-3b encoder
  
Replicate the node features for the graph with these embeddings
Train GAT for node classification 

Model	Test Accuracy:

OpenAI	68.71%

Voyage	68.80%

T5-3b	68.71%

Gemini	68.93%

Skip-gram	72.83%




                  








