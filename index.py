print("Hello, Reply with either yes or no")

animal_posibility = "Dog, Cat, Donkey, Camel, Horse, Goat, Sheep, Buffallo, Cow, Llama, Domestic pig, Chicken, duck, turkey, pigeon, Guinea Fowl, Dove, canary, parrot,peakcork,rabbit, pinch"
choice = input("Does this animal have feathers?\n")
yes = 'yes'
no = "no"
unavailableChoice = "Sorry, this program can not predict your animal"

if(choice == yes) :
    animal_posibility = "Chicken, duck, turkey, pigeon, Guinea Fowl, Dove, canary, parrot,peakcork, pinch"
    print("Your Animal Posibilities are: "+animal_posibility)
   #Continuation of condition checking from first branch
    choice = input("Does this animal usually lay two eggs in the nest for breeding?\n")
    if(choice == yes):
       animal_posibility = " pigeon,  Dove, canary, parrot, Finch"
       print("Your Animal Posibilities are: "+animal_posibility)
       #continue
       choice = input("Can this animal immitate human voice?\n")
       if(choice == yes):
        animal_posibility = "parrot"
        print("Your Animal Posibilities are: "+animal_posibility)
       else:
        animal_posibility = " pigeon,  Dove, canary, Finch"
        print("Your Animal Posibilities are: "+animal_posibility)
        choice = input("Does this animal prefer to live solidarily?\n")
        if(choice == yes):
          animal_posibility = "canary"  
          print("Your Animal Posibilities are: "+animal_posibility)
        else:
           animal_posibility = " pigeon,  Dove, Finch"
           print("Your Animal Posibilities are: "+animal_posibility)
           choice = input("Does this animal prefer to live near human settlements?\n")
           if(choice == yes):
             animal_posibility = " pigeon"
             print("Your Animal Posibilities are: "+animal_posibility)
           else:
            animal_posibility = "Dove, Finch"
            print("Your Animal Posibilities are: "+animal_posibility)
            choice = input("Does one of the species of this animal have zebra in its name?\n")
            if(choice == yes):
              animal_posibility = "Finch"
              print("Your Animal Posibilities are: "+animal_posibility)  
            else:
                animal_posibility = "Dove"
                print("Your Animal Posibilities are: "+animal_posibility)

    else:
        animal_posibility = "Duck, Guiney, fowl, peakcork,Turkey, Chicken"
        print("Your Animal Posibilities are: "+animal_posibility)
        choice = input("Can this animal swim in water?\n")
        if(choice == yes):
            animal_posibility = "Duck"
            print("Your Animal Posibilities are: "+animal_posibility)
        else:
           animal_posibility = "Guiney fowl, peakcork,Turkey, Chicken"
           print("Your Animal Posibilities are: "+animal_posibility)
           choice = input("Is this animal famous for its dancing?\n")
           if(choice == yes):
             animal_posibility = "peakcork"
             print("Your Animal Posibilities are: "+animal_posibility)
           else:
             animal_posibility = "Guiney fowl,Turkey, Chicken"
             print("Your Animal Posibilities are: "+animal_posibility)
             choice = input("Is this animal famous for dinner in thanks giving?\n")
             if(choice == yes):
                animal_posibility = "Turkey"
                print("Your Animal Posibilities are: "+animal_posibility)
             else:
                animal_posibility = "Guiney fowl, Chicken"
                print("Your Animal Posibilities are: "+animal_posibility)
                choice = input("Is this animal favourite stable food for most canadians?\n")
                if(choice == yes):
                     animal_posibility = "Chicken"
                     print("Your Animal Posibilities are: "+animal_posibility)
                else:
                    animal_posibility = "Guiney fowl"
                    print("Your Animal Posibilities are: "+animal_posibility)

else :
    animal_posibility = "Dog, Cat, Donkey, Camel, Horse, Goat, Sheep, Buffallo, Cow, Llama, Domestic pig, rabbit"
    print("Your Animal Posibilities are: "+animal_posibility)

    choice = input("Can humans consume its milk/meat?\n")
    if(choice == yes) :
        animal_posibility = "Donkey, Camel, Horse, Goat, Sheep, Buffallo, Cow, Llama, Domestic pig, rabbit"
        print("Your Animal Posibilities are: "+animal_posibility)
        #Continuation of condition checking from SEcond branch Left
        choice = input("Can humans ride this animal or use it as a means of communication?\n")
        if(choice == yes):
            animal_posibility = "Donkey, Camel, Horse, Buffallo, Cow, Llama"
            print("Your Animal Posibilities are: "+animal_posibility)
            #Continue
            choice = input("Does this animal associate with deserts?\n")
            if(choice == yes):
                animal_posibility = "Camel"
                print("Your Animal Posibilities are: "+animal_posibility)
            else:
                animal_posibility = "Donkey, Horse, Buffallo, Cow, Llama"
                print("Your Animal Posibilities are: "+animal_posibility)

                choice = input("Does this animal Belong to South America?\n")
                if(choice == yes):
                  animal_posibility = "Llama"
                  print("Your Animal Posibilities are: "+animal_posibility)  
                else:
                    animal_posibility = "Donkey, Horse, Buffallo, Cow"
                    print("Your Animal Posibilities are: "+animal_posibility)
                    choice = input("Is this animal considered faithful to its owner?\n")
                    if(choice == yes):
                        animal_posibility = "Horse"
                        print("Your Animal Posibilities are: "+animal_posibility)
                    else:
                        animal_posibility = "Donkey, Buffallo, Cow"
                        print("Your Animal Posibilities are: "+animal_posibility)
                        choice = input("Does this animal prefer water and mainly found in Asia?\n")
                        if(choice == yes):
                            animal_posibility = "Buffallo"
                            print("Your Animal Posibilities are: "+animal_posibility)
                        else:
                            animal_posibility = "Donkey, Cow"
                            print("Your Animal Posibilities are: "+animal_posibility)
                            choice = input("Is this animal a main source of milk in Canada?\n")
                            if(choice == yes):
                               animal_posibility = "Cow"
                               print("Your Animal Posibilities are: "+animal_posibility) 
                            else:
                              animal_posibility = "Donkey"
                              print("Your Animal Posibilities are: "+animal_posibility)  
        else:
            animal_posibility = "Goat, Sheep, Domestic pig, rabbit"
            print("Your Animal Posibilities are: "+animal_posibility)
            #continue
            choice = input("Does this animal usually make a burrow?\n")
            if(choice == yes):
              animal_posibility = "rabbit"
              print("Your Animal Posibilities are: "+animal_posibility)  
            else:
              animal_posibility = "Goat, Sheep, Domestic pig"
              print("Your Animal Posibilities are: "+animal_posibility)  
              #continue
              choice = input("Is this animal prohibitted to consume in Islam?\n")
              if(choice == yes):
                animal_posibility = "Domestic pig"
                print("Your Animal Posibilities are: "+animal_posibility)
              else:
                 animal_posibility = "Goat, Sheep" 
                 choice = input("Does this animal give us wool?\n")
                 if(choice == yes):
                   animal_posibility = "Sheep" 
                   print("Your Animal Posibilities are: "+animal_posibility)
                 else:
                  animal_posibility = "Goat" 
                  print("Your Animal Posibilities are: "+animal_posibility) 
    else :
        animal_posibility = "Dog, Cat"
        print("Your Animal Posibilities are: "+animal_posibility)

    #The end of a condition
    choice = input("Is this animal considered a man's best friend?\n")
    if(choice == yes) :
        animal_posibility = "Dog"
        print("Your Animal Posibilities are: "+animal_posibility)
    elif(choice == no) :
        animal_posibility = "Cat"
        print("Your Animal Posibilities are: "+animal_posibility)
    else:
        print(unavailableChoice)