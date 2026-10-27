"""Cache package — Semantic vector memory for selector healing."""

from kernhell.cache.cache_manager import CacheManager
from kernhell.cache.embedder import SemanticEmbedder, cosine_similarity
from kernhell.cache.schemas import CacheEntry, CacheStats

__all__ = [
    "CacheEntry",
    "CacheManager",
    "CacheStats",
    "SemanticEmbedder",
    "cosine_similarity",
]
