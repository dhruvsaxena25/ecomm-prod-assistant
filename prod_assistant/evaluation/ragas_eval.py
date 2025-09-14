import asyncio
from utils.model_loader import ModelLoader
from ragas import SingleTurnSample
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingWrapper
from ragas.metrics import LLMContextPrecisionWithoutReference, ResponseRelevancy
from grpc.experimental.aio import grpc_aio
grpc_aio.init_grpc_aio()

model_loader = ModelLoader()


