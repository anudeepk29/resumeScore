#!pip install sentence_transformers
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the model
model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

# Sample Job Description and Resume
job_description_file = "/job_description.txt"
with open(job_description_file, 'r') as f:
  job_description = f.read()

resume_file = "/resume.txt"
with open(resume_file, 'r') as f:
  resume = f.read()

# Encode the job description and resume to get their embeddings
job_desc_embedding = model.encode([job_description])
resume_embedding = model.encode([resume])

# Compute the cosine similarity
similarity_score = cosine_similarity(job_desc_embedding, resume_embedding)[0][0]

# Display the similarity score
