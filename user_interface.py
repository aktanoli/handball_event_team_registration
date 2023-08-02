from datetime import date

from team import Team

# Creating class for UserInterface
class UserInterface:
    def __init__(self, fee=200):
        # Create an empty list that will store all the teams.
        self.__teams = []

        #Fee variable that store the fee of each team that is mandatory to pay in order take part in the event.
        self.__fee = fee

    # Method to create the unique ID for each Team object.
    def unique_id(self):
        #The ID wil be 1 for the first team that is being created.
        if len(self.__teams) == 0:
            return 1
        else:
            # Get all the ID that has been created from the team list.
            team_id = max(self.__teams, key=lambda team: team.get_id())
            if team_id:
                # New ID will be the last ID in the list + 1
                return team_id.get_id() + 1
            else:
                return 1     

    # Create a new team.
    def team_registration(self):
        print("\n\t\tREGISTER A NEW TEAM:")

        # Create a while loop that will ask the user to enter a team name and it's end when the user enters a valid value. 
        while True:
            t_name = str(input("Please Enter Your Team Name: ")).strip()  # strip() method is used to remove the trailing spaces.
            if t_name:
                break

        # Create another while loop to enter a team type. 
        # And it will end when the user enters a valid value that is boys or girls.
        while True:
            # strip() method is used to remove the  trailing spaces.
            # lower() method is used to convert in to lower case(), if the user enters 'BOYs' or 'Boys'
            team_type = str(input("Please Enter Your Team Type (boys/girls): ")).strip().lower()
            if team_type != "boys" and team_type != "girls":
                print("You Have Enter A Wrong Team Type!")
            else:
                break
        # Create a while loop to confirm the fees has paid or not by the team.
        # And it will end when the user choose the correct value (Y/N).
        while True:
            fee_paid = str(input("Has the team paid the fee? (Y/N) ")).strip().upper()
            if fee_paid != "Y" and fee_paid != "N":
                print("You Have Enter A Wrong Input!")
            else:
                if fee_paid == "Y":
                    fee_paid = True
                else:
                    fee_paid = False
                break
        
        # Get the new ID for the current team to be created
        u_id = self.unique_id()

        # Get the today's date
        today = date.today()

        # Create new Team object
        team_object = Team(u_id, today, t_name, team_type, fee_paid)

        # Add the Team object to the list
        self.__teams.append(team_object)

        print(f"\n>> Your Team '{t_name}' Registered Successfully!")

    def update_the_team(self):
        # Check if the user changes to a team object.
        user_made_changes = False

        # Use try and except block to handle the error.
        try:
            u_id = int(input("\nPlease Enter Your Team ID: "))
            # List comprehension is used to search the team with the user input ID in the list.
            find_team = [team for team in self.__teams if team.get_id() == u_id]

            # If matched:
            if find_team:
                # List with 1 element is found as a result.
                find_team = find_team[0]
                print(f"\n\t\tTEAM ID {find_team.get_id()} UPDATE")

                # Print the name of current team
                print(f"Name: {find_team.get_name()}")

                # Choose whether to update or skip the current name
                update_name = str(input("Update Your Team Name (leave space to skip): ")).strip()
                if update_name:
                    user_made_changes = True
                    find_team.set_name(update_name)

                # Print the type of current team.
                print(f"Type: {find_team.get_type()}")
                while True:
                    # Choose wheter to update or skip the team type.
                    update_type = str(input("Update Your Team Type (boys/girls) (leave space to skip): ")).strip().lower()
                    if update_type != "boys" and update_type != "girls" and update_type:
                        print("You Have Enter A Wrong Team Type!")
                    elif not update_type:
                        break
                    else:
                        user_made_changes = True
                        find_team.set_type(update_type)
                        break

                # If any changes has found to the team
                if user_made_changes:
                    # Ask the user to confirm the update.
                    confirm_change = str(input("Are the Changes Confirm? (Y/N): ")).strip().upper()
                    if confirm_change == "Y":
                        # Find the team in the list by matching the team ID
                        for x in range(len(self.__teams)):
                            if self.__teams[x].get_id() == find_team.get_id():
                                # And update with object has made.
                                self.__teams[x] = find_team
                                break
                        print("YOU HAVE UPDATED THE TEAM SUCCESSFULLY!")
                    else:
                        print("YOU HAVE NOT MADE ANY CHANGE.")

            else:
                print(f"No Team Found with ID {u_id} !")
        except:
            print("You Have Enter A Wrong Team ID!")

    

    # Fee pay function is created to pay team fee.
    def pay_your_fee(self):
        # Use try and except block to handle the error.
        try:
            u_id = int(input("\nPlease Enter Your Team ID: "))
            # List comprehension is used to search the team with the user input ID in the list.
            find_team = [team for team in self.__teams if team.get_id() == u_id]
            if find_team:
                # List with 1 element is found as a result.
                find_team = find_team[0]

                # If condition is used to confirm the fee has paid by this team
                if find_team.get_paid_fee():
                    print(f"\nTeam'{find_team.get_name()}' Has Already Paid The Fee.")
                else:
                    # Ask the user to confirm the paymnet (Y/N)
                    confirm_change = str(input("Are You Confirm To pay The Fee? (Y/N): ")).strip().upper()
                    if confirm_change == "Y":
                        find_team.set_fee_paid(True)
                        for x in range(len(self.__teams)):
                            if self.__teams[x].get_id() == find_team.get_id():
                                self.__teams[x] = find_team
                                break
                        print("YOU HAVE PAID THE FEE SUCCESSFULLY!")
                    else:
                        print("YOU HAVE NOT MADE ANY CHANGE.")

            else:
                print(f"No Team Found with ID {u_id} ")
        except:
            print("You Have Enter A Wrong Team ID!")

    def team_delete(self):
        # Use try and except block to handle the error.
        try:
            u_id = int(input("\nPlease Enter Your Team ID: "))
            # List comprehension is used to search the team with the user input/this ID in the list.
            find_team = [team for team in self.__teams if team.get_id() == u_id]

            if find_team:
                # List with 1 element is found as a result.
                find_team = find_team[0]
                print(f"Team Found with ID {find_team.get_id()}.")

                # User have to select the option to confirm the change
                confirm_change = str(input(f"Are You Confirm to Delete '{find_team.get_name()}'? (Y/N): ")).strip().upper()
                if confirm_change == "Y":
                    # List comprehension is used to filter the list by deleting the team with that ID
                    self.__teams = [team for team in self.__teams if team.get_id() != u_id]
                    print(f"TEAM {find_team.get_name()} DELETED SUCCESSFULLY!")
                else:
                    print("YOU HAVE NOT MADE ANY CHANGE.")
            else:
                print(f"No Team Found with ID {u_id} !")
        except:
            print("You Have Enter A Wrong Team ID!")

    def cancel_participation_in_the_team(self):
        # Use try and except block to handle the error.
        try:
            u_id = int(input("\nPlease Enter Your Team ID: "))
            # List comprehension is used to search the team with the user input ID in the list.
            find_team = [team for team in self.__teams if team.get_id() == u_id]

            if find_team:
                # List with 1 element is found as a result.
                find_team = find_team[0]

                # If condition is used to find this team has cancelled the participation
                if find_team.get_cancel_date():
                    print(f"\nTeam '{find_team.get_name()}' Has Already Cancelled The Participation.'")
                else:
                    # Ask the user to confirm the change (Y/N)
                    confirm_change = str(input(
                        f"Are You Confirm Cancelling The participation For '{find_team.get_name()}'? (Y/N): ")).strip().upper()
                    if confirm_change == "Y":
                        find_team.set_date_cancel(date.today())
                        for x in range(len(self.__teams)):
                            if self.__teams[x].get_id() == find_team.get_id():
                                self.__teams[x] = find_team
                                break
                        print(f"YOU HAVE SUCCESSFULLY CANCELLED THE PARTICIPATION FOR TEAM '{find_team.get_name()}'!")
                    else:
                        print("YOU HAVE NOT MADE ANY CHANGE.")

            else:
                print(f"No Team Found with ID {u_id}!")
        except:
            print("You Have Enter A Wrong Team ID!")

    def get_team_by_id(self):
        # Use try and except block to handle the error.
        try:
            u_id = int(input("\nPlease Enter Your Team ID: "))
            # List comprehension is used to search the team with the user input/this ID in the list.
            find_team = [team for team in self.__teams if team.get_id() == u_id]
            if find_team:
                print("------------------------------------")
                # List with 1 element is found as a result.
                print(find_team[0], end="")
                print("------------------------------------")
            else:
                print(f"No Team Found with ID {u_id}!")
        except:
            print("You Have Enter A Wrong Team ID!")
    # Create a method to delete a team
    
    
    def paid_fee_amount(self):
        # List comprehension is used to get all the teams that has paid the fee.
        count_paid_fee = len([team for team in self.__teams if team.get_paid_fee()])
        fee_amount = count_paid_fee * self.__fee
        print(f"\n${fee_amount} COLLECTED FROM FEES.")

    def paid_fee_percent(self):
        # List comprehension is used to get all the teams that has paid the fee.
        count_paid_fee = len([team for team in self.__teams if team.get_paid_fee()])

        # Number of teams
        number_of_teams = len(self.__teams)
        if number_of_teams == 0:
            fee_paid_percent = 0
        else:
            # Formula to calculate the percentage
            fee_paid_percent = (count_paid_fee / number_of_teams) * 100.0
        print(f"\nTHERE ARE {fee_paid_percent}% OF TEAMS WHO PAID THEIR FEE")

    # Method is created to print all the teams in the list.
    def get_all_teams(self):
        print(f"\n\t\tLIST OF ALL TEAMS ({len(self.__teams)})")
        if self.__teams:
            print("------------------------------------")
            for team in self.__teams:
                # We can use the team object in the method print(), because we have implemented the method __str__() in class Team.
                print(team, end="")
                print("------------------------------------")
        else:
            print("\n>> There are no teams registered!")

    def get_team_type(self):
        # Create a while loop to enter a team type. 
        # And it will end when the user enters a valid value that is boys or girls.
        while True:
            team_type = str(input("\nPlease Enter Your Team Type (boys/girls): ")).strip().lower()
            if team_type != "boys" and team_type != "girls":
                print("You Have Enter A Wrong Input!")
            else:
                break

        # List comprehension is used to find in the list, the team with this type
        teams_found = [team for team in self.__teams if team.get_type() == team_type]
        print(f"\n\t\t{team_type.upper()} LIST OF TEAMS ({len(teams_found)})")

        if teams_found:
            print("------------------------------------")
            for team in teams_found:
                print(team, end="")
                print("------------------------------------")
        else:
            print("\n No Team Found!")

    def number_of_teams(self):
        # Count all the teams
        count_teams = len(self.__teams)
        print(f"\n THERE ARE {count_teams} TEAM(S) REGISTERED.\n")
    

    def menu(self):
        print("\n\t\tWELCOME TO HANDBALL EVENT MENU")
        print("1. Register A New Team")
        print("2. Handball Team Detail By ID")
        print("3. Handball Teams Detail By Their Type (boys or girls)")
        print("4. Show All Handball Teams Details In A List")
        print("5. Update A Team By ID")
        print("6. Delete A Team By ID")
        print("7. Check Fee Status of A Team By Their ID")
        print("8. Want To Cancel Team Participation?")
        print("9. Show The Number of Teams Registered")
        print("10. Percent of teams that has paid their fee")
        print("11. Save All The Teams's Data In A Text File")
        print("12. Read All Detail of The Teams From A Text File")
        print("13. Show All The Amount Collected From Fees")
        print("0. Exit the program")

    



    # Create Method to save the data in a file
    def save_data(self):
        if len(self.__teams) == 0:
            print("\nNo Teams Data Found to Write!\n")
        else:
            # Use try and except block to handle the error.
            try:
                # Open the file for writing
                with open('teams.txt', 'w') as file:
                    # For loop is used to loop the TEAM list to write the file.
                    for team in self.__teams:
                        file.write(team.get_data_for_file())
                        # Add new line
                        file.write("\n")
                print("\nTeams Data Has Been Written Successfully!\n")
            except:
                print("\nFOUND AN ERROR!\n")

    def read_file_data(self):
        # Use try and except block to handle the error.
        try:
            # Open the file for reading
            with open('teams.txt', 'r') as file:
                # Read a list line by line
                content = file.readlines()

            if len(content) > 0:
                #If there is any data contains in the file, clear the current list
                self.__teams.clear()
                # Loop the list file content that contains string
                for l in content:
                    # Remove the new line characters and any white spaces
                    l = l.replace("\n", "").strip()

                    # To convert the string into a list by using split method.
                    # Separate the values (id, date, name, etc ) by comma
                    val = l.split(",")
                    id_ = int(val[0])
                    date_ = val[1]
                    teamname_ = val[2]
                    team_type = val[3]

                    if val[4] == 'True':
                        fee_paid = True
                    else:
                        fee_paid = False
                    date_cancel = val[5]

                    # Create a object name Team
                    team = Team(id_, date_, teamname_, team_type, fee_paid)
                    if date_cancel != 'None':
                        team.set_date_cancel(date_cancel)

                    # Add the Team object in the list
                    self.__teams.append(team)
                print("\nData Has Been Read Successfully!\n")
            else:
                print("\nThe File is Empty!\n")
        except:
            print("\nFOUND AN ERROR!\n")

    # Create a Handball teams management function 
    def go(self):
        # Create a while loop to print all the available menu items, the user can exit by pressing '0'.
        while True:
            self.menu()
            user_selection = -1

            # Use try and except block to prevent non-integer value.
            try:
                user_selection = int(input("Please Select Any One From The Menu: "))
            except:
                pass

            # According to the user choice, do the corresponding action.
            # Each action is linked with a corresponding method.
            if user_selection == 1:
                self.team_registration()
            elif user_selection == 2:
                self.get_team_by_id()
            elif user_selection == 3:
                self.get_team_type()
            elif user_selection == 4:
                self.get_all_teams()
            elif user_selection == 5:
                self.update_the_team()
            elif user_selection == 6:
                self.team_delete()
            elif user_selection == 7:
                self.pay_your_fee()
            elif user_selection == 8:
                self.cancel_participation_in_the_team()
            elif user_selection == 9:
                self.number_of_teams()
            elif user_selection == 10:
                self.paid_fee_percent()
            elif user_selection == 11:
                self.save_data()
            elif user_selection == 12:
                self.read_file_data()            
            elif user_selection == 13:
                self.paid_fee_amount()                       
            elif user_selection == 0:
                print("Exit.")
                break
            else:
                print("YOU HAVE SELECT THE WRONG OPTION! TRY ANOTHER!")
