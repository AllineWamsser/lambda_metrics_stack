import json
import random

def main(event, context):
    """
    Simulates Kubernetes metrics collection and logs them.
    """
    metrics = {
        "cpu_usage": f"{random.randint(10, 80)}%",
        "memory_usage": f"{round(random.uniform(0.5, 2.0), 2)}Gi"
    }

    result = {
        "status": "success",
        "cluster": "demo-cluster",
        "metrics": metrics
    }

    print(json.dumps(result, indent=2))
    return result