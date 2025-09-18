import os
import json
import boto3
from kubernetes import client, config


def handler(event, context):
    """
    Função Lambda para coletar métricas do Kubernetes e enviá-las para o CloudWatch.
    Esta função se conecta ao cluster usando a configuração in-cluster.
    """
    try:
        # Carrega a configuração do cluster a partir do ambiente de execução da Lambda.
        # Isso funciona quando a Lambda está rodando dentro do seu cluster Kubernetes.
        config.load_incluster_config()
        v1 = client.CoreV1Api()

        # Coleta o número de pods em todos os namespaces
        pods = v1.list_pod_for_all_namespaces(watch=False)
        pod_count = len(pods.items)

        print(f"Número de Pods encontrados: {pod_count}")

        # Envia a métrica para o CloudWatch
        cloudwatch = boto3.client('cloudwatch')
        cloudwatch.put_metric_data(
            MetricData=[
                {
                    'MetricName': 'NumberOfPods',
                    'Dimensions': [
                        {
                            'Name': 'ClusterName',
                            'Value': os.environ['CLUSTER_NAME']
                        },
                    ],
                    'Unit': 'Count',
                    'Value': pod_count
                },
            ],
            Namespace='Kubernetes/Metrics'
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Métricas enviadas com sucesso para o CloudWatch.')
        }

    except Exception as e:
        print(f"Erro ao coletar ou enviar métricas: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Falha na execução: {str(e)}")
        }