from kubernetes import client, config

# Configs can be set in a configuration class or directly using a helper utility
config.load_kube_config()

v1 = client.CoreV1Api()
print("Listing all pods with their IP:")
ret = v1.list_pod_for_all_namespaces(watch=False)
for i in ret.items:
    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))
    