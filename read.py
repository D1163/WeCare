# read.py
def load_products():
    try:
        with open("products.txt", "r") as file:
            d = {} #dictionary to store product data
            p_id = 1
            for line in file:
                #removing newline
                line = line.replace('\n', '').replace('\r', '')
                if line:
                    parts = line.split(',')
                    if len(parts) >= 5:
                        #adding product data to dictionary
                        d[p_id] = {
                            'name': parts[0].replace('\n', '').replace('\r', '').replace(' ', ''),
                            'brand': parts[1].replace('\n', '').replace('\r', '').replace(' ', ''),
                            'quantity': int(parts[2].replace('\n', '').replace('\r', '').replace(' ', '')),
                            'cost_price': float(parts[3].replace('\n', '').replace('\r', '').replace(' ', '')),
                            'origin': parts[4].replace('\n', '').replace('\r', '').replace(' ', '')
                        }
                        p_id += 1
            return d
    except FileNotFoundError:
        #handle the case where files do not exist
        print("Error: products.txt file not found")
        return {}
    except Exception as e:
        #handling any other exception that may occur
        print("Error loading products:", e)
        return {}
