from qdrant_client import QdrantClient, models
import os
from feature_extraction import compute_feature_vector

class QdrantHandler:
    def __init__(self):
        self.client = QdrantClient(":memory:")  # In-memory DB
        self.collection_name = "frames"
        self.vector_size = 512
        self.client.recreate_collection(
            collection_name=self.collection_name,
            vectors_config=models.VectorParams(
                size=self.vector_size, distance=models.Distance.COSINE
            )
        )

    def insert_frame(self, id, image_path):
        vector = compute_feature_vector(image_path)
        self.client.upsert(
            collection_name=self.collection_name,
            points=[
                models.PointStruct(id=id, vector=vector, payload={"path": image_path})
            ]
        )

    def search_similar(self, image_path, limit=5):
        query_vector = compute_feature_vector(image_path)
        search_result = self.client.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=limit
        )
        return search_result
