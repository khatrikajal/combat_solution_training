def is_calculation_query(text: str) -> bool:
    calc_keywords = ["calculate", "what is", "solve", "+", "-", "*", "/", "=", "evaluate"]
    return any(kw in text.lower() for kw in calc_keywords)

def route_query(query: str) -> str:
    if is_calculation_query(query):
        return "calc"
    return "llm"
