def handle_build(repo, spec):
    print(f"Building project from {repo} with spec {spec}...")
    # Simulate creating a unique build ID
    import hashlib, time
    build_id = hashlib.sha256(f"{repo}-{spec}-{time.time()}".encode()).hexdigest()[:10]
    print(f"Build complete. Resource ID: {build_id}")
    # In a real system, you'd push this to IPFS and register on-chain
