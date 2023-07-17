class Crew:

    def __init__(self, numberofmember, cost, numberofequipments, time):

        self.numberofmember = numberofmember

        self.cost = cost

        self.numberofequipments = numberofequipments

        self.time = time

    # Hourly work rate is the time surpasses for 1 unit of work that is completed by one crew member

    def hourlyworkrate(self, percentage = 1):

        return percentage / (self.time * self.numberofmember)
    
    # Cost efficency rate is the money that you have spent for 1 unit of work for one crew member

    def costefficency(self, percentage = 1):

        return percentage / (self.cost * self.numberofmember)
    
    # Time & Cost efficency rate is the time and the money that you have spent for 1 unit of work for one crew member
    
    def timeandcost_efficency(self, percentage):    
        
        return percentage / (self.cost * self.time * self.numberofmember)
    
    # Suffiency of the equipments for desired crew's determined members
    
    def sufeq(self):

        if self.numberofequipments / self.numberofmember >= 1:

            return True
        
        else:

            return False

    class ComparisonToolbox:
        
        def __init__(self, *crew):
        
            self.crew = crew

        # Hourly work rate list
        
        def hwr_comparison(self):
            
            hwrates = []
            
            for crew_member in self.crew:
            
                hwrates.append(crew_member.hourlyworkrate())
                
            return hwrates

        # Cost efficency list
        
        def cost_comparison(self):
        
            costs = []
        
            for crew_member in self.crew:
            
                costs.append(crew_member.costefficency())
        
            return costs

        # Time and cost efficency list
        
        def timeandcost_comparison(self):
            
            timeandcosts = []
            
            percentage = 1  # Define the percentage value as needed
            
            for crew_member in self.crew:
                
                timeandcosts.append(crew_member.timeandcost_efficency(percentage))
            
            return timeandcosts
    
# Creating a variable with crew class

crew1 = Crew(4, 100, 5, 36)

crew2 = Crew(5, 88, 6, 28)

crew3 = Crew(6, 189, 5, 26)

Crews = [crew1, crew2, crew3]

comparison_toolbox = Crew.ComparisonToolbox(*Crews)

crew1_hwr = crew1.sufeq()

# Methods of Crew.ComparisonToolbox()

hwr_comparison_values = comparison_toolbox.hwr_comparison()

cost_comparison_values = comparison_toolbox.cost_comparison()

timeandcost_comparison_values = comparison_toolbox.timeandcost_comparison()

print(hwr_comparison_values)

print(cost_comparison_values)

print(timeandcost_comparison_values)