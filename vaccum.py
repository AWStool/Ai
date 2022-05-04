def vacuumcleaner():
    final_condition = {'A': '0', 'B': '0'}  # desired condition
    cost = 0

    location_input = "A"
    cost += 1
    roomA_condition = input("Enter status of A ")
    roomB_condition = input("Enter status of B ")
    final_condition={'A':roomA_condition,'B':roomB_condition}
    print(final_condition)

    if location_input == 'A':
        # Location A is Dirty.
        print("Vacuum is placed in Location A")
        if roomA_condition == '1':
            print("Location A is Dirty.")
            final_condition['A'] = '0'
            cost += 1
            print("Cost for cleaning A " + str(cost))
            print("Location A has been Cleaned.")

            if roomB_condition == '1':
                # if B is Dirty
                print("Location B is Dirty.")
                print("Moving right to the Location B. ")
                cost += 1
                print("Cost for moving right " + str(cost))
                final_condition['B'] = '0'
                cost += 1
                print("Cost for cleaning " + str(cost))
                print("Location B has been Cleaned. ")
            else:
                print("No action" + str(cost))
                print("Location B is already clean.")

        if roomA_condition == '0':
            print("Location A is already clean ")
            if roomB_condition == '1':
                print("Location B is Dirty.")
                print("Moving right to the Location B. ")
                cost += 1
                print("Cost for moving right " + str(cost))
                final_condition['B'] = '0'
                cost += 1
                print("Cost for cleaning" + str(cost))
                print("Location B has been Cleaned. ")
            else:
                print("No action " + str(cost))
                print(cost)
                print("Location B is already clean.")

    else:
        print("Vacuum is placed in location B")
        # Location B is Dirty.
        if roomB_condition == '1':
            print("Location B is Dirty.")
            final_condition['B'] = '0'
            cost += 1
            print("Cost for cleaning " + str(cost))
            print("Location B has been Cleaned.")

            if roomA_condition == '1':
                print("Location A is Dirty.")
                print("Moving left to the Location A. ")
                cost += 1
                print("Cost for moving left " + str(cost))
                final_condition['A'] = '0'
                cost += 1
                print("cost for cleaning " + str(cost))
                print("Location A has been Cleaned.")

            else:
                print("No action" + str(cost))
                print("Location A is already clean.")

        else:
            print(cost)
            print("Location B is already clean.")

            if roomA_condition == '1':
                # if A is Dirty
                print("Location A is Dirty.")
                print("Moving left to the Location A. ")
                cost += 1
                print("Cost for moving left ", cost)
                final_condition['A'] = '0'
                cost += 1
                print("Cost for cleaning " + str(cost))
                print("Location A has been Cleaned. ")
            else:
                print("No action " + str(cost))
                print("Location A is already clean.")

    print("total cost considering the initial location and the other possibility ", cost + cost)


vacuumcleaner()
