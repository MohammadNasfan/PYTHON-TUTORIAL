# p13.py
# Analyzes inventory for total products, low stock, out-of-stock, and highest stock item.
# total products
# out-of-stock products
# low-stock products
# product with highest stock
def analyze_inventory(inventory):
    total_products=0
    out_of_stock=[]
    low_stock_products=[]
    highest_stock=0
    highest_product=0
    
    for i in inventory:
        total_products+=1
        product = i[0]
        stock = i[1]
        if stock==0:
            out_of_stock.append(i[0])
        if stock!=0 and stock<5:
             low_stock_products.append(i[0])
        if stock>highest_stock:
            highest_stock=stock
            highest_product=product

        
        
             
        
    
       
              
            
    return total_products,out_of_stock,low_stock_products,highest_product




print(analyze_inventory([
    ["Rice", 5],
    ["Sugar", 0],
    ["Milk", 12],
    ["Bread", 2],
    ["Eggs", 0]
]))