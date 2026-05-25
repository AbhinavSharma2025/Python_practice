def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor =="unknown":
            raise ValueError("we don't know that flavour")
    except ValueError as e:
        print("Error: ",e)
    
    else:
        print(f"{flavor} chai is served")
    
    finally:
        print("Next customer")        


serve_chai("masala")
serve_chai("unknown")
