"""
Return True is there exist a trusted connection to given node from the node 0, else return False
"""

def IsTrusted(node, trustGraph, pretrustedPeers, trustThreshold):
    if not pretrustedPeers:
        return False
    if not any(trustGraph):
        return False
    queue = [(node, 0)]
    visited = set()
    while queue:
        curr, dist = queue.pop(0)
        if curr in pretrustedPeers and dist <= trustThreshold:
            return True
        visited.add(curr)
        for i in range(len(trustGraph)):
            if trustGraph[curr][i] != 0 and i not in visited:
                queue.append((i, dist + trustGraph[curr][i]))
    return False


