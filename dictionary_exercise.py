country={"china":143,"india":136,"USA":32,'Pakistan':21}

def print_values():
    for key, value in country.items():
        print(key+"==>"+str(value))

def add_values():
    new_key= input("Enter the new Country:")
    if new_key in country:
        print("The country already exists")
    else:
        new_value = input("enter the population:")
        country[new_key]=int(new_value)
        print_values()

def remove_values():
    remove_country=input("Which Country to be removed?\t")
    if remove_country.lower()in country:
        del country[remove_country]
        print_values()
    else:
        print("No such country exists")

def query_values():
    query_country=input("Which country you want to query?")
    print("The population of "+query_country+" is: "+str(country[query_country]))


def main ():
    user_input = input("Enter the Input add||remove||print||query||:")
    if user_input.lower()=='add':
        add_values()

    if user_input.lower()=='remove':
        remove_values()

    if user_input.lower()=='print':
        print_values()

    if user_input.lower()=='query':
        query_values()

if __name__=='__main__':
    while(1):
        main()