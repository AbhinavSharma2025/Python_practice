def chai(flavour):
    if flavour not in ["masala","elaichi","ginger"]:
        raise ValueError ("Tea not identified....")
    print(f"brewing {flavour} chai")

chai("masala")