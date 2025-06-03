#
#
#


#int

top50 = ["Kendrick Lamar", "Kendrick Lamar", "Kendrick Lamar", "Kendrick Lamar", "Kendrick Lamar", "Kendrick Lamar", "Kendrick Lamar", "Kendrick Lamar", "Gracie Abrams", "Tyler, The Creator", "Kendrick Lamar", "Kendrick Lamar", "Lady Gaga", "Gigi Perez", "Kendrick Lamar", "Kendrick Lamar", "ROSÉ", "Billie Eilish", "Tyler, The Creator", "Jimin", "The Weeknd", "Cynthia Erivo", "Sabrina Carpenter", "Brenda Lee", "Mariah Carey", "Chappell Roan", "Billie Eilish", "Tyler, The Creator", "Bobby Helms", "Gracie Abrams", "Wham!", "Shaboozey", "GloRilla", "Sabrina Carpenter", "Post Malone", "Stromae", "The Kid LAROI", "Teddy Swims", "Sabrina Carpenter", "Oscar Maydon", "Benson Boone", "Kendrick Lamar", "The Marías", "Ariana Grande", "Ariana Grande", "Morgan Wallen", "Chappell Roan", "The Neighbourhood", "Noah Kahan", "Sabrina Carpenter"]
enroll = [4237, 19200, 38500, 19100, 45200, 51800, 27800, 22000, 4300, 30400, 22500, 17200, 25500, 14700, 23000, 31500, 33600, 42500, 21700, 29700, 46000, 25000, 10600, 33200, 33800, 15900, 29100, 20300, 56800, 56100, 30800, 41900, 25000, 38200, 26400, 52800, 32700, 17700, 42700, 51200, 43700, 33000, 33400, 27700, 21700, 39300, 29200, 15000, 19200, 8800, 12400, 22600, 30800, 13200, 41200, 21500, 17300, 24300, 46000, 50300, 21900, 47800, 22200, 30000, 4600, 35500, 25800, 21600, 26300, 21900, 29800, 39400, 20000, 21200, 12300, 34900, 68100, 28500, 25300, 25000, 23200, 22700, 30900, 46600, 28600, 43400, 7100, 70900, 34900, 32800, 11800, 15100, 50100, 50700, 14500, 16500, 22900, 10400, 40000, 28900, 51800, 69400, 38800, 38200, 23100, 18100, 14100, 4300, 21900, 68600, 45400, 32200, 30600, 30500, 45700, 25100, 30700, 33000, 29400, 13100, 24400, 33400, 8100, 47900, 30600, 30000, 20300, 22900, 44400, 12400]
school = ["Air Force", "Akron", "Alabama", "Appalachian State", "Arizona", "Arizona State", "Arkansas", "Arkansas State", "Army", "Auburn", "Ball State", "Baylor", "Boise State", "Boston College", "Bowling Green", "Buffalo", "BYU", "California", "Central Michigan", "Charlotte", "Cincinnati", "Clemson", "Coastal Carolina", "Colorado", "Colorado State", "Duke", "East Carolina", "Eastern Michigan", "FIU", "Florida", "Florida Atlantic", "Florida State", "Fresno State", "Georgia", "Georgia Southern", "Georgia State", "Georgia Tech", "Hawaii", "Houston", "Illinois", "Indiana", "Iowa", "Iowa State", "Kansas", "Kansas State", "Kent State", "Kentucky", "Liberty", "Louisiana", "Louisiana–Monroe", "Louisiana Tech", "Louisville", "LSU", "Marshall", "Maryland", "Memphis", "Miami (FL)", "Miami (OH)", "Michigan", "Michigan State", "Middle Tennessee", "Minnesota", "Mississippi State", "Missouri", "Navy", "NC State", "Nebraska", "Nevada", "New Mexico", "New Mexico State", "North Carolina", "North Texas", "Northern Illinois", "Northwestern", "Notre Dame", "Ohio", "Ohio State", "Oklahoma", "Oklahoma State", "Old Dominion", "Ole Miss", "Oregon", "Oregon State", "Penn State", "Pittsburgh", "Purdue", "Rice", "Rutgers", "San Diego State", "San Jose State", "SMU", "South Alabama", "South Carolina", "South Florida", "Southern Miss", "Stanford", "Syracuse", "TCU", "Temple", "Tennessee", "Texas", "Texas A&M", "Texas State", "Texas Tech", "Toledo", "Troy", "Tulane", "Tulsa", "UAB", "UCF", "UCLA", "UConn", "UMass", "UNLV", "USC", "UTEP", "UTSA", "Utah", "Utah State", "Vanderbilt", "Virginia", "Virginia Tech", "Wake Forest", "Washington", "Washington State", "West Virginia", "Western Kentucky", "Western Michigan", "Wisconsin", "Wyoming"]

#function
def artist_name(name, list):
    name = list.count("Kendrick Lamar")
    print(name)
artist_name("Kendrick Lamar", top50)


#Print the name of the NCAA Division I team with the highest enrollment
def high_enrollment():
    largestNum = 0
    global enroll
    for number in enroll:
        if number > largestNum:
            largestNum = number
    print(largestNum)
    for i in range (len(enroll)):
        if enroll[i]:
            type = enroll.index(enroll)
            print(school[type])
            print(largestNum)
#high_enrollment doesnt work/isnt finished

#main
high_enrollment()
